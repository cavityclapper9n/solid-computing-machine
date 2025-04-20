import random
import datetime

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "The future depends on what you do today. – Mahatma Gandhi",
    "It always seems impossible until it's done. – Nelson Mandela",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky"
]

def get_quote():
    today = datetime.date.today()
    index = today.toordinal() % len(quotes)  # Change daily
    return quotes[index]

if __name__ == "__main__":
    print("✨ Quote of the Day ✨")
    print(get_quote())
