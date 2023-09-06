def hihi(odin, dva):
    print('Bublik, %s %s' % (odin, dva))
hihi('cola', 'fanta')

def rarara(lolo, kuku, gugu):
    return kuku - gugu + lolo
print(rarara(10, 11, 12))

class Robot:
    pass
class Robocop(Robot):
    def bronya(self):
        print('bronya')
    def spravedliviy(self):
        print('spravedliviy')
class Electronic(Robot):
    def begal(self):
        print('begal')
    def volos(self):
        print('volos')
class Alex_merfi(Robocop):
    pass
class Malec(Electronic):
    pass
class Blondin(Malec):
    pass
borodatiy = Malec()
borodatiy.begal()
villy = Malec()
villy.volos()
jiv = Alex_merfi()
jiv.bronya()





