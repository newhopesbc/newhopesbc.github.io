# New Hope Korean Baptist Church — V3

A static bilingual website ready for GitHub Pages. The Sermons section plays the five newest **completed, public, embeddable livestreams** inside the website and provides a “More” link to the church YouTube Streams page. No YouTube account administrator access is needed.

## Setup

1. Create a **public** GitHub repository and upload all files and folders, including `.github/workflows/update-youtube.yml`.
2. In GitHub repository **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)**. Save.
3. Create a Google Cloud project and enable **YouTube Data API v3**. Create an API key. For security, restrict the key to YouTube Data API v3; do not place it in the website HTML/JavaScript. Do not use HTTP referrer restrictions for this server-side key.
4. In GitHub repository **Settings → Secrets and variables → Actions → New repository secret**, set name `YOUTUBE_API_KEY` and paste the API key as its value.
5. In **Actions → Update Sunday worship videos → Run workflow**, run once. The workflow generates `videos.json`, commits it to `main`, and GitHub Pages deploys it. Future updates are scheduled once daily (GitHub schedules may run late).
6. Check the public website and verify that the embedded video plays. Some video owners may restrict embedding.

### Important
- Before the first successful workflow run, the page shows a clear setup notice rather than invented sample videos.
- Only completed livestreams are included. If the church uploads ordinary recordings instead of streaming, the script must be adapted.
- The script checks the latest 100 uploads (up to 200 requested) and shows up to five eligible videos; if there are fewer, it shows fewer.
- GitHub Pages serves static files only. The GitHub Action uses the API key privately and commits only public video metadata.
- If workflow commits fail, verify **Settings → Actions → General → Workflow permissions → Read and write permissions**.
- The automatic update runs once per day, not instantly upon upload. You can manually run the workflow anytime.
- Service times, church description, and address remain placeholders until confirmed.


## V4 update
Worship schedule, street address and phone from the November 15, 2026 church bulletin. Verify schedule with church before visiting.
