import uuid


def get_random_email(length):
    random_uuid = str(uuid.uuid4())[:length]
    email = f"{random_uuid}@example.com"
    return email

def get_random_string(length):
    random_uuid = str(uuid.uuid4())
    random_string = ''.join(random_uuid.split('-'))
    return random_string[:length]