from client import Client
from member import Member

a_client = Client('Andres','a@a.com',12345,'Home')
a_member = Member('Dulci','d@a.com',54321,'No Home')

def test_assign_num():
    assert a_client.number_set(54321) == 54321

def test_purchase():
    assert a_client.purchase('Cocacola',500,3) == '1500 units of Cocacola'
    
def test_print_object():
    assert str(a_client).startswith('This object is relate to:')

def test_assign_num2():
    assert a_member.number_set(202020) == 202020

def test_get_name():
    assert a_member.name_get() == 'Dulci'