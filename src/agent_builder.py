from src.config import get_llm
from src.tools import load_data
from src.agent_core import run_agent

def build_agent(excel_file_path):

    llm = get_llm()
    df = load_data(excel_file_path)

    def agent_interface(user_input,role):
        return run_agent(llm, df, user_input,role)

    return agent_interface
