import telebot
import hashlib
import random
import time

BOT_TOKEN = "8340836312:AAHC87iQUxbONjja4TlMYNLdMlW5HJQ05hU"
OWNER_NAME = "Hà Hữu Xuyên"

bot = telebot.TeleBot(BOT_TOKEN)

# ===== START =====
@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(
        msg,
        f"""🤖 BOT DỰ ĐOÁN TÀI / XỈU (MD5 + AI)

👤 Chủ bot: {OWNER_NAME}

📌 Cách dùng:
• Gửi 1 chuỗi bất kỳ
• Bot trả MD5 + dự đoán

⚠️ Chỉ mang tính giải trí
"""
    )

# ===== PREDICT =====
@bot.message_handler(func=lambda m: True)
def predict(msg):
    text = msg.text.strip()

    # MD5
    md5_hash = hashlib.md5(text.encode("utf-8")).hexdigest()

    # Lấy 4 hex cuối để tránh lệch
    h1 = int(md5_hash[-4:-2], 16)
    h2 = int(md5_hash[-2:], 16)
    total = h1 + h2  # 0 – 510

    # Cân tài/xỉu bằng chẵn lẻ
    if total % 2 == 0:
        result = "🔴 XỈU"
    else:
        result = "🟢 TÀI"

    # % tin cậy (dựa độ chênh)
    diff = abs(h1 - h2)
    percent = min(85, 55 + diff // 4)

    reply = f"""
🔐 MD5:
`{md5_hash}`

📊 Phân tích:
• Hex 1: {h1}
• Hex 2: {h2}
• Tổng: {total}

🎯 Dự đoán phiên sau:
{result}

📈 Độ tin cậy:
{percent}%

© {OWNER_NAME}
⚠️ Giải trí – không đảm bảo thắng
"""
    bot.reply_to(msg, reply, parse_mode="Markdown")

# ===== RUN =====
print("BOT ĐANG CHẠY...")
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print("LỖI:", e)
        time.sleep(5)