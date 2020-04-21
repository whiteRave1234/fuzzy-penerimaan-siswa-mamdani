x = {} #Rules Array Dictionary
#[TPA_Label][UN_Label][Jarak_label]
#TPA    : 0 = Tinggi , 1 = Sedang , 2 = Rendah
#UN     : 0 = A , 1 = B , 2 = C, 3 =D
#Jarak  : 0 = Dekat, 1 = Normal, 2 = Jauh
#Tinggi
x[0][0][0] = 1      # -> Maks 1 karena hanya ada label untuk tinggi(0) dan rendah(1)
x[0][1][0] = 1
x[0][2][0] = 1
x[0][3][0] = 1
x[1][0][0] = 1
x[1][1][0] = 1
x[1][2][0] = 1
x[1][3][0] = 1
x[2][0][0] = 1
x[2][1][0] = 1
x[2][2][0] = 1
x[2][3][0] = 1
#Tinggi (UN = C|D)
x[0][0][1] = 1
x[0][1][1] = 1
x[1][0][1] = 1
x[1][1][1] = 1
x[2][0][1] = 1
x[2][1][1] = 1
#[TPA_Label][UN_Label][Jarak_label]
#TPA    : 0 = Tinggi , 1 = Sedang , 2 = Rendah
#UN     : 0 = A , 1 = B , 2 = C, 3 =D
#Jarak  : 0 = Dekat, 1 = Normal, 2 = Jauh
#Rendah (Jauh)
x[0][0][2] = 0
x[0][1][2] = 0
x[0][2][2] = 0
x[0][3][2] = 0
x[1][0][2] = 0
x[1][1][2] = 0
x[1][2][2] = 0
x[1][3][2] = 0
x[2][0][2] = 0
x[2][1][2] = 0
x[2][2][2] = 0
x[2][3][2] = 0
#Rendah (UN C|D)
x[0][2][1] = 0
x[0][3][1] = 0
x[1][2][1] = 0
x[1][3][1] = 0
x[2][2][1] = 0
x[3][3][1] = 0
class Inferensi :

    def __init__(self, TPA, UN, Jarak):
        #Ekstrak Array
        y = []
        z = []
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
                                #Get "Value" of NK not "which" NK
                                val = min(tpa,un,jarak) #minimasi nilai tpa,un,jarak
                                NKlabel = x[i][j][k]
                                if (NKlabel == 1):      #if NK == 1 -> Tinggi
                                    y.append(val)
                                elif (NKlabel == 0):    #elif NK == 0 -> Rendah
                                    z.append(val)
        #maksimisasi
        max(y)
        max(z)
