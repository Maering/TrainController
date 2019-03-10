from src.Trains.train import Train
from src.Orders.orders import P50XUpdateLok

def test_train_init():
    t = Train('LokTest', 12)

    assert t.address_less_significant == 'c'
    assert t.address_less_significant == '0'
    assert t.speed == 0
    assert t.parameters == 'c0'

    # Change speed
    t.setSpeed(64)
    assert t.speed == 40

    # Toggle lights
    t.toggleLights()
    assert t.parameters == 'd0'

    # Toggle function F1
    t.toggleF1()
    assert t.parameters == 'd1'

def test_train_speed_change_to_64():
    t = Train('LokTest', 12)
    assert t.speed == 0
    t.setSpeed(64)
    assert t.speed == 40
    return True

def test_train_speed_change_to_128():
    ''' must fail '''
    t = Train('LokTest', 12)
    assert t.speed == 0
    t.setSpeed(128)
    assert t.speed == 0
    return True

print(test_train_init())
print(test_train_speed_change_to_64())
print(test_train_speed_change_to_128())
