# Banking System

This repository contains a comprehensive banking system that facilitates user registration, login, balance inquiry, fund transfers, bill payments, donations, transaction history viewing, and account management. The system is designed to ensure secure and efficient handling of user data and transactions.

## Features

### 1. Registration
**User Requirements:**
- Account Number (14 digits)
- Debit Card Number (16 digits)
- ATM Pin (4 digits)
- CNIC (13 digits)
- User Name (4-10 characters)
- Password (5-12 characters)

**System Requirements:**
- Verify and validate the account number, debit card number, ATM pin, and CNIC against existing records.
- Ensure the user name is unique and adheres to length restrictions.
- Ensure the password adheres to length restrictions and has no invalid spaces.
- Write the registration details to a new file upon successful validation.

### 2. Login
**User Requirements:**
- User Name
- Password

**System Requirements:**
- Verify and validate the user name and password.
- Option to reset the password if the entered password is incorrect.

### 3. Current Balance
**System Requirements:**
- Display the current account balance after user login.
- Update the balance after every successful transaction.

### 4. Transfer Funds
**User Requirements:**
- Enter details for a new beneficiary or select from existing beneficiaries.
- Enter the transfer amount.

**System Requirements:**
- Validate the account number and nick name for new beneficiaries.
- Ensure the transfer amount is valid and does not exceed the current balance.
- Update the balance for both the sender and the recipient.

### 5. Receipt Generation
**System Requirements:**
- Display transaction details including time, sender's account number, sender's name, receiver's account number, receiver's name, and transferred amount.

### 6. Bills Payment
**User Requirements:**
- Select bill type and company name.
- Enter Bill ID (12 digits).

**System Requirements:**
- Verify and validate the Bill ID and amount.
- Ensure the balance is sufficient for bill payment.
- Update the bill status and user balance upon successful payment.

### 7. Donations
**User Requirements:**
- Select organization name and donation type.
- Enter donation amount.

**System Requirements:**
- Validate the donation amount and ensure the balance is sufficient.
- Update the balance and generate a receipt for the donation.

### 8. Transaction History
**System Requirements:**
- Display transaction details including amount, time, and receiver's account number.

### 9. Account Info
**User Requirements:**
- Option to reset password.

**System Requirements:**
- Display user information including username, account password, account number, and current balance.
- Allow the user to reset their password.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sudais0/banking-system.git
   cd banking-system
