import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("8340836312:AAHC87iQUxbONjja4TlMYNLdMlW5HJQ05hU")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN chưa được set trong Environment Variables")

bot = telebot.TeleBot(BOT_TOKEN)

# Lưu tiền theo user
user_money = {}

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(
        msg,
        "🤖 Bot quản lý lời/lỗ\n\n"
        "📌 Lệnh dùng:\n"
        "/win <số tiền> ➜ thắng\n"
        "/thua <số tiền> ➜ thua\n"
        "/tong ➜ xem tổng\n\n"
        "VD: /win 50000"
    )

@bot.message_handler(commands=['win'])
def win(msg):
    try:
        amount = int(msg.text.split()[1])
        uid = msg.from_user.id
        user_money[uid] = user_money.get(uid, 0) + amount
        bot.reply_to(msg, f"✅ Thắng +{amount:,}đ\n💰 Tổng: {user_money[uid]:,}đ")
    except:
        bot.reply_to(msg, "❌ Sai cú pháp\nVD: /win 50000")

@bot.message_handler(commands=['thua'])
def thua(msg):
    try:
        amount = int(msg.text.split()[1])
        uid = msg.from_user.id
        user_money[uid] = user_money.get(uid, 0) - amount
        bot.reply_to(msg, f"❌ Thua -{amount:,}đ\n💰 Tổng: {user_money[uid]:,}đ")
    except:
        bot.reply_to(msg, "❌ Sai cú pháp\nVD: /thua 30000")

@bot.message_handler(commands=['tong'])
def tong(msg):
    uid = msg.from_user.id
    total = user_money.get(uid, 0)
    bot.reply_to(msg, f"📊 Tổng hiện tại: {total:,}đ")

print("🤖 Bot đang chạy...")
bot.infinity_polling()
