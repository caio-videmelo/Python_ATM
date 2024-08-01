# PYBank: ATM Simulator

This repository contains a Python-based ATM simulator. The simulator allows users to perform basic ATM operations such as language selection, currency selection, money transfer, cash withdrawal, and viewing account statements. It supports multiple languages (English and Brazilian Portuguese) and multiple currencies (US Dollars, Brazilian Real, Euro, and British Pounds).

## Features

Multi-language support: English and Brazilian Portuguese.

Multiple currency options: US Dollars (US$), Brazilian Real (R$), Euro (€), and British Pounds (£).

Basic ATM operations: Transfer money, withdraw money, and view account statement.

Note combinations for withdrawals to ensure valid note denominations.

User-friendly prompts and confirmations.

Account Creation: Users can create new bank accounts by providing their personal information, such as name, ID, date of birth, and home address.

Account Details: Each bank account displays the account number, agency number, available notes, current balance, and the associated client information.

## 'Client' Class

The Client class represents an individual client and stores their personal information. It has the following attributes:

  name: The client's name.

  client_id: The client's ID (CPF).

  date_of_birth: The client's date of birth.

  home_address: The client's home address.

The class also includes a __str__ method that returns a string representation of the client's information.

## 'BankAccount' Class

The BankAccount class represents a bank account and manages the account details. It has the following attributes:

  account_number: A unique account number generated automatically.

  balance: The current balance of the account, initially set to 1000.

  client: The client associated with the account.

  currency_symbol: The symbol of the selected currency.

  available_notes: The available denominations for the selected currency.

The class includes the following methods:

  withdraw(amount): Subtracts the specified amount from the account balance if sufficient funds are available.

  get_balance(): Returns the current balance of the account.

__str__: Returns a string representation of the account details, including the account number, agency number, bank name, currency, available notes, balance, and the associated client information.

## How to Use

### Language Selection

Prompt: "Choose the language: 1) English ; 2) Portuguese_BR"

User Input: Enter 1 for English or 2 for Portuguese_BR.

### Currency Selection

Prompt: "Please select the desired currency: 1 - American Dollars (US$); 2 - Brazilian Real (R$); 3 - Euro (€); 4 - Pounds (£)"

User Input: Enter 1, 2, 3, or 4 based on the desired currency.

Confirmation: The application will confirm the selected currency, e.g., "The currency chosen was American Dollars (US$)".

### Main Menu

Once the currency is selected, the user will see the main menu. Here, the user can choose to transfer money, withdraw money, or view the user's statement.

Prompt: "MENU:\n1 - Transfer\n2 - Withdrawal\n3 - Statement\nChoose an option: "

User Input: Enter 1, 2, or 3 based on the desired operation.

### Transfer Money

Prompts:

a. "Please inform the bank name:"

b. "Please inform the account number to be credited:"

c. "Please inform the agency number:"

d. "Please inform the amount to be transferred: "

User Input: Provide the required details and transfer amount.

Confirmation: The application will confirm the successful transfer and update your balance.

### Withdraw Money

Prompt: "Withdrawal value: "

User Input: Enter the amount desired to withdraw (must be a multiple of 10).

Confirmation: The application will print the notes and update the user's balance.

### View Statement

Prompt: "Statement in preparation..."

Output: The application will show the user's current balance and recent transfers and withdrawals.

### Creating a bank account

The create_bank_account function handles the creation of a new bank account. It prompts the user to provide their personal information, creates a Client instance, and then creates a BankAccount instance associated with the client. The function also selects the currency for the account and displays a confirmation message upon successful account creation.

### Handling Invalid Input

If the user provides an invalid input at any step, the application will notify the user and prompt them to try again.

## Example Usage

Select Language:
Input: 1

Output: "The user selected the English language."

Select Currency:
Input: 2

Output: "The currency chosen was Brazilian Real (R$)."

Main Menu:
Input: 1

Output: Prompts for transfer details and amount.

Transfer Money:
Input: Provide bank name, account number, agency number, and transfer amount.

Output: "Transfer of R$ X.XX successfully made to account X at agency Y of bank Z!"

Main Menu:
Input: 3

Output: Displays current balance and recent transactions.

## Installation

Clone the repository:

```bash
git clone https://github.com/caio-videmelo/Python_ATM.git
```

Navigate to the project directory:

```bash
cd src
```

Run the application:

```bash
python python_atm.py
```

## Requirements

Python 3.x

pytz library

## Dependencies

Install the dependencies using the following command:

```bash
pip install pytz
```

## License

This project is licensed under the MIT License.

## Acknowledgments

This project is inspired by the need for a basic ATM simulator to practice Python programming and understanding basic banking operations.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.
