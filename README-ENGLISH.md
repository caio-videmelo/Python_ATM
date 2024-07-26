# ATM Simulator

This project simulates an ATM with basic functionalities for withdrawing, depositing, and generating a statement. The code is written in Python and is designed to manage cash transactions and provide a statement of transactions performed.

## Features

### 1. **Withdraw**

Allows the user to withdraw a specified amount and provides possible combinations of banknotes for the withdrawal. The ATM supports R$ 10.00, R$ 20.00, and R$ 50.00 banknotes. Options are presented to the user, who can choose the desired combination. The withdrawn amount is subtracted from the available balance and recorded for future reference.

- **Requirements:** The amount must be a multiple of R$ 10.00 and cannot exceed R$ 600.00.
- **Updates:** Updates the available balance and records the withdrawn amount and the date/time of the withdrawal.

### 2. **Deposit**

Allows the user to deposit an amount into a bank account. The user must provide the bank name, account number, agency number, and the deposit amount.

- **Requirements:** The amount must be a positive number.
- **Updates:** Adds the deposited amount to the available balance of the ATM.

### 3. **Statement**

Generates a statement showing the current balance of the ATM and the details of the last withdrawal, if any. The statement includes:

- **Current Balance:** The available balance after all transactions.
- **Last Withdrawal:** The date/time and amount of the last withdrawal performed.

## Usage Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/atm-simulator.git
    cd atm-simulator
    ```

2. **Run the script:**

    ```bash
    python atm_simulator.py
    ```

3. **Follow the instructions displayed in the menu:**

    - **1 - Deposit:** Provide the deposit details.
    - **2 - Withdraw:** Provide the withdrawal amount and choose the banknote combination.
    - **3 - Statement:** View the current balance and details of the last withdrawal.

## Example Execution

```plaintext
AVAILABLE BANKNOTES: R$ 10.00, R$ 20.00, R$ 50.00
MENU:
1 - Deposit
2 - Withdraw
3 - Statement
Choose an option: 2
Please specify the amount to withdraw:
Withdrawal amount: R$ 50
Available banknote combinations:
Option 1: 1 banknote(s) of R$ 50.00
Choose the desired banknote combination: 1
Printing, please wait for the notes to be dispensed...
1 banknote(s) of R$ 50.00
Withdrawal successful!
MENU:
1 - Deposit
2 - Withdraw
3 - Statement
Choose an option: 3
Statement in preparation...
Current balance: R$ 950.00
Withdrawal performed on 26/07/2024 15:50 for R$ 50.00
````
## Requirements

Python 3.x

## Contributing

If you would like to contribute to the project, please follow these steps:

Fork the repository.

Create a new branch for your changes (git checkout -b my-new-feature).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin my-new-feature).

Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.