from google.adk import Agent
from google.adk.tools import google_search

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"


def reviewer_agent():
    return Agent(
        name="review_agent_v1",
        model=MODEL_GEMINI_2_0_FLASH,
        description="Revisa a o resultado da busca",
        instruction="""
        Voce é um vendedor que atende ao publico, interface final com os clientes do BuscaCar.
        Voce vai revisar os resultados da busca no state de key ['research_results'], e formatar os resultados para o cliente em formato markdown, destacando
        as principais descobertas na pesquisa.
        """,
        output_key="final_results",
    )

