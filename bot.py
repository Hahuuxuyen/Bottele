import os
import telebot
from datetime import datetime

# Lấy token từ Environment, fallback nếu Render lỗi
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    BOT_TOKEN = "8340836312:AAHC87iQUxbONjja4TlMYNLdMlW5HJQ05hU"

bot = telebot.TeleBot(BOT_TOKEN)

# Lưu tiền theo user
user_money = {}

def time_now():
    return datetime.now().strftime("%H:%M:%S | %d/%m/%Y")

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(
        msg,
        "🤖 BOT GHI LỜI / LỖ\n\n"
        "📌 Lệnh sử dụng:\n"
        "/win <tiền> ➜ thắng\n"
        "/thua <tiền> ➜ thua\n"
        "/tong ➜ xem tổng\n\n"
        "VD: /win 50000"
    )

@bot.message_handler(commands=['win'])
def win(msg):
    try:
        amount = int(msg.text.split()[1])
        uid = msg.from_user.id
        user_money[uid] = user_money.get(uid, 0) + amount

        bot.reply_to(
            msg,
            f"✅ THẮNG +{amount:,}đ\n"
            f"💰 TỔNG: {user_money[uid]:,}đ\n"
            f"🕒 {time_now()}"
        )
    except:
        bot.reply_to(msg, "❌ Sai cú pháp\nVD: /win 50000")

@bot.message_handler(commands=['thua'])
def thua(msg):
    try:
        amount = int(msg.text.split()[1])
        uid = msg.from_user.id
        user_money[uid] = user_money.get(uid, 0) - amount

        bot.reply_to(
            msg,
            f"❌ THUA -{amount:,}đ\n"
            f"💰 TỔNG: {user_money[uid]:,}đ\n"
            f"🕒 {time_now()}"
        )
    except:
        bot.reply_to(msg, "❌ Sai cú pháp\nVD: /thua 30000")

@bot.message_handler(commands=['tong'])
def tong(msg):
    uid = msg.from_user.id
    total = user_money.get(uid, 0)

    bot.reply_to(
        msg,
        f"📊 TỔNG HIỆN TẠI: {total:,}đ\n"
        f"🕒 {time_now()}"
    )

print("🤖 Bot đang chạy 24/24...")
bot.infinity_polling()
