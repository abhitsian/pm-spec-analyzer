# PM Spec Analyzer

Socratic review tool for PM specs. Analyzes your spec, asks one question at a time to improve your thinking, then provides actionable feedback.

**Based on Claude Code's AskUserQuestion tool** - uses the same Socratic questioning pattern to clarify thinking, applied to product spec review.

![Upload Screen](screenshots/upload-screen.png)

## What It Does

1. Upload spec (filename becomes title)
2. Initial analysis across 8 dimensions
3. Select stage: Early Draft, Developing, or Final Review
4. Answer questions one at a time (can edit/review anytime)
5. Get feedback summary with key insights
6. Download feedback to local session folder

### 8 Dimensions

1. Problem Definition
2. User Understanding
3. Solution Rationale
4. Success Metrics
5. Technical Feasibility
6. Assumptions & Risks
7. Stakeholder Alignment
8. Scope & Trade-offs

## Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code)
- Python 3.8+

### Installation

```bash
git clone https://github.com/abhitsian/pm-spec-analyzer.git
cd pm-spec-analyzer
pip install streamlit python-docx
streamlit run app_simplified.py
```

Or use the installer:
```bash
./install.sh && ./run.sh
```

## How to Use

1. **Upload spec** (.txt, .md, .docx) - filename auto-fills as title
2. **Initial analysis** - scored across 8 dimensions
3. **Select stage** - Early Draft, Developing, or Final Review
4. **Answer questions** - one at a time, Socratic method
5. **Review/edit** - see all answers, edit any before submitting
6. **Get feedback** - key insights and remaining gaps
7. **Download** - feedback saved to session folder

Sessions auto-save to `~/.pm_spec_analyzer/sessions/[timestamp]_[id]_[title]/`

Each session folder contains:
- `session.json` - Full session data
- `original_spec.md` - Your uploaded spec
- `transcript.md` - Complete Q&A transcript
- Downloaded feedback file

## File Support

- `.txt` - Plain text
- `.md` - Markdown
- `.docx` - Word documents

## Methodology

### Based on AskUserQuestion

Claude Code includes a tool called `AskUserQuestion` that clarifies ambiguous requirements through Socratic questioning:
- Asks one non-obvious question at a time
- Goes progressively deeper based on responses
- Continues until ambiguities are resolved

This tool applies the same pattern to PM spec review.

### Key Differences from Traditional Feedback

**Traditional:** "Your spec needs success metrics"
**Socratic:** "How will you know if this actually solves the problem?"

Questions force thinking. Feedback identifies gaps.

### Adaptations for PM Specs

- **8-dimension framework** - Problem, User, Solution, Metrics, Technical, Risks, Stakeholders, Scope
- **Initial analysis** - Score spec to identify gaps
- **Stage awareness** - Questions adapt to Early Draft / Developing / Final Review
- **Spec generation** - Creates improved version from interview insights
- **Session storage** - Saves for review

See [METHODOLOGY.md](METHODOLOGY.md) for detailed comparison with AskUserQuestion.

## Technical Details

- Uses Claude Code CLI via subprocess
- No API keys needed
- Runs locally
- Streamlit UI

## Requirements

```
streamlit>=1.28.0
python-docx>=1.0.0
```

## License

MIT
