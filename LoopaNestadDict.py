from Enhetsomvandlare import enhetsomvandlare

allarecept = {"korv och mos":
               [{"potatis": 1000}, {"korv": 2}, {"salt": "3tsk"}],
               "köttfärssås": [{"köttfärs": "1kg"}, {"sås": 1}]}

lista = {"potatis": "2kg"}


def test():
     for recept in allarecept:
         for ingredienser in allarecept[recept]:
             for ingrediens in ingredienser:
                 for mängd in lista:
                     if mängd == ingrediens:
                         if enhetsomvandlare(lista[mängd]) >= ingredienser[ingrediens]:
                             print("recept hittat", recept)
                    # print(mängd)
                 #print(f'du behöver {ingrediens} och mängd {ingredienser[ingrediens]}')
