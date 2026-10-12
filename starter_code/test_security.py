from security import hash_password, check_password, STORED_PASSWORD_HASH

print("Password hashing test:", bool(hash_password("hello")))
print("Correct password test:", check_password("CornerStore123!", STORED_PASSWORD_HASH))
print("Wrong password test:", check_password("wrongpassword", STORED_PASSWORD_HASH))
