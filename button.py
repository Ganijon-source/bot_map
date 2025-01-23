import os
import requests
chop_etish = print

Token = "7542472244:AAF_uzh6u6yy9wVZcGJ7r-Z9rhR51byUv04"
BASE_URL = f"https://api.telegram.org/bot{Token}/"

def get_id():
    r = requests.get(BASE_URL + "getUpdates").json()
    if r.get("result"):
        msg = r["result"][-1]["message"]
        return msg["chat"]["id"], msg.get("text", "")
    return None, ""

def send_message(ide_paydi, text):
    tugma1 = {"text": "😎 Call Tony Stark"}
    tugma2 = {"text": "❤️ Chat with Scarlett Johansson"}
    tugma3 = {"text": "👨‍❤️‍💋‍👨 Wanna marry to GPT 4 o1"}
    tugma4 = {"text": "😡 Kill Thanos"}
    tugma5 = {"text": "🌪️🌍 Destroy the Universe"}
    tugma6 = {"text": "🪐 Wanna have my own planet"}

    keyboard = {
        "keyboard": [
            [tugma1, tugma2],
            [tugma3, tugma4],
            [tugma5, tugma6]
        ],
        "resize_keyboard": True
    }
    data = {"chat_id": ide_paydi, "text": text, "reply_markup": keyboard}
    requests.post(BASE_URL + "sendMessage", json=data)
def blablablabla(chat_id, text):
    if text == "😎 Call Tony Stark":
        r = "Tony Stark is unavailable. He's in another galaxy."
    elif text == "❤️ Chat with Scarlett Johansson":
        r = "Sorry, she doesn't know you. Who are you again?"
    elif text == "👨‍❤️‍💋‍👨 Wanna marry to GPT 4 o1":
        r = "I wish you many happy robot children!"
    elif text == "😡 Kill Thanos":
        r = "Thor already did that (didn't you watch?)."
    elif text == "🌪️🌍 Destroy the Universe":
        r = "You can't even delete your Instagram, let alone the universe!"
    elif text == "🪐 Wanna have my own planet":
        r = "Sure, but then I'll be president of the USA!"
    else:
        r = "I don't understand. Please use the buttons."               
    send_message(chat_id, r)
def main():
    ide_paydi, text = get_id()
    if ide_paydi:
        bor_tugmalar = [
            "😎 Call Tony Stark", "❤️ Chat with Scarlett Johansson",
            "👨‍❤️‍💋‍👨 Wanna marry to GPT 4 o1", "😡 Kill Thanos",
            "🌪️🌍 Destroy the Universe", "🪐 Wanna have my own planet"
        ]
        if text in bor_tugmalar:
            blablablabla(ide_paydi, text)
        else:
            send_message(ide_paydi, "Lubboy tugmani taanlang, barbir ishlamaydi")
    else:
        chop_etish("Xabaar yuq xali")
if __name__ == "__main__":
   main()
       