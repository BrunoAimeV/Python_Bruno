import random
import time

def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

def trobada(canviTalaiot):
    print ("T'estas apropant al talaiot...")
    time.sleep(2)
    print ("Està fosc i és tenebrós...")
    time.sleep(2)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(2)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar...")
        return True
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        return False

partidaNova = "si"
punts = 0

while partidaNova == "s" or partidaNova == "si":
    intro()
    nTalaiot = canviTalaiot()
    if trobada(nTalaiot):
        punts += 1
    print(f"Has acumulat {punts} punts fins ara.")
    partidaNova = input("Vols tornar a menjar (jugar)? Introdueixi si o no: ")
    print("\n")

print(f"Final de la partida. Has aconseguit {punts} punt/s!")
