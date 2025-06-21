# creditBanking_CLI - by Ishan Samanta (CSE -AI & ROBOTICS // B.Tech// University Of Engineering and Management, Kolkata)SESSION : 2025-2029
This is A CLI based simple credit card manager based on Beginner to intermediate OOP fundamentals (Python). This code is written in python and is under rigorous development and new features will be updated regularly.
# CONCEPTS INCLUDED :
💡 Concepts Used
* Class definition and __init__() constructor
* Instance methods for deposit, charge/payment, balance check
* Infinite loop logic to keep the CLI running until explicitly exited
* User interaction through input() and branching using conditions
* Clean separation of logic using methods

## Mechanism :
The application runs in a loop, allowing the user to:

1.Deposit money

2.Make a payment

3.View current balance

4.View card summary

5.Exit the program

It uses simple console input/output to simulate real-world interactions. The loop only stops when the user chooses to exit (-1 or option 5), ensuring continuous usage like a true banking system.

A simple self made project which is under development and will continuously be updated.
Thank you
# ----------------------------------------------------------------------------------------------------------------------------------
# WORK LOGS:
## First publishing date : 18th June, 2025 , time : <4:27 pm>
## UPDATE AND NEW FILE RECEIVED + BUG FIXED  : 18TH JUNE,2025
## MAJOR SECURITY UPDATE: Banking.py ---> Banking_V-02.py \\\ 21st June, 2025 
### 🛡️ Security Improvements in `Banking_V-02.py` (Patch Update) \\\ 21st June, 2025

###  Comparison: `Banking.py` → `Banking_V-02.py`\\\ 21st June, 2025

|  Feature             | ❌ Before                                     | ✅ After                                                   |
|------------------------|----------------------------------------------|------------------------------------------------------------|
| **PIN Verification**   | No PIN required for deposit or withdrawal    | Required before deposit and withdrawal (access controlled) |
| **Private Data**       | `self.pin` was public                        | `__pin` made private, accessed via property                |
| **Logical Access Flow**| Unchecked operations                         | PIN-based access gating implemented                        |
| **OOP Practices**      | Partial encapsulation                        | Proper encapsulation using properties and private members  |

### 🎥 Project Banking_V-02.py explanation link provided in Banking_V-02Readme.md file . Here is the youtube link : https://youtu.be/cbth10L-Nro?feature=shared \\\21ST June, 2025

