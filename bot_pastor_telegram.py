import os
import google.generativeai as genai
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv('API_GOOGLE'))
model = genai.GenerativeModel('gemini-2.5-flash-lite')

logging.basicConfig (
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Olá! Aqui é o Pastor David. Digite /start para começarmos'
    )

async def resposta_ia (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    prompt_com_persona = f"Responda como um Pastor. Use uma linguagem simples. Somente forneça meu numero (ou telefone, contato) se, e somente se, pedirem 82 987373313. Sempre que possivel use uma mensagem curta. A pergunta é: {user_message}"
    
    print(f'Mensagem do Usuário: {user_message}')

    response = model.generate_content(prompt_com_persona)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= response.text
    )

def main():
    application = Application.builder().token(os.getenv('API_TELEGRAM')).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_ia))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()