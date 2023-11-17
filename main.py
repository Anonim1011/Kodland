slowa = {
    "lol": "odpowiedź na coś zabawnego", 
    "CRINGE": "coś dziwnego lub wstydliwego", 
    "ROFL": "odpowiedź na żart", "SHEESH": " lekka dezaprobata",
    "SHEESH": "lekka dezaprobata",
    "CREEPY ": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły"
}

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in slowa.keys():
    print(slowa[word])
else:
    print("nie ma takiego slowa")
