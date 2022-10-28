def enhetsomvandlare(start_enhet):
    mängd = ""
    mängden = 0
    #loopa genom hela stringen med enheten
    for i in range(len(start_enhet)):
        #omvandlar kg till gram
        if start_enhet[i].lower() == "k" and start_enhet[i+1].lower() == "g":
            for m in range(len(start_enhet)-2):
                #addera siffrorna i stringen till mängd och gör sedan om mängd till en int
                #och multiplicera den för att få enheten till gram
                mängd += start_enhet[m]
                mängden = int(mängd)*1000
            return mängden
        #omvandlar mg till gram
        elif start_enhet[i].lower() == "m" and start_enhet[i+1].lower() == "g":
            for m in range(len(start_enhet)-2):
                mängd += start_enhet[m]
                mängden = int(mängd)/1000
            return mängden
        #omvandlar hg till gram
        elif start_enhet[i].lower() == "h" and start_enhet[i+1].lower() == "g":
            for m in range(len(start_enhet)-2):
                mängd += start_enhet[m]
                mängden = int(mängd)*100
            return mängden
        elif start_enhet[i].lower() == "g":
            for m in range(len(start_enhet)-1):
                mängd += start_enhet[m]
            return int(mängd)                
    
    
    
