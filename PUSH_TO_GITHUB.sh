#!/bin/bash

echo "🚀 Pushing PM Spec Analyzer to GitHub..."
echo ""

cd ~/spec_analyzer

# Check if remote exists
if git remote | grep -q origin; then
    echo "✅ Remote 'origin' already configured"
else
    echo "Adding remote..."
    git remote add origin https://github.com/abhitsian/pm-spec-analyzer.git
fi

echo ""
echo "📤 Pushing to GitHub..."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🎉 Your repo is live at:"
    echo "   https://github.com/abhitsian/pm-spec-analyzer"
    echo ""
    echo "Next steps:"
    echo "1. Go to repo Settings → Collaborators"
    echo "2. Add your team members"
    echo "3. Share the setup instructions!"
else
    echo ""
    echo "❌ Push failed. You may need to:"
    echo "1. Create the repo at: https://github.com/new"
    echo "2. Authenticate with GitHub (gh auth login)"
    echo "3. Try again"
fi
