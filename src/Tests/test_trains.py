from Trains.train import Train
from Orders.orders import P50XUpdateLok

def test_train_init():
    t = Train('LokTest', 12)

    assert t.address_less_significant == 'c'
    assert t.address_less_significant == '0'
    assert t.speed == 0
    assert t.parameters == 'c0'

    # Change speed
    t.increaseSpeed()
    assert t.speed == 1

    # Toggle lights
    t.toggleLights()
    assert t.parameters == 'd0'

    # Toggle function F1
    t.toggleF1()
    assert t.parameters == 'd1'

def test_train_speed_change_to_64():
    t = Train('LokTest', 12)
    assert t.speed == 0
    t.increaseSpeed()
    assert t.speed == 1
    return True

print(test_train_init())
print(test_train_speed_change_to_64())
