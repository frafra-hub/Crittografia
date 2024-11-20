def decifrario (word,key):
    decifrata=[]
    frase=""
    alfabeto=["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z"]
    for i in word:
        y=0
        if i == " ": decifrata.append(" ")
        for a in alfabeto:
            y=y+1
            if i==a:
                while key>21: key=key-21
                y=y-key
                if y<0: y=21+y
                decifrata.append(alfabeto[y-1])
    for h in decifrata:
        frase=frase+h
    return frase

risp=input("Digita:\n1. Se vuoi cifrare una parola o frase.\n2. Se vuoi decifrare una parola o frase.\n")
parola=input("Inserisci la parola o frase da cifrare/decifrare: \n").lower()
chiave=int(input("Inserisci la chiave:\n"))
if risp=="1":
    cifrata=[]
    stringa=""
    alfabeto=["a","b","c","d","e","f","g","h","i", "l","m","n","o","p","q","r","s","t","u","v","z"]
    for i in parola:
        y=0
        if i==" ":cifrata.append(" ")
        for a in alfabeto:
            y=y+1
            if i == a:
                while chiave>21:chiave=chiave-21
                y=y+chiave
                if y>21:
                    y=y-21
                cifrata.append(alfabeto[y-1])
    for h in cifrata:
        stringa=stringa+h
    print("La parola cifrata è:\n", stringa)
elif risp=="2": 
    #deci=decifrario(parola,chiave)
    print("La parola decifrata è\n", decifrario(parola,chiave))
else: "Torna quando avrai qualcosa da decifrare..."



