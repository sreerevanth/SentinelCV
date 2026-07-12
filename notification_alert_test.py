import requests

BOT_TOKEN = "8205081054:AAFSeIgntU8TfW8jl03WsbZ_HhTh3kGY93o"
CHAT_ID = "7135291777"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "🔥 BRO ITS WORKING"}
)