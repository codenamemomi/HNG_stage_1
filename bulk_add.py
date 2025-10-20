import requests

BASE_URL = "http://127.0.0.1:8000/strings"

strings = [
    "madam", "racecar", "hello world", "A man a plan a canal Panama",
    "fastapi rocks", "level", "rotor", "zebra zone", "xyz", "moon noon",
    "civic", "reviver", "palindrome test string", "amazing app", "kayak",
    "rotavator", "refer", "wow", "xylophone tune", "zoo", "the quick brown fox",
    "madam madam", "abba", "python code", "never odd or even",
    "supercalifragilisticexpialidocious", "red rum sir is murder",
    "a toyota", "test123", "stats"
]

for s in strings:
    res = requests.post(BASE_URL, json={"value": s})
    print(f"{s} → {res.status_code}")
