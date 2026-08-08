class OracleTools:

    @staticmethod
    def generate_sql(request):

        prompt = f"""
Generate ONLY Oracle SQL.

User Request:
{request}

Rules:
- Return only Oracle SQL.
- Use Oracle SQL syntax.
- No explanation.
- No markdown.
"""

        return prompt