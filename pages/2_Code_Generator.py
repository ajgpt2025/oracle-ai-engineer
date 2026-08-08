import streamlit as st
from agents.oracle_agent import OracleAgent
st.title("🛠 Oracle Code Generator")
if "agent" not in st.session_state:
    st.session_state.agent = OracleAgent()
st.write("Generate Oracle SQL, PL/SQL, APEX, EBS and more.")

code_type = st.selectbox(
    "Choose Code Type",
    [
        "Oracle SQL",
        "PL/SQL",
        "Procedure",
        "Function",
        "Package",
        "Trigger",
        "View",
        "MERGE Statement",
        "Dynamic SQL",
        "Oracle APEX",
        "Oracle EBS",
        "BI Publisher"
    ]
)

st.write(f"You selected: **{code_type}**")

request = st.text_area(
    "Describe what you want to generate",
    height=180
)

if st.button("Generate"):

    if request.strip():

        prompt = f"""
You are an expert Oracle developer.

Generate {code_type}.

User Request:
{request}

Requirements:
- Return only the requested Oracle code.
- No markdown.
- No explanation.
- Use Oracle best practices.
"""

        answer = st.session_state.agent.ask(prompt)

        st.subheader("Generated Code")

        st.code(answer)