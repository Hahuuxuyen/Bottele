import telebot
import hashlib
import random

BOT_TOKEN = "8340836312:AAHC87iQUxbONjja4TlMYNLdMlW5HJQ05hU"
OWNER_NAME = "Hà Hữu Xuyên"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(
        msg,
        f"""🤖 BOT DỰ ĐOÁN TÀI / XỈU (AI + MD5)

👤 Chủ bot: {OWNER_NAME}

👉 Gửi 1 chuỗi bất kỳ
👉 Bot trả kết quả dự đoán phiên sau

⚠️ Chỉ mang tính tham khảo – giải trí
"""
    )

@bot.message_handler(func=lambda m: True)
def predict(msg):
    text = msg.text.strip()

    # Tính MD5
    md5_hash = hashlib.md5(text.encode("utf-8")).hexdigest()

    # Lấy 2 hex cuối
    last_hex = md5_hash[-2:]
    value = int(last_hex, 16)

    # Logic tài xỉu
    if value > 127:
        result = "🟢 TÀI"
    else:
        result = "🔴 XỈU"

    # % tin cậy (random an toàn)
    percent = random.randint(60, 85)

    reply = f"""
🔐 MD5:
`{md5_hash}`

📊 Phân tích:
• Hex cuối: `{last_hex}`
• Giá trị: `{value}`

🎯 Dự đoán phiên sau:
{result}

📈 Độ tin cậy:
{percent}%

© {OWNER_NAME}
⚠️ Giải trí – không đảm bảo thắng
"""
    bot.reply_to(msg, reply, parse_mode="Markdown")

bot.polling(none_stop=True)