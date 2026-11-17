"""Sync church photos from a Google Drive folder for paginated display."""
import io
import json
import os
import re
from pathlib import Path

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
from PIL import Image, ImageOps

FOLDER_ID = '1VkU0ARAWvaTCJ2gwUrw5I_INg_iScaVA'
OUT = Path('assets/gallery')
OUT.mkdir(parents=True, exist_ok=True)

secret = os.environ.get('GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON', '')
if not secret:
    raise RuntimeError('Missing GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON GitHub secret')
info = json.loads(secret)
credentials = service_account.Credentials.from_service_account_info(
    info, scopes=['https://www.googleapis.com/auth/drive.readonly'])
session = AuthorizedSession(credentials)

photos = []
token = None
while True:
    params = {
        'q': f"'{FOLDER_ID}' in parents and trashed = false and (mimeType = 'image/jpeg' or mimeType = 'image/png' or mimeType = 'image/webp' or mimeType = 'image/heic')",
        'fields': 'nextPageToken,files(id,name,mimeType,createdTime)',
        'pageSize': 100,
        'orderBy': 'createdTime desc',
        'supportsAllDrives': 'true',
        'includeItemsFromAllDrives': 'true',
    }
    if token:
        params['pageToken'] = token
    response = session.get('https://www.googleapis.com/drive/v3/files', params=params, timeout=40)
    response.raise_for_status()
    data = response.json()
    photos.extend(data.get('files', []))
    token = data.get('nextPageToken')
    if not token:
        break

if not photos:
    raise RuntimeError('No photos visible to service account. Check folder sharing and files.')

photos = sorted(photos, key=lambda x: x.get('createdTime', ''), reverse=True)
manifest = []
for photo in photos:
    fid = photo['id']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', fid):
        continue
    resp = session.get(f'https://www.googleapis.com/drive/v3/files/{fid}', params={'alt': 'media'}, timeout=90)
    resp.raise_for_status()
    if len(resp.content) > 30_000_000:
        print('Skipping oversized photo:', photo['name'])
        continue
    try:
        with Image.open(io.BytesIO(resp.content)) as im:
            im = ImageOps.exif_transpose(im).convert('RGB')
            im.thumbnail((1600, 1200))
            path = OUT / f'{fid}.jpg'
            im.save(path, format='JPEG', quality=82, optimize=True)
    except Exception as exc:
        print('Skipping unreadable image:', photo['name'], exc)
        continue
    manifest.append({'file': str(path), 'name': photo['name']})

if not manifest:
    raise RuntimeError('No supported images could be converted.')
keep = {Path(item['file']).name for item in manifest}
for existing in OUT.glob('*.jpg'):
    if existing.name not in keep:
        existing.unlink()
Path('gallery.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Synced {len(manifest)} church photos')
