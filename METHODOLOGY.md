# Methodology

## Based on Claude Code's AskUserQuestion

This tool applies the same pattern as Claude Code's `AskUserQuestion` tool.

### What is AskUserQuestion?

Claude Code includes a tool called `AskUserQuestion` for clarifying ambiguous requirements:

```
Description: Ask questions to clarify requirements
- Ask non-obvious questions only
- One question at a time
- Go deep based on responses
- Continue until ambiguities resolved
```

**Pattern:**
1. Identify ambiguity
2. Ask one targeted question
3. Listen to response
4. Either ask follow-up or move to next topic
5. Summarize when clear

### Applied to PM Specs

Same pattern, different domain:

**AskUserQuestion** → Clarifies code requirements
**PM Spec Analyzer** → Clarifies spec quality

**Core pattern (unchanged):**
- One question at a time
- Non-obvious questions only
- Progressive depth
- Know when complete

**Domain adaptations:**
- 8-dimension framework (Problem, User, Solution, Metrics, Technical, Risks, Stakeholders, Scope)
- Stage awareness (Early Draft / Developing / Final Review)
- Initial analysis (score each dimension)
- Spec generation (create improved version from insights)
- Session storage (save for review)

## Why Socratic Method

**Traditional feedback:**
"Your spec needs success metrics"

**Socratic questioning:**
"How will you know if this actually solves the problem?"

The question forces thinking. The feedback just identifies a gap.

## The Question Cycle

```
1. Analyze spec → Identify highest priority gap
2. Consider stage → Adjust question difficulty
3. Ask one question → Target specific gap
4. Listen to response → Evaluate understanding
5. Decide next:
   - Follow-up (go deeper on same topic)
   - New question (move to different dimension)
   - Complete (all dimensions covered)
6. Generate improved spec
```

Same cycle AskUserQuestion uses, specialized for PM specs.

## Example Comparison

### AskUserQuestion (General)
```
User: "I need a sync feature"
Claude: "What specifically needs to sync?"
User: "User data across instances"
Claude: "What happens when the same data changes in multiple places?"
User: "I hadn't thought about that"
Claude: "What should happen in that case?"
[continues until requirements clear]
```

### PM Spec Analyzer (Specialized)
```
PM: [uploads spec about sync feature]
Analyzer: [scores 8 dimensions]
         Problem Definition: 2/5
         Solution Rationale: 1/5
PM: [selects "Developing" stage]
Analyzer: "What's the root cause - concurrent writes, network latency, or something else?"
PM: "Concurrent writes causing conflicts"
Analyzer: "What alternatives did you evaluate for handling concurrent writes?"
PM: "Last-write-wins, manual resolution, CRDTs"
Analyzer: "For CRDTs, how will you measure if it actually solves the problem?"
[continues across 8 dimensions until complete]
[generates improved spec incorporating insights]
```

Same questioning approach, applied to spec review.

## Technical Implementation

Uses Claude Code CLI:
```python
result = subprocess.run(
    [CLAUDE_CLI, '--print', prompt],
    capture_output=True,
    text=True
)
```

Prompt includes:
- Current spec
- Conversation history
- Stage context (Early/Developing/Final)
- 8 dimensions to cover
- Instruction: "Ask ONE non-obvious question"

Response format:
```json
{
    "question": "...",
    "topic": "Problem Definition",
    "why_asking": "...",
    "done": false
}
```

When `done: true`, provides summary and generates improved spec.

## Lifecycle Stages

Questions adapt to stage:

**Early Draft:**
- Focus: Problem clarity, user understanding
- Style: Exploratory, foundational
- Example: "What problem are you actually solving?"

**Developing:**
- Focus: Solution rationale, metrics, technical approach
- Style: Direct, challenging gaps
- Example: "What alternatives did you consider and why did you reject them?"

**Final Review:**
- Focus: Edge cases, risks, unvalidated assumptions
- Style: Rigorous, detail-oriented
- Example: "What could cause this to fail in production?"

Same questioning method, different depth expectations.

## Why This Works

AskUserQuestion is effective because:
- Forces clarification through questions
- Reveals unstated assumptions
- Builds understanding progressively
- Develops requirement definition skills

This tool applies the same principles to spec review:
- Forces PM to think through each dimension
- Reveals gaps in reasoning
- Builds spec quality progressively
- Develops spec writing skills

Both teach thinking, not just identify problems.
