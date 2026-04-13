import random
import string
import uuid


def generate_new_user_name():
    return f"user_{uuid.uuid4().hex[:8]}"


def generate_new_user_email():
    return f"test_{uuid.uuid4().hex[:10]}@example.com"


def generate_new_user_password():
    letters = ''.join(random.choices(string.ascii_letters, k=5))
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{letters}{digits}"