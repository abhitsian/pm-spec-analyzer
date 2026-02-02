#!/bin/bash

echo "🚀 PM Spec Analyzer - Complete Push to GitHub"
echo "=============================================="
echo ""

# Check if repo exists on GitHub
echo "Checking if you've created the GitHub repo..."
echo ""

cd ~/spec_analyzer

# Try to push
echo "Attempting to push..."
echo ""
echo "If prompted for credentials:"
echo "  Username: abhitsian"
echo "  Password: Use your GitHub Personal Access Token"
echo ""
echo "Don't have a token? Create one at:"
echo "  https://github.com/settings/tokens/new"
echo "  (Check 'repo' scope)"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Your code is on GitHub!"
    echo ""
    echo "🎉 Repository URL:"
    echo "   https://github.com/abhitsian/pm-spec-analyzer"
    echo ""
    echo "📖 Share with your team:"
    echo "   git clone https://github.com/abhitsian/pm-spec-analyzer.git"
    echo "   cd pm-spec-analyzer"
    echo "   ./install.sh && ./run.sh"
    echo ""
    echo "👥 Next: Add team members as collaborators!"
    echo "   https://github.com/abhitsian/pm-spec-analyzer/settings/access"
    echo ""
else
    echo ""
    echo "⚠️  Push failed. Common fixes:"
    echo ""
    echo "1. Make sure you created the repo at:"
    echo "   https://github.com/new"
    echo "   Name: pm-spec-analyzer"
    echo ""
    echo "2. Get a Personal Access Token:"
    echo "   https://github.com/settings/tokens/new"
    echo "   - Name it 'PM Spec Analyzer'"
    echo "   - Check 'repo' scope"
    echo "   - Copy the token"
    echo ""
    echo "3. Try again with: ./COMPLETE_PUSH.sh"
    echo "   Use token as password when prompted"
    echo ""
fi
