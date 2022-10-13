from Enhetsomvandlare import enhetsomvandlare

recept = {"potatismos" : {"smör" : 100, "potatis" : 1000},
          "smoothie" : {"banan" : 100}}

ingredienser = {}
def inmatning():
    totalt = input("Hur många ingredienser har du? ")
    if totalt.isnumeric() == False:
        print("Du måste ange antalet i siffror")
        inmatning()
    n = 0
    while n < int(totalt):
        råvara = input(f"Ange ingrediens nr {n+1}: ")
        mängd = input(f"Ange mängd av ingrediens nr {n+1}: ")
        ingredienser[råvara.lower()] = mängd.lower()
        n +=1
    svar = input("Vill du lägga till fler ingredienser y/n? ")
    if svar.lower() == "y":
        inmatning()
    else:
        print("Du valde", ingredienser)
        recept_val()


def recept_val():
    x = 0
    for value in recept:
        for ingrediens in recept[value]:
            for råvara in ingredienser:
                if råvara == ingrediens:
                    if enhetsomvandlare(ingredienser[råvara]) >= recept[value][ingrediens]:
                        print("Du kan göra", value)
                        x = 1
    if x != 1:
        print("Du har inte tillräckligt med ingredienser för att laga något")
        inmatning()
    return None

inmatning()