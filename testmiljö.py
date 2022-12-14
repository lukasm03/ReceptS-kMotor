import math
from Enhetsomvandlare import enhetsomvandlare

kokbok = {"potatismos" : {"smör" : 100, "potatis" : 1000},
          "smoothie" : {"banan" : 100},
          "korv med bröd" : {"korv" : 500, "bröd" : 200}}

ingredienser = {}

def inmatning():
    totalt = input("Hur många ingredienser har du? ")
    while totalt.isnumeric() == False:
        print("Du måste ange antalet i siffror")
        totalt = input("Hur många ingredienser har du? ")
    n = 0
    while n < int(totalt):
        ingrediens = input(f"Ange ingrediens nr {n+1}: ")
        if ingrediens.isnumeric(): 
            print("Du måste ange ingrediensen med bokstäver ")
            ingrediens = input(f"Ange ingrediens nr {n+1}: ")
        else:
            #kan lägga in enhetsomvandlaren här om man vill
            mängd = input(f"Ange mängd av ingrediens nr {n+1}: ")
            while mängd.isnumeric() == True:
                print("Du måste ange mängd med nummer")
                mängd = input(f"Ange mängd av ingrediens nr {n+1}: ")
            else:
                ingredienser[ingrediens.lower()] = mängd.lower()
                n +=1
    svar = input("Vill du lägga till fler ingredienser y/n?")
    while svar.lower() != "y" or svar.lower() != "n":
        if svar.lower() == "y":
            inmatning()
            break
        elif svar.lower() == "n":
            recept_val()
            break
        print("Du måste ange antingen y eller n")
        #kanske lägga till annat meddelande om man vill lägga till fler ingredienser
        svar = input("Vill du lägga till fler ingredienser y/n? ")



def recept_val():
    for recept in kokbok:
        if all(elim in ingredienser for elim in kokbok[recept]):
            mängdkontroll = 0
            antal_portioner = []
            for receptkomponent in kokbok[recept]:
                for ingrediens in ingredienser:
                    if ingrediens == receptkomponent:
                        x = enhetsomvandlare(ingredienser[ingrediens])
                        y = kokbok[recept][receptkomponent]
                        if  x >= y: 
                            antal_portioner.append(math.floor(x/y))
                            mängdkontroll += 1              
            if mängdkontroll == len(kokbok[recept]):
                antal_portioner.sort()
                #skapa strängen som anger hur mycket av vilka ingredisenser som krävs
                antal_mängd = ""
                for x in kokbok[recept]:
                    antal_mängd += f'{(kokbok[recept][x])*antal_portioner[0]}g {x} och ' 
                if antal_portioner[0] == 1:
                    print(f'Du kan laga {recept} för {antal_portioner[0]} person.')
                else:
                    print(f'Du kan laga {recept} för {antal_portioner[0]} personer.')
                print(f'För detta recept krävs det {antal_mängd[:-5]}.')
                print()
            else:
                print("Inget recept matchar de ingredienser du angav.")
                print()
                
inmatning()
