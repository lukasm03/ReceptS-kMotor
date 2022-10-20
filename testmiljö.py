import math
from Enhetsomvandlare import enhetsomvandlare

kokbok = {"potatismos" : {"smör" : 100, "potatis" : 1000},
          "smoothie" : {"banan" : 100},
          "korv med bröd" : {"korv" : 500, "bröd" : 200}}

ingredienser = {}

def inmatning():
    totalt = input("Hur många ingredienser har du? ")
    if totalt.isnumeric() == False:
        print("Du måste ange antalet i siffror")
        inmatning()
    n = 0
    while n < int(totalt):
        råvara = input(f"Ange ingrediens nr {n+1}: ")
        if råvara.isnumeric(): 
            print("Du måste ange råvaror med bokstäver")
            inmatning()
        else:
            mängd = input(f"Ange mängd av ingrediens nr {n+1}: ")
            if mängd.isnumeric() == False:
                print("Du måste ange mängd med nummer")
                inmatning()
            else:
                ingredienser[råvara.lower()] = mängd.lower()
                n +=1
    svar = input("Vill du lägga till fler ingredienser y/n? ")
    if svar.lower() == "y":
        inmatning()
    else:
        print("Du valde", ingredienser)
        recept_val()


def recept_val():
    for recept in kokbok:
        if all(elim in ingredienser for elim in kokbok[recept]):
            mängdkontroll = 0
            antal_portioner = []
            for receptkonponent in kokbok[recept]:  
                for ingrediens in ingredienser:
                    if ingrediens == receptkonponent:
                        x = enhetsomvandlare(ingredienser[ingrediens])
                        y = kokbok[recept][receptkonponent]
                        if  x >= y: 
                            antal_portioner.append(math.floor(x/y))
                            mängdkontroll += 1
                            
            if mängdkontroll == len(kokbok[recept]):
                antal_portioner.sort()
                print(f"Du kan laga {recept} för {antal_portioner[0]} personer")
                
inmatning()