class Fuzzifikasi:
    #constructor
    def __init__(self,nama):
        self.calonsiswa=nama
        print(self.calonsiswa)
        self.memberTPA=[0,0,0]
        self.memberUN=[0,0,0,0]
        self.memberJarak=[0,0,0]

    def TPA(self,c_value):
        # Buruk
        if (c_value <= 33.3):
            TPAr=1
        elif(c_value<=45.95 and c_value>=33.3):
            TPAr=((45.95-c_value)/(45.95-33.3))
        else:
            TPAr=0
        # Sedang
        if(c_value>= 33.3 and c_value<=66.6):
            if c_value==49.95:
                TPAs=1
            elif(c_value<=49.95):
                TPAs=((c_value-33.3)/(66.6-33.3))
            elif(c_value>=49.95):
                TPAs=((66.6-c_value)/(66.6-49.95))
        else:
            TPAs=0

        # Tinggi
        if (c_value >= 66.6):
            TPAt=1
        elif(c_value>=49.95):
            TPAt=((c_value-49.95)/(66.6-49.95))
        else:
            TPAt=0

        # Update
        self.memberTPA=[TPAt,TPAs,TPAr]

    def UN(self,un):
        A=0
        B=0
        C=0
        D=0
        # D
        if(un<55):
            D=((55-un)/(55-0))
        else:
            D=0
        # C
        if (un>=0.0 and un<=70):
            #  UN < 55
            if(un==55):
                C=1
            elif(un<55):
                C=((un-0)/(55-0))
            elif(un>55):
                C=((70-un)/(70-55))
        else:
            C=0
        # B
        if (un>= 55 and un<=85):
            if(un>=70 and un<=75):
                B=1
            elif(un<=70):
                B=((un-55)/(70-55))
            elif(un>=75):
                B=((85-un)/(85-75))
        else:
            B=0
        # A
        if(un>=80):
            A=1
        elif(un>=75):
            A=((un-75)/(85-75))
        else:
            A=0
        
        # Update
        self.memberUN=[A,B,C,D]

    def Jarak(self,m):
        # Dekat
        if (m <= 4000):
            dekat=1
        elif (m<=6000 and m>=4000):
            dekat=((6000-m)/(6000-3000))
        else:
            dekat=0
        # Normal
        if(m>= 4000 and m<=8000):
            if m==6000:
                normal=1
            elif(m<=6000):
                normal=((m-4000)/(6000-4000))
            elif(m>=6000):
                normal=((8000-m)/(8000-6000))
        else:
            normal=0

        # Jauh
        if (m >= 8000):
            jauh=1
        elif(m>=6000):
            jauh=((m-6000)/(8000-6000))
        else:
            jauh=0

        # Update
        self.memberJarak=[dekat,normal,jauh]