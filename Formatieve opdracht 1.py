# In samenwerking met Achraf, Berke en Oualid

# Opdracht 1
def piramide_for():
    lengte = int(input("Kies een getal: "))
    sterretje = "*"
    for i in range(1, lengte + 1):
        print(i * sterretje)
    for j in range(lengte - 1, 0, -1):    # stapgrootte van -1 zodat 'ie achterstevoren gaat
        print(j * sterretje)
    return
piramide_for()

def piramide_while():
    lengte = int(input("Kies een getal: "))
    sterretje = "*"
    begin_getal = 0
    while begin_getal <= lengte:
        aantal_sterren = begin_getal * sterretje
        begin_getal = begin_getal + 1
        print(aantal_sterren)
    while lengte > 0:
        sterren_aantal = lengte * sterretje
        lengte = lengte - 1
        print(sterren_aantal)
    return
piramide_while()


# Opdracht 2
def strings():
    woord1 = input("Geef een string: ")
    woord2 = input("Geef nog een string: ")
    lengte1 = len(woord1)
    lengte2 = len(woord2)

    for i in range(lengte1):
        if woord1[i] != woord2[i]:
            print("Het eerste verschil is de " + str([i + 1]) + "e letter")
            break
strings()

# Opdracht 3
def count():
    x = int(input("Geef een getal tot 10 dat u wilt tellen: "))
    lijst = [1, 1, 2, 3, 3, 4, 5, 2, 1, 7, 3, 8, 2, 5, 9, 3, 3, 6, 2]
    tellen = lijst.count(x)
    print(tellen)
count()

def compare():
    lijst_positief = []
    lijst = [1, 1, 2, 3, 3, 4, 5, 2, 1, 7, 3, 8, 2, 5, 9, 3, 3, 6, 2]
    compare = [j - i for i, j in zip(lijst[: -1], lijst[1 :])]
    # Bovenstaande lijn van https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/
    for i in compare:
        a = [abs(i)]
        lijst_positief.append(a)
    print(max(lijst_positief))
compare()

def binair():
    bin_lijst = [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    aantal0 = count()
    aantal1 = count()
binair()

# Opdracht 4
def palindroom():
    woord = str(input("Geef een woord: "))
    if woord == woord[::-1]:
        print(woord + " is een palindroom.")
    else:
        print(woord + " is geen palindroom.")
palindroom()

# Opdracht 5:
def sorteren():
    lijst = [4, 3, 7, 2, 9, 4, 7, 2, 1]
    nieuwe_lijst = []
    while lijst:
        minimum = lijst[0]
        for i in lijst:
            if i < minimum:
                minimum = i
        nieuwe_lijst.append(minimum)
        lijst.remove(minimum)
    print(nieuwe_lijst)
sorteren()

# Opdracht 6
def gemiddelde():
    lijst = input("Geef een lijst met nummers met spaties ertussen: ")
    split = lijst.split()
    start = 0
    for i in split:
        start = start + int(i)
        gem = start / (len(split))
    print("Het gemiddelde is " + str(gem))
gemiddelde()
# bron: https://pynative.com/python-accept-list-input-from-user/

# Opdracht 7
import random
import time
def gokken():
    getal = random.randrange(0, 9)
    gok = int(input("Gok een getal onder de 10: "))
    while gok != getal:
        print("Fout gegokt. Probeer opnieuw.")
        time.sleep(1)
        gokken()
        break
    if gok == getal:
        print("Goed gegokt!")
gokken()

# Opdracht 8
def compress():
    file = open('testfile.txt', 'r')
    for line in file:
        lines = line.strip()
        if lines:
            print(lines)
compress()
# Bron: https://stackoverflow.com/questions/10794245/removing-spaces-and-empty-lines-from-a-file-using-python/10794299

# Opdracht 9
# We hadden veel moeite met deze opdracht, graag wat tips om te beginnen.

# Opdracht 10
def febonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)
getal = int(input('Geef een getal:'))
print(febonacci(getal))
# bron: https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

# Opdracht 11
def caesar():
    alfabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
    caesar_alfabet = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    invoer_tekst = str(input("Geef een tekst: "))
    invoer_rotatie = int(input("Geef een rotatie: "))

    caesar_tekst = ""
    for i in invoer_tekst.upper():
        if i.isalpha(): caesar_tekst += caesar_alfabet[ (alfabet[i] + invoer_rotatie)%26 ]
        else: caesar_tekst += i

    print(invoer_tekst)
    print(caesar_tekst.lower())
caesar()
# bron: https://gist.github.com/jameslyons/8701593

# Opdracht 11
def FizzBuzz():
    for Fizzbuzz in range(1, 101):
        if Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0:
            print('FizzBuzz')
            continue
        elif Fizzbuzz % 3 == 0:
            print('Fizz')
        elif Fizzbuzz % 5 == 0:
            print('Buzz')
        else:
            print(Fizzbuzz)
FizzBuzz()
