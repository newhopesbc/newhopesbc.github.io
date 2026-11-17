# 교회 사진 페이지 기능 (V12)

- 최신 사진부터 한 페이지에 6장씩 표시합니다.
- 사진 아래 페이지 번호 또는 화살표로 이전 사진을 볼 수 있습니다.
- 기존 Google Drive 하루 1회 동기화는 유지합니다.
- 기존 24장 제한을 제거했습니다. 사진이 매우 많아지면 GitHub 저장소 용량과 실행 시간이 늘어날 수 있습니다.

## GitHub 업데이트
기존 파일을 삭제하지 말고 다음 두 파일만 각각 같은 경로에 덮어씁니다.
- `index.html`
- `scripts/sync_drive_gallery.py`

`gallery.json`, `assets/gallery/`, `videos.json`, `CNAME`, `.github/workflows/update-youtube.yml`, `.github/workflows/update-drive-gallery.yml`은 그대로 유지하세요.

업데이트 후 GitHub Actions > Update Google Drive Gallery > Run workflow를 한 번 실행하면 기존 24장 제한 없이 사진 목록을 갱신합니다.
