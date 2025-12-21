import telebot, json, os

BOT_TOKEN = os.getenv("8340836312:AAHC87iQUxbONjja4TlMYNLdMlW5HJQ05hU")
bot = telebot.TeleBot(BOT_TOKEN)

DATA_FILE = "data.json"
data = {}

def save():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def bal(uid): return data.get(str(uid), 0)
def setb(uid, v):
    data[str(uid)] = v
    save()

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m,
        "💰 BOT GHI LỜI / LỖ\n"
        "/win số_tiền\n"
        "/thua số_tiền\n"
        "/balance\n"
        "/reset"
    )

@bot.message_handler(commands=["win"])
def win(m):
    try:
        a = int(m.text.split()[1])
        b = bal(m.from_user.id) + a
        setb(m.from_user.id, b)
        bot.reply_to(m, f"✅ +{a:,}₫ | Tổng: {b:,}₫")
    except:
        bot.reply_to(m, "Dùng: /win 100000")

@bot.message_handler(commands=["thua"])
def lose(m):
    try:
        a = int(m.text.split()[1])
        b = bal(m.from_user.id) - a
        setb(m.from_user.id, b)
        bot.reply_to(m, f"❌ -{a:,}₫ | Tổng: {b:,}₫")
    except:
        bot.reply_to(m, "Dùng: /thua 50000")

@bot.message_handler(commands=["balance"])
def balance(m):
    b = bal(m.from_user.id)
    st = "📈 LỜI" if b>0 else "📉 LỖ" if b<0 else "⚖️ HÒA"
    bot.reply_to(m, f"{st}\n💰 {b:,}₫")

@bot.message_handler(commands=["reset"])
def reset(m):
    setb(m.from_user.id, 0)
    bot.reply_to(m, "🔄 Reset về 0₫")

bot.infinity_polling()