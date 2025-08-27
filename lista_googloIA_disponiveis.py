import google.generativeai as genai

# Substitua pela sua chave de API
genai.configure(api_key="AIzaSyAISyUl2DUvCFXbV3EzJLBWWwqZGryj-78")

# Liste todos os modelos disponíveis para sua conta
for m in genai.list_models():
    # Apenas para facilitar a leitura, mostra os modelos de texto
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)