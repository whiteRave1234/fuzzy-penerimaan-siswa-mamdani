class Inferensi :
    
    x = {} #Rules Array Dictionary
    #Maks 1 karena hanya ada label untuk tinggi dan rendah
    #Tinggi
    x[0][0][0] = 1
    x[0][0][0] = 1
    x[0][0][0] = 1
    x[0][0][0] = 1
    x[0][0][0] = 1
    x[0][0][0] = 1
    #Rendah
    x[0][0][0] = 0
    x[0][0][0] = 0
    x[0][0][0] = 0
    x[0][0][0] = 0
    x[0][0][0] = 0


    def __init__(self, TPA, UN, Jarak):
        #Ekstrak Array
        # y = []
        # z = []
        for i,tpa in enumerate(TPA):
            #i maks 3
            if tpa <= 0 : 
                pass
            else : 
                for j,un in enumerate(UN):
                    #j maks 3
                    if UN <= 0 :
                        pass
                    else : 
                        for k,jarak in enumerate(Jarak):
                            #k maks 4
                            if Jarak <= 0 :
                                pass
                            else : 
                                #Get Value of NK not which NK
                                val = min(tpa,un,jarak)
                                NKlabel = x[i][j][k]
                                if (NKlabel == 1):
                                    y.append(val)
                                elif (NKlabel == 0):
                                    z.append(val)
        max(y)
        max(z)
        
    def infer(self, TPA, UN, Jarak):
    