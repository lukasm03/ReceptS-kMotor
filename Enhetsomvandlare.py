allarecept = {"korv och mos":
              [{"potatis": 4}, {"korv": 2}, {"salt": "3tsk"}],
              "köttfärssås": [{"köttfärs": "1kg"}, {"sås": 1}]}



def test():
    for recept in allarecept:
        for ingredienser in allarecept[recept]:
            for ingrediens in ingredienser:
                print(f'du behöver {ingrediens} och mängd 
{ingredienser[ingrediens]}')
            
            "1kg"
            


                
def enhetsomvandlare(start_enhet):
    mängd = ""
    mängden = 0
    for i in range(len(start_enhet)):
        #omvandlar kg till gram
        if start_enhet[i] == "k" and start_enhet[i+1] == "g":
            for m in range(len(start_enhet)-2):
                mängd += start_enhet[m]
                mängden = int(mängd)*1000
            return f'{mängden} gram'
        #omvandlar mg till gram
        elif start_enhet[i] == "m" and start_enhet[i+1] == "g":
            for m in range(len(start_enhet)-2):
                mängd += start_enhet[m]
                mängden = int(mängd)/1000
            return f'{mängden} gram'
        #omvandlar hg till gram
        elif start_enhet[i] == "h" and start_enhet[i+1] == "g":
            for m in range(len(start_enhet)-2):
                mängd += start_enhet[m]
                mängden = int(mängd)*100
            return f'{mängden} gram'
        
                
    
    
    

