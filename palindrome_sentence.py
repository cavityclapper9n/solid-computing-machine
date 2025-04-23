import re

def is_palindrome(text):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

sentence = input("🔤 Enter a sentence: ")
print("✅ Palindrome!" if is_palindrome(sentence) else "❌ Not a palindrome.")
