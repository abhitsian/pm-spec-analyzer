# Setup Guide

## Prerequisites

1. Claude Code installed
   - Test: `claude --version`
   - Install: https://claude.com/claude-code

2. Python 3.8+
   - Test: `python3 --version`

## Installation

```bash
git clone https://github.com/abhitsian/pm-spec-analyzer.git
cd pm-spec-analyzer
pip3 install streamlit python-docx
streamlit run app_simplified.py
```

Or use installer:
```bash
./install.sh && ./run.sh
```

App opens at `http://localhost:8501`

## Troubleshooting

### Claude Code not found

Check paths:
- `~/.local/bin/claude`
- `/usr/local/bin/claude`
- `/opt/homebrew/bin/claude`

### Module not found: streamlit

```bash
pip3 install streamlit python-docx
```

### Word documents won't upload

```bash
pip3 install python-docx
```

Then restart app.

### Port in use

```bash
pkill -f streamlit
streamlit run app_simplified.py
```

## Usage

1. Upload spec
2. Get analysis
3. Select stage
4. Answer questions
5. Generate improved spec

## Storage

Sessions saved to: `~/.pm_spec_analyzer/sessions/`
