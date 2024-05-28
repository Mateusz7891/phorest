class GiftCard:
    def __init__(self, email: str, first_name: str, last_name: str, value: str, recipient_email: str, recipient_message: str):

        self.email = email
        """ @type : str """

        self.recipient_email = recipient_email
        """ @type : str """

        self.first_name = first_name
        """ @type : str """

        self.last_name = last_name
        """ @type : str """

        self.value = value
        """ @type : str """

        self.recipient_message = recipient_message
        """ @type : str """
