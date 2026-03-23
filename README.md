# glam-secure-auth
A Python-based password validation module focusing on NIST standards and user privacy 
# Secure Entry Portal: Python Authentication Logic
### *Bridging Cybersecurity Standards with User-Centric Design*

## Project Overview
This project is a **Security Authentication Module** built in Python. It evaluates password strength based on **NIST 800-63B guidelines** while implementing privacy controls to prevent physical security threats like "shoulder surfing."

##  Key Security Features
* **Input Masking:** Utilizes the `getpass` library to hide plain-text passwords during entry.
* **Complexity Validation:** Uses **Regular Expressions (Regex)** to enforce:
    * Minimum 8-character length.
    * Requirement of uppercase, lowercase, numbers, and symbols.
* **Human-Centric Feedback:** Provides clear, encouraging error handling to improve the user "Glow-Up" experience.

## Technical Stack
* **Language:** Python 3.x
* **Libraries:** `re` (Regex), `getpass` (Privacy Masking)
* **Domain:** Identity and Access Management (IAM)

## How to Run
1. Clone the repo.
2. Run `python validator.py` in your terminal.
3. Witness the magic!
