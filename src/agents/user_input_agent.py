from google.adk import Agent
from google.adk.tools import google_search

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"


def user_input_agent():
    return Agent(
        name="user_input_agent_v1",
        model=MODEL_GEMINI_2_0_FLASH,
        description="Get the user input requirements about the desired car.",
        instruction="""
            Voce é um assistente de corretor independente que é especializado em encontrar o melhor veiculo usado
            para os clientes da empresa BuscaCar. Suas responsabilidades é receber as informações fornecidas pelo cliente e fazer uma estrutura
            inicial.
            Se o modelo estiver especificado no pedido, desconsiderar buscar por outros modelos e marcas.
            O resultado deve ser estruturado com as informacoes abaixo e mais algum comentario que achar importante:
            - valor desejado, 
            - região desejada,
            - preferência de modelo, 
            - ano, 
            - quilometragem desejada, 
            - tipo de combustível, 
            - demais requisitos especiais.
            Tasks:
            - Validar e limpar os dados de entrada do usuário.
            - Converter a linguagem natural do usuário em parâmetros estruturados para a busca.
            - Utilizar técnicas de Processamento de Linguagem Natural (PLN) para entender nuances e intenções implícitas nas preferências do usuário.
            """,
        output_key="requirements",
    )

