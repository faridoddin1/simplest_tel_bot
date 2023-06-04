# pip install pyTelegramBotAPI
import telebot

# Replace YOUR_BOT_TOKEN with your actual bot token
BOT_TOKEN = "5928971447:AAFjTBiVHbm1SwNm7GTAmljOTIpJTHnJ_VQ"

# Create a new Telegram bot object
bot = telebot.TeleBot(BOT_TOKEN)

# Define a handler function to respond to the /start command
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.reply_to(message, "Hello!")

# Define a handler function to respond to the /help command
@bot.message_handler(commands=["help"])
def help_handler(message):
    bot.reply_to(message, "I am a simple bot that can say hello. To get started, send me the /start command.")

if __name__ == "__main__":
    # Start the bot
    bot.polling()
