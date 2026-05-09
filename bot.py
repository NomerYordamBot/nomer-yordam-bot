import telebot
import pandas as pd

TOKEN = "8731025825:AAH_4Wa_O-OM8PBLfpTEb7VXgAhIjMw2wZ0"

SHEET_ID = "1f6WqnXizDjbWkaT_nn2IAhkrnjjIy8mG"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

bot = telebot.TeleBot(TOKEN)

def load_data():
    df = pd.read_csv(URL)
    df = df.fillna("")
    return df

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Ism yozing, telefon chiqadi.")

@bot.message_handler(func=lambda message: True)
def search(message):
    text = message.text.lower()
    df = load_data()

    for _, row in df.iterrows():
        ism = str(row.iloc[0]).lower()
        telefon = str(row.iloc[1])

        if text in ism:
            bot.reply_to(message, f"📞 {row.iloc[0]}:\n{telefon}")
            return

    bot.reply_to(message, "❌ Topilmadi")

print("Bot ishga tushdi...")
bot.infinity_polling()