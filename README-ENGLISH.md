# ATM Simulator

This project simulates an ATM with basic functionalities for withdrawing, depositing, and generating a statement. The code is written in Python and is designed to manage cash transactions and provide a statement of transactions performed.

## Features

## 1. Language Selection Menu

The ATM simulation program supports two languages to enhance user accessibility. Upon starting the program, users are presented with a language selection menu. Here’s how it works:

### How to Use the Language Selection Menu

Initial Prompt: When the program starts, it displays the following message:

```bash
Choose the language: 1) English ; 2) Portuguese_BR
```

### Selecting a language:

Users can choose their preferred language by entering the corresponding number:

1 for English

2 for Portuguese (Brazil)

### Confirmation Message:

After making a selection, the program confirms the user's choice with a message:

If English is selected:

```bash
The user selected the English language.
```

If Portuguese is selected:

```bash
O usuário selecionou Português_BR.
```

### Subsequent Program Interaction:

Once a language is selected, all subsequent prompts, messages, and outputs will be displayed in the chosen language. This includes:

Withdrawal prompts

Deposit instructions

Menu options

Error messages

### Example Interactions:

User selects English:

```bash
Choose the language: 1) English ; 2) Portuguese_BR
Choose an option (1 or 2): 1
The user selected the English language.
AVAILABLE NOTES: R$ 10.00, R$ 20.00, R$ 50.00
MENU:
1 - Transfer
2 - Withdrawal
3 - Statement
Choose an option:
```

User selects Portuguese:

```bash
Escolha o idioma: 1) Inglês ; 2) Português_BR
Escolha uma opção (1 ou 2): 2
O usuário selecionou Português_BR.
NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00
MENU:
1 - Transferência
2 - Saque
3 - Extrato
Escolha uma opção:
```

### 2. Currency Selection Menu

Upon launching the application and selecting the preferred language, the user will be prompted to choose the currency for all transactions. This menu ensures that the user can conduct financial operations in the currency of his/her/they choice. The options available are:

a. American Dollars (US$)

b. Brazilian Real (R$)

c. Euro (€)

d. Pounds (£)

After selecting a currency, the application will confirm the user's choice and adjust all subsequent operations and statements to reflect the chosen currency. This includes displaying available notes, transaction amounts, and account balances using the appropriate currency symbol and denominations.

### 3. **Withdraw**

Allows the user to withdraw a specified amount and provides possible combinations of banknotes for the withdrawal. The ATM supports R$ 10.00, R$ 20.00, and R$ 50.00 banknotes. Options are presented to the user, who can choose the desired combination. The withdrawn amount is subtracted from the available balance and recorded for future reference.

- **Requirements:** The amount must be a multiple of R$ 10.00 and cannot exceed R$ 600.00.
- **Updates:** Updates the available balance and records the withdrawn amount and the date/time of the withdrawal.
- **Checks** if the withdrawal amount is a multiple of 10 and within the allowed limits.
- **Updates** the balance and records the date and time of the withdrawal with the São Paulo time zone.

### 4. **Transfer**

Allows the user to transfer an amount into a bank account. The user must provide the bank name, account number, agency number, and the transfer amount.

- **Requirements:** The amount must be a positive number.
- **Updates:** The transfer process deducts the transferred amount from the total amount of the user's bank account.

### 5. **Statement**

Generates a statement showing the current balance of the ATM and the details of the last withdrawal, if any. The statement includes:

- **Current Balance:** The available balance after all transactions.
- **Last Withdrawal:** The date/time and amount of the last withdrawal performed, including the date and time in the São Paulo time zone.

## Usage Instructions

1. **Clone the repository:**

    ```bash
    git clone (https://github.com/caio-videmelo/Python_ATM)
    cd src
    ```

2. **Run the script:**

    ```bash
    python python_atm.py
    ```

3. **Follow the instructions displayed in the menu:**

### Step 1: Language Selection

Prompt: "Choose the language: 1) English ; 2) Portuguese_BR"

User Input: Enter 1 for English or 2 for Portuguese_BR.

### Step 2: Currency Selection

Prompt: "Please select the desired currency: 1 - American Dollars (US$); 2 - Brazilian Real (R$); 3 - Euro (€); 4 - Pounds (£)"

User Input: Enter 1, 2, 3, or 4 based on the desired currency.

Confirmation: The application will confirm the selected currency, e.g., "The currency chosen was American Dollars (US$)".

### Step 3: Main Menu

Once the currency is selected, the user will see the main menu. Here the user can choose to transfer money, withdraw money, or view the user's statement.

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

If the user's provide an invalid input at any step, the application will notify the user and prompt him/her/they to try again.

## Example Usage:

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

## Requirements

Python 3.x
- `pytz` library for time zone management (installable via `pip install pytz`)

## Time Zone Details

The date and time of withdrawals are recorded in the São Paulo time zone (America/Sao_Paulo) to ensure the accuracy of the temporal information.

## Contributing

If you would like to contribute to the project, please follow these steps:

Fork the repository.

Create a new branch for your changes (git checkout -b my-new-feature).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin my-new-feature).

Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
