import asyncio
from dotenv import load_dotenv

from google.adk.agents import SequentialAgent
from google.adk.sessions import InMemorySessionService

from google.adk.runners import Runner
from google.genai import types

import warnings

from src.agents.research_agent import research_agent
from src.agents.reviewer_agent import reviewer_agent
from src.agents.user_input_agent import user_input_agent

# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

APP_NAME = "car_recomendation_app"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service = InMemorySessionService()
def runner(agent):

    session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    runner = Runner(
        agent=agent,  # The agent we want to run
        app_name=APP_NAME,  # Associates runs with our app
        session_service=session_service  # Uses our session manager
    )
    print(f"Runner created for agent '{runner.agent.name}'.")
    return runner


async def call_agent_async(query: str, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  # Prepare the user's message in ADK format
  content = types.Content(role='user', parts=[types.Part(text=query)])

  final_response_text = "" # Default

  # Key Concept: run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # You can uncomment the line below to see *all* events during execution
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      # Key Concept: is_final_response() marks the concluding message for the turn.
          if event.is_final_response():
              for part in event.content.parts:
                  if part.text is not None:
                      final_response_text += part.text
                      final_response_text += "\n"
  return final_response_text

def greetings():
    print("==="*40)
    print("Bem-vindo ao assistente de recomendação de veículos!\n")
    print("Este assistente irá ajudá-lo a encontrar o carro ideal com base em suas preferências.\n")
    print("Por favor, forneça uma descrição detalhada do tipo de veículo que você está procurando.")
    print("Exemplo: 'Procuro por um carro SUV a partir de 2019, abaixo de 80 mil km, valor de até 90 mil reais.'")
    print("Você pode incluir preferências como cor, tipo de combustível, marcas e características desejadas.\n")
    print("Vamos começar!\n")

if __name__ == '__main__':
    load_dotenv()
    greetings()
    query = input("Entre com a descricao do tipo de veiculo que voce procura: ")

    query_test = """
        Procuro por um carro SUV a partir de 2019, abaixo de 80 mil km, valor de ate 90 mil reais. 
        Preferencia por flex, branco. deve ser automatico. Considere as marcas como honda, nissan, fiat e hyundai.
        Quero um carro alto, economico e tecnologico.
        """

    # para testar voce pode inserir "query_test" no input para usar esse prompt acima,
    # senao ele vai usar o que voce inserir
    if query == "query_test":
        query = query_test

    if not query:
        print("No query provided.")
    else:
        try:
            sequencial_agent = SequentialAgent(name="fluxo_sequencial_agentes",
                                             description="Orquestra os agentes",
                                             sub_agents=[user_input_agent(),
                                                         research_agent(),
                                                         reviewer_agent()])
            runner = runner(sequencial_agent)

            response = asyncio.run(call_agent_async(query, runner, USER_ID, SESSION_ID))

            final_session = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)

            print(final_session.state['final_results'])
        except Exception as e:
            print(f"An error occurred: {e}")

