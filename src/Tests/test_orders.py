from orders import P50XFeedback
from orders import P50XTurnsOn
from orders import P50XTurnsOff

def test_check():
    order = P50XFeedback()
    print(order)

def test_on():
    order = P50XTurnsOn()
    print(order)

def test_off():
    order = P50XTurnsOff()
    print(order)

test_check()
test_on()
test_off()