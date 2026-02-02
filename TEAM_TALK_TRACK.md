# PM Spec Analyzer - Team Share

Hey team,

Built something that might help with spec writing. Wanted to share and see what you think.

## What It Is

A tool that asks you questions about your spec - one at a time, Socratic style. Like having someone challenge your thinking, but without the 3-day review cycle.

Upload spec → Answer 5-8 questions → Get feedback → Incorporate and iterate.

## Why I Built It

We've all had specs bounce back multiple times. "What's the actual user pain?" "Why this approach?" "What about metrics?"

This just asks those questions upfront. Faster feedback loop.

Also - we all have Claude Code already. It's there for everyone to use. But it's built for code. This is about building PM-specific tools on top of it. Same backend, purpose-built for our workflow.

## How It Works

1. Upload your spec (txt, md, or docx)
2. Pick your stage: Early Draft / Developing / Final Review
3. Answer questions - it goes deep based on your answers
4. Review/edit your answers before submitting
5. Get feedback summary
6. Download everything to a local folder

Sessions save automatically. You can review past Q&As anytime.

**Behind the scenes:** Uses Claude Code's [AskUserQuestion pattern](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - the same Socratic questioning approach Claude uses to clarify code requirements, but applied to PM specs instead.

## Try It Out

**Install (3 commands):**
```bash
git clone https://github.com/abhitsian/pm-spec-analyzer.git
cd pm-spec-analyzer
pip install streamlit python-docx && streamlit run app_simplified.py
```

Opens at localhost:8501

**Or just try with your next spec:**
- Grab one you're working on
- Run through it
- See if the questions help

## What I'm Curious About

- Does it ask the right questions?
- Are the questions at the right depth for each stage?
- Is 5-8 questions too many/few?
- Would you actually use this vs just asking a colleague?

No pressure to use it. Just want to see if it's useful or just noise.

Let me know what you think.

— Abhishek

P.S. It runs locally, uses Claude Code (which we already have), no API keys needed.
