from random import *

oddelovac = "-" * 50


#vrátí iterovaný list z vygenerovaného čísla
def createList(cislo):
    return [int(i) for i in str(cislo)]

#funkce udělá list z vygenerovaného čísla a porovná délku s listem který je převeden do setu
#kdyby v listu byli duplikáty, v setu se neukáží, protože v setu duplikát být nemůže
def noDuplicates(cislo):                            
    cislo_list = createList(cislo)
    if len(cislo_list) == len(set(cislo_list)):
        return True
    else:
        return False


#závíslá na True/False z funkce noDuplicates()
#bude generovat číslo tak dlouho, dokud nebude mít unikátní čísla
def generateCislo():
    while True:
        cislo = randint(1000,9999)
        if noDuplicates(cislo):
            return cislo



#vrací list, kdy na prvním indexu je počet bulls a na druhém počet cows
#z náhodného čísla udělá list, taktéž z čísla který zadává uživatel
#ve for loopu vezme zvlášť indexy a spojí je do tuplu, pak hodnoty v tuplu porovnává a vrací hodnoty podle podmínky
def pocetBullsCows(cislo, tip):
    bull_cow = [0,0]
    cislo_list = createList(cislo)
    tip_list = createList(tip)

    for i,j in zip(cislo_list,tip_list):
        
        if j in cislo_list:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1

    return bull_cow


cislo = generateCislo()
pocet_tipu = 0

print(f"""Hi there!
{oddelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovac}""")

while True:
    tip = input("Enter a number: ")

    if not tip.isnumeric():
        print("Zadej číslo!")
        print(oddelovac)
        continue

    if not noDuplicates(tip):
        print("Neměli by se opakovat čísla. Zkus znova.")
        print(oddelovac)
        continue

    if int(tip) < 1000 or int(tip) > 9999:
        print("Číslo musí být čtyřmístné nebo nesmí začínat nulou. Zkus znova.")
        print(oddelovac)
        continue
    
    bull_cow = pocetBullsCows(cislo, tip)

    bull = "bull" if bull_cow[0] == 1 else "bulls"
    cow = "cow" if bull_cow[1] == 1 else "cows"

    print(f"{bull_cow[0]} {bull}, {bull_cow[1]} {cow}")
    print(oddelovac)

    pocet_tipu += 1

    if bull_cow[0] == 4:
        print("Uhádl si správně!")
        if pocet_tipu == 1:
            print(f"Číslo si uhádl v {pocet_tipu} tipu, gratuluji!.")
        else:
            print(f"Číslo si uhádl ve {pocet_tipu} tipech.")
        break
