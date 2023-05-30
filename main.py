'''In this program, we create 2 object from class Client and Member, Member have a especial discount of 15%
and Member class inherits from Client

'''
import time
from client import Client
from member import Member

def main():
    print('\nCreating Objets')
    new_client = Client('Andres Gimeno', 'agimenox@gmail.com', 123456, 'St Alberdi 200 Floor 2')
    new_member = Member('Tutor Coder','codertutor@coderhouse.com', 654321, 'St Kennedy 125 NY')
    time.sleep(2)

    '''Testing __str__ with inheritance'''
    print('\nMethod __str__')
    time.sleep(2)

    print(new_client)
    print(new_member)

    '''Testing print_details Method'''
    print('\nMethod printing_details')
    time.sleep(2) 

    print(new_client.print_details())
    print(new_member.print_details())

    '''Testing purchase method for a Client'''
    print('\nMethod purchase for a Client')
    time.sleep(2) 

    print(new_client.purchase('CocaCola', 800, 4))  #Arguments definition per position: (Product Name, Product Cost, amount to buy.) if amount is no given the default is 1.

    '''Testing purchase method for a Member'''
    print('\nMethod purchase for a Member')
    time.sleep(2) 

    print(new_member.purchase('Pepsi', 750,3)) # Producto, Precio, Cantidad

    '''Testin Setter and Getters'''
    print('\nGetters and Setters...')
    time.sleep(2) 

    print(new_client.number_get())  #Getter
    new_client.number_set(5599878)  #Setter

    print(new_member.number_get())
    new_member.number_set(21452)

    print('To test branch and pull request')


if __name__ == "__main__":
    main()