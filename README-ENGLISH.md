# ATM Simulator

This repository contains a Python-based ATM simulator. The simulator allows users to perform basic ATM operations such as language selection, currency selection, money transfer, cash withdrawal, and viewing account statements. It supports multiple languages (English and Brazilian Portuguese) and multiple currencies (US Dollars, Brazilian Real, Euro, and British Pounds).

## Features

Multi-language support: English and Brazilian Portuguese.

Multiple currency options: US Dollars (US$), Brazilian Real (R$), Euro (€), and British Pounds (£).

Basic ATM operations: Transfer money, withdraw money, and view account statement.

Note combinations for withdrawals to ensure valid note denominations.

User-friendly prompts and confirmations.

## How to Use

### Step 1: Language Selection

Prompt: "Choose the language: 1) English ; 2) Portuguese_BR"

User Input: Enter 1 for English or 2 for Portuguese_BR.

### Step 2: Currency Selection

Prompt: "Please select the desired currency: 1 - American Dollars (US$); 2 - Brazilian Real (R$); 3 - Euro (€); 4 - Pounds (£)"

User Input: Enter 1, 2, 3, or 4 based on the desired currency.

Confirmation: The application will confirm the selected currency, e.g., "The currency chosen was American Dollars (US$)".

### Step 3: Main Menu

Once the currency is selected, the user will see the main menu. Here, the user can choose to transfer money, withdraw money, or view the user's statement.

Prompt: "MENU:\n1 - Transfer\n2 - Withdrawal\n3 - Statement\nChoose an option: "

User Input: Enter 1, 2, or 3 based on the desired operation.

### Step 4: Transfer Money

Prompts:

a. "Please inform the bank name:"

b. "Please inform the account number to be credited:"

c. "Please inform the agency number:"

d. "Please inform the amount to be transferred: "

User Input: Provide the required details and transfer amount.

Confirmation: The application will confirm the successful transfer and update your balance.

### Step 5: Withdraw Money

Prompt: "Withdrawal value: "

User Input: Enter the amount desired to withdraw (must be a multiple of 10).

Confirmation: The application will print the notes and update the user's balance.

### Step 6: View Statement

Prompt: "Statement in preparation..."

Output: The application will show the user's current balance and recent transfers and withdrawals.

### Step 7: Handling Invalid Input

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
