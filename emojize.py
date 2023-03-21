emojis = {
        ":)" : "😀",
        ":(" : "😞",
        "lol" : "😂",
        "sick":"😨",
        "happy": "😀",
        "mermaid": "🧜‍"
}

user = input("").split(" ")

for text in user:
    if text in user:
        print(emojis[text])
   