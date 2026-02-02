import streamlit as st
import subprocess
import json
from datetime import datetime
import os
from pathlib import Path
import tempfile

# Page config
st.set_page_config(
    page_title="PM Spec Analyzer",
    page_icon="📋",
    layout="wide"
)

# Find Claude Code CLI
def find_claude_cli():
    """Find Claude Code CLI in common locations"""
    claude_paths = [
        Path.home() / ".local/bin/claude",
        Path("/usr/local/bin/claude"),
        Path("/opt/homebrew/bin/claude"),
        Path("/usr/bin/claude"),
    ]

    for path in claude_paths:
        if path.exists() and path.is_file():
            return str(path)

    # Try which command as fallback
    try:
        result = subprocess.run(['which', 'claude'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass

    return None

CLAUDE_CLI = find_claude_cli()

if not CLAUDE_CLI:
    st.error("❌ Claude Code CLI not found! Please install Claude Code first: https://claude.com/claude-code")
    st.stop()

# Evaluation dimensions
EVALUATION_DIMENSIONS = {
    "Problem Definition": {
        "description": "Clarity on WHAT problem is being solved and WHY it matters",
        "criteria": [
            "Clear problem statement exists",
            "Root cause identified (not just symptoms)",
            "User pain quantified with evidence",
            "Impact of doing nothing is stated",
            "Problem validated with customer research"
        ]
    },
    "User Understanding": {
        "description": "Deep understanding of WHO has this problem",
        "criteria": [
            "Target user persona clearly defined",
            "User jobs-to-be-done articulated",
            "User context and constraints understood",
            "Edge cases and power users considered",
            "Accessibility needs addressed"
        ]
    },
    "Solution Rationale": {
        "description": "WHY this solution vs alternatives",
        "criteria": [
            "Multiple alternatives were considered",
            "Trade-offs explicitly documented",
            "Rationale for chosen approach is clear",
            "Simplest viable solution identified",
            "Build vs buy vs partner evaluated"
        ]
    },
    "Success Metrics": {
        "description": "HOW we'll know if this succeeds",
        "criteria": [
            "Clear success metrics defined",
            "Metrics tied to business outcomes",
            "Baseline and target values stated",
            "Leading and lagging indicators identified",
            "Measurement plan exists"
        ]
    },
    "Technical Feasibility": {
        "description": "Engineering complexity and constraints",
        "criteria": [
            "Technical approach outlined",
            "Dependencies and integrations identified",
            "Performance/scale considerations addressed",
            "Security and compliance reviewed",
            "Technical risks documented"
        ]
    },
    "Assumptions & Risks": {
        "description": "What could go wrong and what we're assuming",
        "criteria": [
            "Key assumptions explicitly listed",
            "Assumptions marked as validated or unvalidated",
            "Risk mitigation strategies defined",
            "Rollback plan exists",
            "Impact of failure considered"
        ]
    },
    "Stakeholder Alignment": {
        "description": "Who needs to be involved and their concerns",
        "criteria": [
            "All stakeholders identified",
            "Stakeholder concerns addressed",
            "Cross-functional dependencies mapped",
            "Communication plan exists",
            "Decision-making process clear"
        ]
    },
    "Scope & Trade-offs": {
        "description": "What's in, what's out, and why",
        "criteria": [
            "MVP clearly defined",
            "Out-of-scope items listed explicitly",
            "Phasing strategy explained",
            "What we're NOT building is clear",
            "Resource/timeline trade-offs acknowledged"
        ]
    }
}

def call_claude_code(prompt_text):
    """Call Claude Code CLI with a prompt and return the response"""

    # Create temporary file for prompt
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(prompt_text)
        prompt_file = f.name

    try:
        # Call Claude Code CLI
        result = subprocess.run(
            [CLAUDE_CLI, '--prompt', prompt_file],
            capture_output=True,
            text=True,
            timeout=180
        )

        if result.returncode != 0:
            raise Exception(f"Claude Code error: {result.stderr}")

        return result.stdout

    finally:
        # Clean up temp file
        try:
            os.unlink(prompt_file)
        except:
            pass

def analyze_spec(spec_text, pm_name, spec_title):
    """Send spec to Claude Code for comprehensive analysis"""

    dimensions_text = "\n\n".join([
        f"**{dim}**: {info['description']}\nCriteria:\n" +
        "\n".join([f"- {c}" for c in info['criteria']])
        for dim, info in EVALUATION_DIMENSIONS.items()
    ])

    prompt = f"""You are a senior product management coach helping junior PMs improve their specs through Socratic questioning.

Analyze this product specification across these dimensions:

{dimensions_text}

For each dimension:
1. Score it from 1-5 (1=missing, 3=adequate, 5=excellent)
2. Identify what's present and what's missing
3. Ask 2-3 probing Socratic questions that make the PM think deeper
4. DO NOT provide answers or write content for them

Spec Title: {spec_title}
PM Name: {pm_name}

SPEC CONTENT:
{spec_text}

Respond in this JSON format:
{{
    "overall_score": <number 1-5>,
    "overall_summary": "<2-3 sentence assessment>",
    "dimensions": {{
        "Problem Definition": {{
            "score": <number>,
            "strengths": ["<specific things done well>"],
            "gaps": ["<specific things missing>"],
            "socratic_questions": [
                "<question that makes them think deeper>",
                "<question that challenges assumptions>"
            ]
        }},
        ... (repeat for each dimension)
    }},
    "critical_missing_elements": ["<top 3-5 things that MUST be addressed>"],
    "ready_for_stakeholder_review": <true/false>,
    "next_steps": ["<specific action items for the PM>"]
}}

Be thorough, specific, and challenging. Reference specific parts of the spec in your feedback."""

    response = call_claude_code(prompt)

    # Extract JSON from response
    try:
        # Try to find JSON in the output
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start != -1 and json_end > json_start:
            json_str = response[json_start:json_end]
            return json.loads(json_str)
        else:
            # If no JSON found, return raw response
            return {
                "overall_score": 3.0,
                "overall_summary": "Analysis completed. See detailed feedback below.",
                "raw_output": response,
                "dimensions": {}
            }
    except Exception as e:
        return {
            "overall_score": 3.0,
            "overall_summary": f"Analysis completed with parsing issues: {str(e)}",
            "raw_output": response,
            "dimensions": {}
        }

def improve_section(spec_text, dimension, feedback, pm_responses):
    """Help PM improve a specific section through dialogue"""

    prompt = f"""You are a senior PM coach helping a junior PM improve their spec.

CONTEXT:
The PM is working on the "{dimension}" section of their spec.

ORIGINAL SPEC EXCERPT:
{spec_text[:2000]}

FEEDBACK GIVEN:
Score: {feedback.get('score', 0)}/5
Gaps: {', '.join(feedback.get('gaps', []))}

QUESTIONS YOU ASKED:
{chr(10).join([f"Q: {q}" for q in feedback.get('socratic_questions', [])])}

PM's RESPONSES:
{pm_responses}

Based on the PM's responses, ask 2-3 FOLLOW-UP questions that:
1. Push them to be more specific
2. Challenge any weak assumptions
3. Force them to think about edge cases or implications

DO NOT write content for them. Only ask questions that develop their thinking.

If their responses are strong and show good reasoning, acknowledge it and ask them to now draft improved content based on their answers.

Respond in JSON format:
{{
    "assessment": "<brief assessment of their responses>",
    "follow_up_questions": ["<question 1>", "<question 2>"],
    "ready_to_draft": <true/false>,
    "guidance_if_ready": "<high-level guidance for what to include, not the actual content>"
}}"""

    response = call_claude_code(prompt)

    try:
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start != -1 and json_end > json_start:
            json_str = response[json_start:json_end]
            return json.loads(json_str)
    except:
        pass

    # Fallback response
    return {
        "assessment": response[:500],
        "follow_up_questions": ["What specific evidence supports your thinking?", "What could prove this wrong?"],
        "ready_to_draft": False,
        "guidance_if_ready": ""
    }

# Session state initialization
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'improvement_mode' not in st.session_state:
    st.session_state.improvement_mode = None
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = {}

# Main UI
st.title("📋 PM Spec Analyzer & Co-Creation Tool")
st.markdown("Upload your spec for comprehensive evaluation and Socratic coaching to improve your thinking.")

# Sidebar
with st.sidebar:
    st.header("About This Tool")
    st.markdown("""
    This tool evaluates your product specs across 8 critical dimensions:

    - **Problem Definition**
    - **User Understanding**
    - **Solution Rationale**
    - **Success Metrics**
    - **Technical Feasibility**
    - **Assumptions & Risks**
    - **Stakeholder Alignment**
    - **Scope & Trade-offs**

    It won't write your spec for you - it asks questions that make you think deeper.
    """)

    st.divider()
    st.markdown(f"**✅ Claude Code**: Found at `{CLAUDE_CLI}`")
    st.markdown("**💡 Tip**: Be thorough in your responses. The tool can tell when you're being superficial.")

# Main content area
tab1, tab2 = st.tabs(["📤 Upload & Analyze", "🔄 Improve Spec"])

with tab1:
    st.header("Upload Your Spec")

    col1, col2 = st.columns([2, 1])

    with col1:
        pm_name = st.text_input("Your Name", placeholder="e.g., Sarah Chen")
        spec_title = st.text_input("Spec Title", placeholder="e.g., Multi-Instance Data Sync Feature")

    spec_input_method = st.radio("Input Method", ["Paste Text", "Upload File"], horizontal=True)

    if spec_input_method == "Paste Text":
        spec_text = st.text_area(
            "Paste Your Spec Here",
            height=400,
            placeholder="Paste your full product spec here..."
        )
    else:
        uploaded_file = st.file_uploader("Upload Spec Document", type=['txt', 'md'])
        spec_text = ""
        if uploaded_file:
            spec_text = uploaded_file.read().decode()
            st.text_area("Spec Preview", spec_text, height=400, disabled=True)

    if st.button("🔍 Analyze Spec", type="primary", disabled=not (pm_name and spec_title and spec_text)):
        with st.spinner("Analyzing your spec with Claude Code... This may take 30-90 seconds."):
            try:
                result = analyze_spec(spec_text, pm_name, spec_title)
                st.session_state.analysis_result = result
                st.session_state.spec_text = spec_text
                st.session_state.pm_name = pm_name
                st.session_state.spec_title = spec_title
                st.success("✅ Analysis complete! Check results below.")
                st.rerun()
            except Exception as e:
                st.error(f"Error analyzing spec: {str(e)}")

    # Display results
    if st.session_state.analysis_result:
        st.divider()
        result = st.session_state.analysis_result

        # Overall score
        st.header("📊 Overall Assessment")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            score = result.get('overall_score', 0)
            score_color = "🔴" if score < 2.5 else "🟡" if score < 4 else "🟢"
            st.metric("Overall Score", f"{score:.1f} / 5.0", delta=score_color)

        with col2:
            st.markdown(f"**Summary**: {result.get('overall_summary', 'No summary available')}")

        with col3:
            if result.get('ready_for_stakeholder_review'):
                st.success("✅ Ready for review")
            else:
                st.warning("⚠️ Needs work")

        # Critical missing elements
        if result.get('critical_missing_elements'):
            st.error("**❗ Critical Missing Elements**")
            for item in result['critical_missing_elements']:
                st.markdown(f"- {item}")

        st.divider()

        # Dimension breakdown
        st.header("📋 Dimension-by-Dimension Analysis")

        dimensions = result.get('dimensions', {})

        if dimensions:
            for dim_name, dim_info in EVALUATION_DIMENSIONS.items():
                if dim_name in dimensions:
                    dim_result = dimensions[dim_name]

                    with st.expander(f"**{dim_name}** - Score: {dim_result.get('score', 0)}/5",
                                   expanded=dim_result.get('score', 5) < 3):
                        st.markdown(f"*{dim_info['description']}*")

                        col1, col2 = st.columns(2)

                        with col1:
                            if dim_result.get('strengths'):
                                st.markdown("**✅ Strengths:**")
                                for strength in dim_result['strengths']:
                                    st.markdown(f"- {strength}")

                        with col2:
                            if dim_result.get('gaps'):
                                st.markdown("**❌ Gaps:**")
                                for gap in dim_result['gaps']:
                                    st.markdown(f"- {gap}")

                        st.markdown("**🤔 Questions for You to Consider:**")
                        for i, question in enumerate(dim_result.get('socratic_questions', []), 1):
                            st.markdown(f"{i}. {question}")

                        # Quick improve button
                        if st.button(f"💬 Work on improving '{dim_name}'", key=f"improve_{dim_name}"):
                            st.session_state.improvement_mode = dim_name
                            st.rerun()
        else:
            # Show raw output if structured data not available
            st.markdown("**Analysis Output:**")
            st.text(result.get('raw_output', 'No output available'))

        # Next steps
        if result.get('next_steps'):
            st.divider()
            st.header("🎯 Next Steps")
            for i, step in enumerate(result['next_steps'], 1):
                st.markdown(f"{i}. {step}")

with tab2:
    st.header("🔄 Iterative Improvement")

    if not st.session_state.analysis_result:
        st.info("👈 Please analyze a spec first in the 'Upload & Analyze' tab")
    else:
        # Dimension selector
        dimensions = list(EVALUATION_DIMENSIONS.keys())

        if st.session_state.improvement_mode:
            selected_dimension = st.session_state.improvement_mode
            st.session_state.improvement_mode = None  # Reset after using
        else:
            selected_dimension = st.selectbox(
                "Select dimension to improve",
                dimensions,
                index=0
            )

        st.subheader(f"Working on: {selected_dimension}")
        st.markdown(f"*{EVALUATION_DIMENSIONS[selected_dimension]['description']}*")

        # Show the feedback
        result_dims = st.session_state.analysis_result.get('dimensions', {})
        if selected_dimension in result_dims:
            dim_result = result_dims[selected_dimension]

            st.markdown(f"**Current Score**: {dim_result.get('score', 0)}/5")

            with st.expander("📝 Review Feedback", expanded=True):
                if dim_result.get('gaps'):
                    st.markdown("**Gaps Identified:**")
                    for gap in dim_result['gaps']:
                        st.markdown(f"- {gap}")

                if dim_result.get('socratic_questions'):
                    st.markdown("**Questions to Answer:**")
                    for i, q in enumerate(dim_result['socratic_questions'], 1):
                        st.markdown(f"{i}. {q}")

            # Conversation area
            st.divider()
            st.markdown("### 💭 Your Responses")

            # Initialize conversation history for this dimension
            if selected_dimension not in st.session_state.conversation_history:
                st.session_state.conversation_history[selected_dimension] = []

            # Display conversation history
            for entry in st.session_state.conversation_history[selected_dimension]:
                if entry['type'] == 'pm':
                    st.markdown(f"**You:** {entry['content']}")
                else:
                    st.info(f"**Coach:** {entry['content']}")

            # Response input
            pm_response = st.text_area(
                "Answer the questions above (be thorough - superficial answers will be challenged)",
                height=200,
                key=f"response_{selected_dimension}"
            )

            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("Submit Response", type="primary"):
                    if pm_response:
                        with st.spinner("Coach is reviewing your response..."):
                            # Add PM response to history
                            st.session_state.conversation_history[selected_dimension].append({
                                'type': 'pm',
                                'content': pm_response
                            })

                            # Get all PM responses for this dimension
                            all_pm_responses = "\n\n".join([
                                entry['content']
                                for entry in st.session_state.conversation_history[selected_dimension]
                                if entry['type'] == 'pm'
                            ])

                            # Get coach feedback
                            try:
                                feedback_result = improve_section(
                                    st.session_state.spec_text,
                                    selected_dimension,
                                    dim_result,
                                    all_pm_responses
                                )

                                # Add coach response to history
                                coach_response = feedback_result.get('assessment', '')
                                if feedback_result.get('follow_up_questions'):
                                    coach_response += "\n\n**Follow-up questions:**\n"
                                    for q in feedback_result['follow_up_questions']:
                                        coach_response += f"- {q}\n"

                                if feedback_result.get('ready_to_draft'):
                                    coach_response += f"\n\n✅ **Good work!** You're ready to draft improved content.\n\n**Guidance:** {feedback_result.get('guidance_if_ready', '')}"

                                st.session_state.conversation_history[selected_dimension].append({
                                    'type': 'coach',
                                    'content': coach_response
                                })

                                st.rerun()
                            except Exception as e:
                                st.error(f"Error getting coach feedback: {str(e)}")
                    else:
                        st.warning("Please provide a response first")

            with col2:
                if st.button("Clear conversation for this dimension"):
                    st.session_state.conversation_history[selected_dimension] = []
                    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
Built for PM teams who want to develop stronger product thinking 💪<br>
Powered by Claude Code CLI
</div>
""", unsafe_allow_html=True)
