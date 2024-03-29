'''
Arguments: Full Name, Email, Phone Number, Address

'''
class Client:
    client_id = 1
    def __init__(self,client_full_name:str,client_email:str,client_phone:int,client_address:str):
        self.client_full_name = client_full_name
        self.client_email = client_email
        self._client_phone = client_phone
        self.client_address = client_address
        self.client_id = Client.client_id
        Client.client_id += 1

    def __str__(self):
        return f'This object is relate to: {self.client_full_name}'
        

    def print_details(self):
        return f'\nNAME: {self.client_full_name} \nEMAIL: {self.client_email} \nID: {self.client_id} \nPHONE: {self._client_phone} \nADDRESS: {self.client_address}'

    def purchase(self,product,price_per_unit,amount = 1):
        total = price_per_unit * amount
        return f'{total} units of {product}'
    
    def number_set(self,new_number:int):
        self._client_phone = new_number
        return self._client_phone

    def number_get(self):
        return self._client_phone
    
    def name_get(self):
        return self.client_full_name
