def bd(n):
        a=1
        sum=0
        while n>0:
                sum+=(n%10)*a
                a=a*2
                n=n//10
        return sum
def db(n):
        a=1
        sum=0
        while n>0:
                sum+=(n%2)*a
                a=a*10
                n=n//2
        return sum
def bo(n):
        a=1
        x=0
        while n>0:
                x=bd(n%1000)*a+x
                a=a*10
                n=n//1000
        return x
def bh(n):
        h=''
        while n>0:
                x=bd(n%10000)
                if x>9:
                        h=chr(97+(x%10))+h
                else:
                        h=chr(48+x)+h
                n=n//10000
        return h
def ob(n):
        a=1
        z=0
        while n>0:
                x=n%10
                if x>7:
                        return "invalid input magane"
                z=db(x)*a+z
                a=a*1000
                n=n//10
        return z
def hb(n):
        l=-(n.__len__()+1)
        a=1
        i=-1
        z=0
        while i>l:
                x=ord(n[i])
                if x>96 and x<103:
                        x=(x-97)+10
                elif x>47 and x<58:
                        x=x-48
                else:
                        return "invalid op"
                z=db(x)*a+z
               
                a=a*10000
                i=i-1
        return z


def oh(n):
        return bh(ob(n))
def ho(n):
        return bo(hb(n))
def od(n):
        return bd(ob(n))
def do(n):
        return bo(db(n))
def dh(n):
        return bh(db(n))
def hd(n):
        return bd(hb(n))
