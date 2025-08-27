# Importa a biblioteca necessária (você precisaria instalá-la primeiro)
# pip install google-generativeai
import google.generativeai as genai

# --- CONFIGURAÇÃO (PASSO OBRIGATÓRIO) ---
# Você obteria uma chave de API se registrando em um serviço como o Google AI Studio
API_KEY = "AIzaSyAISyUl2DUvCFXbV3EzJLBWWwqZGryj-78"
genai.configure(api_key=API_KEY)

# Escolha o modelo que você quer usar (ex: 'gemini-pro')
model = genai.GenerativeModel('gemini-2.5-flash-lite')

print("Chatbot de IA: Olá, eu sou um chatbot inteligente. Pode perguntar o que quiser!")
print("Digite 'sair' para encerrar a conversa.")

while True:
    entrada_usuario = input("Você: ")
    
    if entrada_usuario.lower() == 'sair':
        print("Chatbot de IA: Até mais! Foi um prazer.")
        break
    
    try:
        # Envia a mensagem do usuário para o modelo de IA e obtém a resposta
        # Este é o passo que conecta seu código com a inteligência artificial!
        response = model.generate_content(entrada_usuario)
        
        # Exibe o texto gerado pelo modelo
        print(f"Chatbot de IA: {response.text}")
        
    except Exception as e:
        # Caso ocorra algum erro (falha na internet, chave de API inválida, etc.)
        print(f"Chatbot de IA: Desculpe, algo deu errado. Erro: {e}")