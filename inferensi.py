class Inferensi :
    
    x = {}
    #Maks 1 karena hanya ada label untuk tinggi dan rendah
    #TInggi
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
            if tpa <= 0 : 
                pass
            else : 
                for j,un in enumerate(UN):
                    if UN <= 0 :
                        pass
                    else : 
                        for k,jarak in enumerate(Jarak):
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
    