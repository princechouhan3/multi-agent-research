import streamlit as st
from agents.researcher import run_research_agent
from agents.summarize import run_summarize_agent
from agents.writer import run_writer_agent

st.set_page_config(page_title="AI Report Generator", layout="centered")

st.title("🧠 Multi-Agent Report Generator")
st.markdown("This app uses AI agents to research, summarize, and write reports on any topic.")

topic = st.text_input("Enter your research topic:", placeholder="e.g., AI in Climate Change")

if st.button("Generate Report") and topic:
    with st.spinner("🔍 Researching..."):
        research_content = run_research_agent(topic)
    st.success("✅ Research Complete")

    with st.spinner("📝 Summarizing..."):
        summary = run_summarize_agent(research_content)
    st.success("✅ Summarization Complete")

    with st.spinner("📄 Writing Report..."):
        report = run_writer_agent(topic, summary)
    st.success("✅ Report Generated")

    st.markdown("### 📘 Final Report")
    st.text_area(label="", value=report, height=400)
