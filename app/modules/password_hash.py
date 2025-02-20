from argon2 import PasswordHasher

def get_password_hasher():
    return PasswordHasher()