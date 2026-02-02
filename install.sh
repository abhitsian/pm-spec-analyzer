#!/bin/bash

echo "🚀 Installing PM Spec Analyzer - Socratic Coach"
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+ first."
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check for Claude Code
if ! command -v claude &> /dev/null; then
    echo "⚠️  Claude Code CLI not found in PATH"
    echo "   Make sure it's installed: https://claude.com/claude-code"
    echo "   The app will check common installation locations when it runs."
    echo ""
else
    echo "✅ Claude Code found: $(claude --version 2>&1 | head -n1)"
    echo ""
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installation complete!"
    echo ""
    echo "🚀 To start the app, run:"
    echo "   streamlit run app_simplified.py"
    echo ""
    echo "   Or use the quick command:"
    echo "   ./run.sh"
    echo ""
else
    echo ""
    echo "❌ Installation failed. Try:"
    echo "   pip3 install --user streamlit python-docx"
    exit 1
fi
