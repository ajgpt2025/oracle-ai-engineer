from ollama import chat
from prompts.oracle_prompt import SYSTEM_PROMPT
from tools.oracle_tools import OracleTools


class OracleAgent:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def ask(self, question):

        # Detect SQL requests
        if question.lower().startswith("sql:"):

            sql_prompt = OracleTools.generate_sql(
                question.replace("sql:", "").strip()
            )

            response = chat(
                model="qwen:latest",
                messages=[
                    {
                        "role": "system",
                        "content": sql_prompt
                    }
                ]
            )

            return response["message"]["content"]

        # Normal chat
        self.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        response = chat(
            model="qwen:latest",
            messages=self.messages
        )

        answer = response["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer