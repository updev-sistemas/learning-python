
class Car(object) :
    def __init__(self) -> None:
        self.ignition = True
        self.combusivel = 40.0

    def odometro(self) :
        base_consume = (self.combusivel / 40) * 100
        return base_consume

    def acelerar(self) :
        minus = self.combusivel * 0.003
        self.combusivel -= minus
        
        if self.combusivel < 0 :
            self.ignition = False
            self.combusivel = 0

    def status(self) :
        if self.combusivel > 0 :
            self.ignition = True
        else :
            self.ignition = False

if __name__ == '__main__' :

    car = Car()

    while True:
        car.acelerar()
        print('Combustivel = %f' % car.odometro())

        if car.ignition == False :
            break