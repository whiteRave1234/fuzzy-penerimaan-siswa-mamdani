class Defuzifkasi :
    def __init__(self,tinggi,rendah) :
        x=0;    a=0
        b=0;    c=0
        numerator=0
        while (x <= 10):
            if(x<=5 and x!=0):
                a=x+a
                counta=x
                numerator=(rendah*x)+numerator
            if(x==6):
                b==2
                if(rendah>=0.5 and tinggi >= 0.5):
                    numerator=0.5*x*2+(numerator)
                    countb=2
                elif(rendah>=0.5 and tinggi < 0.5):
                    numerator=(0.5*x)+(tinggi*x)
                elif(tinggi>= 0.5 and rendah < 0.5):
                    numerator=(0.5*x)+(rendah*x)
            if(x>=7):
                c=c+x
                countc=x-6
                numerator=numerator+(tinggi*x)
            x+=1
                
        if(rendah >= 0.5 and tinggi >= 0.5):    
            denumerator = (counta*rendah)+(countc*tinggi)+(0.5*countb)
            print("CountA = ",counta,"CountB = ",countb,"CountC = ",countc)
        elif (rendah < 0.5 and tinggi < 0.5):
            denumerator = (counta*rendah)+(countc*tinggi)+(rendah+tinggi)
        elif (rendah>=0.5 and tinggi < 0.5):
            denumerator = (counta*rendah)+(countc*tinggi)+(tinggi+0.5)
        elif (tinggi>= 0.5 and rendah < 0.5):
            denumerator = (counta*rendah)+(countc*tinggi)+(rendah+0.5)
            
        self.hasil=numerator/denumerator
        print(numerator)
        print(denumerator)
        print(self.hasil)