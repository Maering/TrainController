print(__name__)
from Orders.orders import P50XFeedback
from Orders.orders import P50XTurnOn
from Orders.orders import P50XTurnOff

def test_check():
    order = P50XFeedback()
    print(order)

def test_on():
    order = P50XTurnOn()
    print(order)

def test_off():
    order = P50XTurnOff()
    print(order)

test_check()
test_on()
test_off()