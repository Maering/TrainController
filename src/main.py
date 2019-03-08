from serialHandler import SerialHandler
from train import Train
from Orders.orders import P50XUpdateLok
#  MAIN 
#serialHandler = SerialHandler.getInstance()
#serialHandler.connect('ttyS0')

if __name__ == '__main__':
    t = Train('LokTest', 12)

    print(t)
    print(t.speed)
    t.setSpeed(64)
    print(t.speed)
    print(t.parameters)

    o = P50XUpdateLok(t)
    print(o)

    t.toggleLights()
    o = P50XUpdateLok(t)
    print(o)

    t.toggleF1()
    o = P50XUpdateLok(t)
    print(o)

