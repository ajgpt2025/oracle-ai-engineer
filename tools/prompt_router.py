from prompts.sql_prompt import SQL_PROMPT
from prompts.plsql_prompt import PLSQL_PROMPT
from prompts.apex_prompt import APEX_PROMPT
from prompts.ebs_prompt import EBS_PROMPT
from prompts.bip_prompt import BIP_PROMPT


def get_prompt(code_type):

    prompts = {
        "Oracle SQL": SQL_PROMPT,
        "PL/SQL": PLSQL_PROMPT,
        "Oracle APEX": APEX_PROMPT,
        "Oracle EBS": EBS_PROMPT,
        "BI Publisher": BIP_PROMPT,
    }

    return prompts.get(code_type, SQL_PROMPT)