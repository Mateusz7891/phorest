from models.CreditCard import CreditCard


class CreditCardBuilder:
    def __init__(self):
        self.card_number = None
        self.date = None
        self.cvc = None

    def with_test_data(self):
        self.card_number = "4111111111111111"
        self.date = "1225"
        self.cvc = "999"
        return self

    def build(self):
        return CreditCard(self.card_number, self.date, self.cvc)
