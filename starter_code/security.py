"""
security.py
------------
Task 6: A basic access-control gate for your sales reports.
"""

import hashlib
import getpass

# Demo password for this learning project
STORED_PASSWORD_HASH = hashlib.sha256(
    "CornerStore123!".encode("utf-8")
).hexdigest()


def hash_password(plain_text_password: str) -> str:
    """Return the SHA-256 hash of a password."""
    return hashlib.sha256(
        plain_text_password.encode("utf-8")
    ).hexdigest()


def check_password(attempt: str, stored_hash: str) -> bool:
    """Check whether the attempted password matches the stored hash."""
    return hash_password(attempt) == stored_hash


def login_gate(stored_hash: str, max_attempts: int = 3) -> bool:
    """Allow up to three attempts to enter the correct password."""
    for attempt_number in range(max_attempts):
        attempt = input("Enter password to view reports: ")

        if check_password(attempt, stored_hash):
            print("Access granted.")
            return True
        else:
            print("Incorrect password. Try again.")

    print("Access denied — too many failed attempts.")
    return False
