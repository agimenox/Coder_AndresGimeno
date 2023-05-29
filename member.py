from client import Client
class Member(Client):
    def __init__(self, client_full_name: str, client_email: str, client_phone: int, client_address: str, member_discount = 15):
        super().__init__(client_full_name, client_email, client_phone, client_address)
        self.member_discount = member_discount


    def print_details(self):
        return f'\nNAME: {self.client_full_name} \nEMAIL: {self.client_email} \nID: {self.client_id} \nPHONE: {self._client_phone} \nADDRESS: {self.client_address} \nDiscount: {self.member_discount} %'

    def purchase(self,product,price_per_unit,amount = 1):
        subtotal = price_per_unit * amount
        discount = subtotal * self.member_discount/100
        total = subtotal - discount
        return f'Congrats! You Purchase x{amount} {product} for {total}!!\n And you SAVE {discount}!!! \n We are going to send yours products to "{self.client_address}" in the next 3 Hours'    