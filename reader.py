def reader():
    name = input("Sinu nimi: ")
    comment = input("Sinu sõnum: ")
    time = datetime.datetime.now()
    action = input("Tegevus: ")
    text = f"Date: {time} Nimi: {name}, Oli selline tegevus: {action}\n"
    file = open("logs.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("jfvkiv oli salvestatu edukalt")