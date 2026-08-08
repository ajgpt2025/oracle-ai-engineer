from agents.oracle_agent import OracleAgent

agent = OracleAgent()

print("=" * 60)
print("🤖 Oracle AI Engineer")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = agent.ask(question)

    print("\nOracle AI:\n")
    print(answer)