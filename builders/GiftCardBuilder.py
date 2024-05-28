import random

from enums.GiftCardValue import GiftCardValue
from helpers import get_random_email, get_random_string
from models.GiftCard import GiftCard


class GiftCardBuilder:
    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None
        self.value = ""
        self.recipient_email = None
        self.recipient_message = None

    def with_send_to_me_data(self):
        self.email = "email_" + get_random_email(8)
        self.first_name = "first_name_" + get_random_string(7)
        self.last_name = "last_name_" + get_random_string(5)
        self.value = random.choice(list(GiftCardValue)).value
        self.recipient_email = self.email
        return self

    def with_send_to_someone_else_data(self):
        self.email = "email_" + get_random_email(8)
        self.first_name = "first_name_" + get_random_string(7)
        self.last_name = "last_name_" + get_random_string(5)
        self.value = random.choice(list(GiftCardValue)).value
        self.recipient_email = "email_" + get_random_email(8)
        self.recipient_message = get_random_string(25)
        return self

    def with_send_to_me_data_other(self):
        self.email = "email_" + get_random_email(8)
        self.first_name = "first_name_" + get_random_string(7)
        self.last_name = "last_name_" + get_random_string(5)
        self.value = str(random.randint(20, 1000))
        self.recipient_email = self.email
        return self

    def with_send_to_someone_else_data_other(self):
        self.email = "email_" + get_random_email(8)
        self.first_name = "first_name_" + get_random_string(7)
        self.last_name = "last_name_" + get_random_string(5)
        self.value = str(random.randint(20, 1000))
        self.recipient_email = "email_" + get_random_email(8)
        self.recipient_message = get_random_string(25)
        return self

    def build(self):
        return GiftCard(self.email, self.first_name, self.last_name, self.value, self.recipient_email, self.recipient_message)
