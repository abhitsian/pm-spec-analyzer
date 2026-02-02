Hey team 👋

Built a spec review tool over the weekend. Asks Socratic questions about your spec - one at a time, goes deep based on your answers.

**Quick demo:**
1. Upload spec
2. Answer 5-8 questions (Problem definition, user pain, metrics, etc.)
3. Get feedback summary
4. Download everything

Think: faster feedback loop without waiting 3 days for reviews.

We all have Claude Code already - this is about building PM-specific tools on top of it. Same backend, purpose-built for our use cases.

Uses Claude's [AskUserQuestion pattern](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) under the hood - same Socratic approach it uses for code clarification, applied to specs.

**Try it:**
```
git clone https://github.com/abhitsian/pm-spec-analyzer.git
cd pm-spec-analyzer
pip install streamlit python-docx && streamlit run app_simplified.py
```

Opens at localhost:8501. Uses Claude Code (we already have it), runs locally.

Curious what you think:
- Right questions?
- Right depth?
- Would you use it?

Try with your next spec. Let me know. 

— Abhishek
