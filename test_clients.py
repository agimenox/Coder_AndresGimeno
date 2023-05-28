from client import Client

a_client = Client('Andres','a@a.com',12345,'Home')

def test_assign_num():
    assert a_client.number_set(54321) == 54321

def test_purchase():
    assert a_client.purchase('Cocacola',500,3) == 1500
    
def test_print_object():
    assert str(a_client).startswith('This object is relate to:')