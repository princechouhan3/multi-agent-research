from agents.researcher import run_research_agent
from agents.summarize import run_summarize_agent
from agents.writer import run_writer_agent

def main():
    print("🔍 Multi-Agent Report Generator")
    topic = input("Enter the topic: ")

    print("\n⏳ Researching...")
    research_output = run_research_agent(topic)
    print("\n✅ Research Complete.\n")

    print("📝 Summarizing research content...")
    summary_output = run_summarize_agent(research_output)
    print("\n✅ Summarization Complete.\n")

    print("📄 Generating final report...")
    report = run_writer_agent(summary_output, topic)
    print("\n✅ Report Generation Complete!\n")

    print("===== 📘 Final Report =====\n")
    print(report)

if __name__ == "__main__":
    main()
