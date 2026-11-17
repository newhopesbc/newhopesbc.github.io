# Google Drive 사진 자동 연동 설정

Google Drive 폴더 ID: `1VkU0ARAWvaTCJ2gwUrw5I_INg_iScaVA`

현재 ZIP에는 사진 자체가 포함되지 않습니다. 아래 최초 설정이 완료되면 GitHub Actions가 사진을 가져와 갤러리에 표시합니다. 기존 YouTube Actions와는 독립적으로 동작합니다.

1. Google Cloud Console에서 프로젝트를 선택하고 **Google Drive API**를 활성화합니다.
2. **IAM 및 관리자 > 서비스 계정**에서 서비스 계정을 생성합니다. 서비스 계정의 **키 > 새 키 추가 > JSON**으로 키를 다운로드합니다. JSON 키는 절대 홈페이지 파일이나 공개 GitHub 저장소에 올리지 마세요.
3. 서비스 계정 이메일 주소(`...@...iam.gserviceaccount.com`)를 복사합니다.
4. Google Drive에서 해당 사진 폴더의 **공유**를 눌러 서비스 계정 이메일을 **뷰어**로 추가합니다. 개인 계정 Drive에서는 조직 정책에 따라 공유가 제한될 수 있습니다. 폴더에 있는 사진이 공유 권한을 상속받는지 확인합니다.
5. GitHub 저장소 > **Settings > Secrets and variables > Actions > New repository secret**에서 이름을 `GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON`으로 만들고 다운로드한 JSON 파일 **내용 전체**를 값으로 넣습니다.
6. GitHub 저장소의 파일을 이 ZIP 내용으로 업데이트합니다. 기존 `videos.json`은 삭제하지 마세요. `.github/workflows/update-youtube.yml`도 유지하세요.
7. **Actions > Update Church Gallery > Run workflow**를 눌러 첫 실행을 합니다. 성공하면 `gallery.json`과 `assets/gallery/*.jpg`가 생성됩니다. 이후 매일 자동 갱신됩니다.

## 작동 방식
- 최근 업로드 사진 최대 24장을 읽어 홈페이지용으로 리사이즈하고 저장합니다.
- 사진은 공개 GitHub Pages 저장소에 커밋되므로, **공개에 동의한 사진만 이 폴더에 넣으세요**.
- 사진이 없는 경우, 권한 오류가 난 경우, 사진을 읽을 수 없는 경우에는 작업이 실패하며 기존 갤러리 데이터는 유지됩니다.
- Drive 폴더의 사진을 삭제하면 다음 성공적인 동기화 때 홈페이지 갤러리에서도 제거됩니다.
- GitHub Actions는 예약 시간보다 늦게 실행될 수 있습니다.
- HEIC 사진은 Pillow 기본 설치에서 지원되지 않을 수 있으므로 JPG/PNG/WebP 권장.
