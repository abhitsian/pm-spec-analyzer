# Adding Screenshot to GitHub

## Quick Steps:

1. Take a screenshot of the upload screen (showing the clean UI)

2. Copy it to the repo:
   ```bash
   cp ~/Desktop/[your-screenshot-name].png screenshots/upload-screen.png
   ```

3. Commit and push:
   ```bash
   git add screenshots/upload-screen.png
   git commit -m "Add upload screen screenshot"
   git push origin main
   ```

The README already references `screenshots/upload-screen.png` so it will show up automatically!
