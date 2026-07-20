import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 JetX Analyzer est en ligne !\n\n"
        "Commande :\n"
        "/stats - voir les statistiques"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Analyse statistique :\n"
        "- Bot connecté ✅\n"
        "- Analyse en préparation ⏳"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))

    app.run_polling()

if __name__ == "__main__":
    main()
