import re
import getpass  # This is the "Security Pro" library for masking

def password_check(password):
    # (The same logic from before goes here)
    if len(password) < 8:
        return "❌ Length check failed. Needs 8+ characters."
    if re.search(r"\d", password) is None:
        return "❌ Strength check failed. Missing a digit."
    # ... (other checks) ...
    return "✅ Password Secured!"

print("--- 🌸 Secure Entry Portal 🌸 ---")
# Instead of input(), we use getpass.getpass()
# This will hide the characters as you type them!
user_input = getpass.getpass("Enter your secret password (it will be hidden): ")

print(password_check(user_input))
