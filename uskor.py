nachV=float(input())
konV=float(input())
t=float(input())
def uskor(nachV,konV,t):
    a=(konV-nachV)/t
    return a
print(uskor(nachV,konV,t))
def dekor(kuku):
    def obertka(nachV,konV,t):
        a=kuku(nachV,konV,t)
        print(nachV*t+(a*(t*t))/2)
    return obertka
uskor=dekor(uskor)
uskor(nachV,konV,t)