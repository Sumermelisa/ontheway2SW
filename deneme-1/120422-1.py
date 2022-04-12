import random

pics = ["""
   +---+
   |   |
       |
       |
       |
       |
==========""","""
   +---+
   |   |
   0   |
       |
       |
       |
==========""","""
   +---+
   |   |
   0   |
   |   |
       |
       |
==========""","""
   +---+
   |   |
   0   |
  /|   |
       |
       |
==========""","""
   +---+
   |   |
   0   |
  /|\  |
       |
       |
==========""","""
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
==========""","""
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========="""]

while True:
    print(("-" * 30)+ "\nHANGMAN\n" +("-" * 30))
    topic= random.choice(["dersler","günler","aylar","renkler"])
    print("konu:",topic)
    if topic== "dersler":
        word=random.choice(["matematik","fizik","edebiyat"])
    elif topic== "günler":
        word= random.choice(["çarşamba", "cuma", "salı"])
    elif topic== "aylar":
        word= random.choice(["mart", "haziran", "ekim"])
    elif topic== "renkler":
        word= random.choice(["mavi", "siyah", "turkuaz"])

    step=0
    letters= []

    while True:
        print(pics[step])

        for i, char in enumerate(word):
            print(char if i in letters else "_"),

        answer= input("tahmin:")

        if answer==word:
            print("TEBRİKLER!!!\n\n")
            break
        else:
            while True:
                rand= random.randint(0, len(word))
                if not rand in letters:
                    letters.append(rand)
                    break

            step+=1

        if step>= len(pics):
            print("kaybettiniz:(\n\n",word)
            break

    if not "y" == input("tekrar oyna"):
        break
