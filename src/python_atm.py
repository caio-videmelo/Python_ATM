import time
from datetime import datetime
import pytz

# Global variables
saldo = 1000  # Initial ATM balance
valor_sacado = 0  # Amount withdrawn in the last withdrawal
valor_transferido = 0  # Amount transferred in the last transfer
data_saque = None  # Date and time of the last withdrawal
data_transferencia = None  # Date and time of the last transfer
transacoes = []  # List to store transactions
moeda = None  # Variable to store the selected currency
simbolo_moeda = ''  # Currency symbol
notas_disponiveis = []  # Available notes for the selected currency

# São Paulo time zone
saopaulo_tz = pytz.timezone('America/Sao_Paulo')

# Variables for messages in different languages
messages = {
    'english': {
        'welcome': "Choose the language: 1) English ; 2) Portuguese_BR",
        'selected_english': "The user selected the English language.",
        'selected_portuguese': "O usuário selecionou Português_BR.",
        'invalid_data': "Invalid data, ending the operation.",
        'withdrawal_limit': "It's impossible to withdraw this amount from this ATM with the available notes!",
        'insufficient_balance': "Insufficient balance to perform the withdrawal.",
        'available_balance': "Current balance: ",
        'available_notes': "AVAILABLE NOTES: ",
        'menu': "MENU:\n1 - Transfer\n2 - Withdrawal\n3 - Statement\nChoose an option: ",
        'combination_options': "Available note combinations:",
        'success_withdrawal': "Withdrawal successful!",
        'excedeu_limite': "Operation failed! Maximum number of withdrawals exceeded.",
        'success_transfer': "Transfer of {} {:.2f} successfully made to account {} at agency {} of bank {}!",
        'statement_preparation': "Statement in preparation...",
        'no_withdrawal': "No withdrawals made yet.",
        'no_transfer': "No transfers made yet.",
        'invalid_option': "Invalid option!",
        'choose_combination': "Choose the desired note combination: ",
        'printing_notes': "Printing, please wait for the notes to be counted and printed...",
        'withdrawal_value': "Withdrawal value: ",
        'transfer_amount': "Please inform the amount to be transferred: ",
        'select_currency': "Please select the desired currency: 1 - American Dollars (US$); 2 - Brazilian Real (R$); 3 - Euro (€); 4 - Pounds (£)",
        'currency_selected': "The currency chosen was ",
        'info_message': "PYBank is a simulation software, for educational purposes only. All transactions are fictitious. In this simulation, you'll start with a current balance of 1000 and the ATM has a withdrawal limit of 600. The currency will be chosen by the user.",
        'provide_data': "Please provide the required data.",
        'invalid_data': "Invalid data provided.",
        'account_number': "Please inform the account number to be credited:",  # Adicionada chave para account number
        'agency_number': "Please inform the agency number:",  # Adicionada chave para agency number
        'insufficient_balance': "Insufficient balance.",
        'success_transfer': "Transfer of {}{} to account {} at agency {} in bank {} was successful."
    },
    'portuguese': {
    'welcome': "Escolha o idioma: 1) Inglês ; 2) Português_BR",
    'selected_english': "O usuário selecionou o idioma inglês.",
    'selected_portuguese': "O usuário selecionou Português_BR.",
    'invalid_data': "Dados inválidos, encerrando a operação.",
    'available_balance': "Saldo disponível: ",
    'withdrawal_limit': "Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!",
    'insufficient_balance': "Saldo insuficiente para realizar o saque.",
    'available_notes': "NOTAS DISPONÍVEIS: ",
    'menu': "MENU:\n1 - Transferência\n2 - Saque\n3 - Extrato\nEscolha uma opção: ",
    'combination_options': "Combinações de notas disponíveis:",
    'success_withdrawal': "Saque realizado com sucesso!",
    'success_transfer': "Transferência de {} {:.2f} realizada com sucesso na conta {} da agência {} do banco {}!",
    'statement_preparation': "Extrato em preparação...",
    'no_withdrawal': "Nenhum saque realizado ainda.",
    'no_transfer': "Nenhuma transferência realizada ainda.",
    'invalid_option': "Opção inválida!",
    'choose_combination': "Escolha a combinação de notas desejada: ",
    'printing_notes': "Imprimindo, aguarde as notas serem contabilizadas e impressas...",
    'withdrawal_value': "Valor do saque: ",
    'transfer_amount': "Por favor, informe o valor a ser transferido: ",
    'select_currency': "Favor, escolher a moeda desejada: 1 - Dólares Americanos (US$); 2 - Real (R$); 3 - Euro (€); 4 - Libras (£)",
    'currency_selected': "A moeda escolhida foi ",
    'info_message': "PYBank é um software de simulação, para fins educacionais somente. Todas as transações são fictícias. Nesta simulação, você iniciará com um saldo de 1000 e o Caixa possui um limite de 600 para saque. A moeda será escolhida pelo usuário.",
    'bank_name': "Por favor, informe o nome do banco:",
    'account_number': "Por favor, informe o número da conta a ser creditada:",
    'agency_number': "Por favor, informe o número da agência:",
    'success_transfer': "Transferência de {}{} para a conta {} na agência {} do banco {} foi realizada com sucesso.",
    'provide_data': "Favor, forneça as informações necessárias.",  # Adicionada vírgula aqui
    'invalid_data': "Dados inválidos fornecidos.",
    'transfer_amount': "Por favor, informe o valor da transferência:",
    'insufficient_balance': "Saldo insuficiente."
    }
}

currency_options = {
    '1': {'english': 'American Dollars (US$)', 'portuguese': 'Dólares Americanos (US$)', 'symbol': 'US$', 'notes': [50, 20, 10]},
    '2': {'english': 'Brazilian Real (R$)', 'portuguese': 'Real (R$)', 'symbol': 'R$', 'notes': [50, 20, 10]},
    '3': {'english': 'Euro (€)', 'portuguese': 'Euro (€)', 'symbol': '€', 'notes': [50, 20, 10]},
    '4': {'english': 'Pounds (£)', 'portuguese': 'Libras (£)', 'symbol': '£', 'notes': [50, 20, 10]}
}


def calcular_combinacoes(valor):
    combinacoes = []
    for quantidade_nota50 in range(0, valor // 50 + 1):
        for quantidade_nota20 in range(0, (valor - quantidade_nota50 * 50) // 20 + 1):
            quantidade_nota10 = (valor - (quantidade_nota50 * 50 + quantidade_nota20 * 20)) // 10
            if (quantidade_nota50 * 50 + quantidade_nota20 * 20 + quantidade_nota10 * 10) == valor:
                combinacoes.append((quantidade_nota50, quantidade_nota20, quantidade_nota10))
    combinacoes.sort(key=lambda x: x[0] + x[1] + x[2])
    return combinacoes[:3]

def saque_dinheiro(lang):
    global saldo, valor_sacado, data_saque, simbolo_moeda

    # Prompt for withdrawal amount
    valor_saque = input(messages[lang]['withdrawal_value'])

    # Validate input
    if not valor_saque.replace(".", "").isdigit():
        print(messages[lang]['invalid_data'])
        return

    valor_saque = float(valor_saque)

    # Check if the withdrawal amount is valid
    if valor_saque < 10 or valor_saque > 600:
        print(messages[lang]['withdrawal_limit'])
        return

    # Check if the amount is a multiple of 10
    if valor_saque % 10 != 0:
        print(messages[lang]['withdrawal_limit'])
        return

    # Check if there is sufficient balance
    if valor_saque > saldo:
        print(messages[lang]['insufficient_balance'])
        return

    # Calculate combinations of notes
    combinacoes = calcular_combinacoes(int(valor_saque))

    if not combinacoes:
        print(messages[lang]['withdrawal_limit'])
        return

    print(messages[lang]['combination_options'])
    for i, (q50, q20, q10) in enumerate(combinacoes):
        partes = []
        if q50 > 0:
            partes.append(f"{q50} nota(s) de {simbolo_moeda} 50.00" if lang == 'portuguese' else f"{q50} note(s) of {simbolo_moeda} 50.00")
        if q20 > 0:
            partes.append(f"{q20} nota(s) de {simbolo_moeda} 20.00" if lang == 'portuguese' else f"{q20} note(s) of {simbolo_moeda} 20.00")
        if q10 > 0:
            partes.append(f"{q10} nota(s) de {simbolo_moeda} 10.00" if lang == 'portuguese' else f"{q10} note(s) of {simbolo_moeda} 10.00")
        print(f"Opção {i + 1}: {', '.join(partes)}" if lang == 'portuguese' else f"Option {i + 1}: {', '.join(partes)}")

    try:
        escolha = int(input(messages[lang]['choose_combination'])) - 1
    except ValueError:
        print(messages[lang]['invalid_option'])
        return

    if 0 <= escolha < len(combinacoes):
        print(messages[lang]['printing_notes'])
        time.sleep(1)
        q50, q20, q10 = combinacoes[escolha]
        if q50 > 0:
            print(f"{q50} nota(s) de {simbolo_moeda} 50.00" if lang == 'portuguese' else f"{q50} note(s) of {simbolo_moeda} 50.00")
        if q20 > 0:
            print(f"{q20} nota(s) de {simbolo_moeda} 20.00" if lang == 'portuguese' else f"{q20} note(s) of {simbolo_moeda} 20.00")
        if q10 > 0:
            print(f"{q10} nota(s) de {simbolo_moeda} 10.00" if lang == 'portuguese' else f"{q10} note(s) of {simbolo_moeda} 10.00")
        print(messages[lang]['success_withdrawal'])
        saldo -= valor_saque
        valor_sacado = valor_saque
        data_saque = datetime.now(saopaulo_tz)
    else:
        print(messages[lang]['invalid_option'])

def transferir_dinheiro(lang):
    global saldo, valor_transferido, data_transferencia, simbolo_moeda, conta, agencia, banco
    
    print(messages[lang]['provide_data'])

    # Solicitar o nome do banco
    print("Please inform the bank name:" if lang == 'english' else "Por favor, informe o nome do banco:")
    banco = input("Bank name: ") if lang == 'english' else input("Nome do banco: ")
    if not isinstance(banco, str):
        print(messages[lang]['invalid_data'])
        return

    # Solicitar o número da conta
    print(messages[lang]['account_number'])
    conta = input("Account number: ") if lang == 'english' else input("Número da conta: ")
    if not conta.isdigit():
        print(messages[lang]['invalid_data'])
        return

    # Solicitar o número da agência
    print(messages[lang]['agency_number'])
    agencia = input("Agency number: ") if lang == 'english' else input("Número da agência: ")
    if not agencia.isdigit():
        print(messages[lang]['invalid_data'])
        return

    # Solicitar o valor da transferência
    print(messages[lang]['transfer_amount'])
    valor_transferido = input(f"Transfer amount ({simbolo_moeda}): ") if lang == 'english' else input(f"Valor da transferência ({simbolo_moeda}): ")
    if not valor_transferido.replace(".", "").isdigit():
        print(messages[lang]['invalid_data'])
        return

    valor_transferido = float(valor_transferido)

    # Verifica se há saldo suficiente
    if valor_transferido > saldo:
        print(messages[lang]['insufficient_balance'])
        return

    saldo -= valor_transferido
    print(messages[lang]['success_transfer'].format(simbolo_moeda, valor_transferido, conta, agencia, banco))
    data_transferencia = datetime.now(saopaulo_tz)

def select_currency(lang):
    global currency_symbol, available_notes
    
    if lang == 'english':
        print("\nSelect Currency:")
        print("1) American Dollars (US$)")
        print("2) Brazilian Real (R$)")
        print("3) Euro (€)")
        print("4) Pounds (£)")
    else:
        print("\nSelecione a moeda:")
        print("1) Dólares Americanos (US$)")
        print("2) Real (R$)")
        print("3) Euro (€)")
        print("4) Libras (£)")
    
    currency_choice = input("Choose an option (1-4): " if lang == 'english' else "Escolha uma opção (1-4): ")
    
    currency_options = {
        '1': {'english': 'American Dollars (US$)', 'portuguese': 'Dólares Americanos (US$)', 'symbol': 'US$', 'notes': [50, 20, 10]},
        '2': {'english': 'Brazilian Real (R$)', 'portuguese': 'Real (R$)', 'symbol': 'R$', 'notes': [50, 20, 10]},
        '3': {'english': 'Euro (€)', 'portuguese': 'Euro (€)', 'symbol': '€', 'notes': [50, 20, 10]},
        '4': {'english': 'Pounds (£)', 'portuguese': 'Libras (£)', 'symbol': '£', 'notes': [50, 20, 10]}
    }
    
    if currency_choice in currency_options:
        currency_symbol = currency_options[currency_choice]['symbol']
        available_notes = currency_options[currency_choice]['notes']
        print(f"Moeda selecionada: {currency_options[currency_choice][lang]}")  # Mensagem localizada
    else:
        print("Invalid option. Please select a valid currency." if lang == 'english' else "Opção inválida. Por favor, selecione uma moeda válida.")
        select_currency(lang)
        
class Client:
    def __init__(self, name, client_id, date_of_birth, home_address):
        self.name = name
        self.client_id = client_id  # Este será o CPF
        self.date_of_birth = date_of_birth
        self.home_address = home_address

    def __str__(self):
        return (f"Cliente(Nome: {self.name}, CPF: {self.client_id}, "
                f"Data de Nascimento: {self.date_of_birth}, Endereço: {self.home_address})")


class BankAccount:
    account_counter = 1  # Variável de classe para rastrear os números das contas
    agency_number = "0001"  # Número de agência fixo para simplicidade
    bank_name = "PYBank"  # Nome do banco

    def __init__(self, client):
        self.account_number = f"{BankAccount.account_counter:04d}"  # Formatar número da conta com zeros à esquerda
        self.balance = 1000.0  # Saldo inicial
        self.client = client  # Associar a conta com um cliente
        BankAccount.account_counter += 1  # Incrementar o contador de contas para a próxima conta

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f"Conta Bancária(Número da Conta: {self.account_number}, "
                f"Número da Agência: {self.agency_number}, "
                f"Banco: {self.bank_name}, "
                f"Saldo: {self.balance:.2f}, "
                f"{self.client})")


def create_bank_account(lang):
    if lang == 'english':
        print("To create a new bank account, please provide:")
    else:
        print("Para criar uma nova conta bancária, por favor forneça:")

    name = input("Enter your name: " if lang == 'english' else "Digite seu nome: ")
    client_id = input("Enter your ID: " if lang == 'english' else "Digite seu CPF: ")  # Mensagem alterada
    date_of_birth = input(
        "Enter your date of birth (MM/DD/YYYY): " if lang == 'english' else "Digite sua data de nascimento (DD/MM/YYYY): "
    )
    home_address = input("Enter your home address: " if lang == 'english' else "Digite seu endereço: ")

    # Criar um novo cliente
    client = Client(name, client_id, date_of_birth, home_address)

    # Criar uma nova conta bancária para o cliente
    account = BankAccount(client)

    if lang == 'english':
        print("\nBank account created successfully!")
    else:
        print("\nConta bancária criada com sucesso!")

    print(account)

    return account

def main():
    # Mensagem introdutória
    print("Welcome to PYBank! / Bem-vindo(a) ao PYBank!")

    # Seleção de idioma
    print("Choose your language: 1) English ; 2) Portuguese_BR")
    language_choice = input("Choose an option (1 or 2): ")
    
    if language_choice == '1':
        lang = 'english'
        print("You have selected English.")
        print("PYBank is a simulation software, for educational purposes only. All transactions are fictitious. "
          "In this simulation, you'll start with a current balance of 1000 and the ATM has a withdrawal limit of 600. "
          "The currency will be chosen by the user.")
          
    elif language_choice == '2':
        lang = 'portuguese'
        print("Você selecionou Português.")
        print("PYBank é um software de simulação, para fins educacionais somente. Todas as transações são fictícias. "
          "Nesta simulação, você iniciará com um saldo de 1000 e o Caixa possui um limite de 600 para saque. "
          "A moeda será escolhida pelo usuário.")
    else:
        print("Invalid selection, defaulting to English.")
        lang = 'english'

    select_currency(lang)

    while True:
        if lang == 'english':
            print("\nMain Menu:")
            print("1) Transfer Money")
            print("2) Withdraw Money")
            print("3) Statement")
            print("4) Create Account")
            print("0) Exit")
        else:
            print("\nMenu Principal:")
            print("1) Transferir Dinheiro")
            print("2) Sacar Dinheiro")
            print("3) Extrato")
            print("4) Criar Conta")
            print("0) Sair")

        option = input("Choose an option (0-4): " if lang == 'english' else "Escolha uma opção (0-4): ")

        if option == "1":
                transferir_dinheiro(lang)
        elif option == "2":
                saque_dinheiro(lang)
        elif option == "3":
                print(messages[lang]['statement_preparation'])
                time.sleep(1)
                print(f"{messages[lang]['available_balance']} {simbolo_moeda} {saldo:.2f}")
            
        if data_transferencia:
                if lang == 'english':
                    print(messages[lang]['success_transfer'].format(simbolo_moeda, valor_transferido, conta, agencia, banco) + 
                        f" on {data_transferencia.strftime('%m/%d/%Y %H:%M')}")
                else:
                    print(messages[lang]['success_transfer'].format(simbolo_moeda, valor_transferido, conta, agencia, banco) + 
                        f" em {data_transferencia.strftime('%d/%m/%Y %H:%M')}")
            
        if data_saque:
                if lang == 'english':
                    print(f"{messages[lang]['withdrawal_value']}{simbolo_moeda} {valor_sacado:.2f} on {data_saque.strftime('%m/%d/%Y %H:%M')}")
                else:
                    print(f"{messages[lang]['withdrawal_value']}{simbolo_moeda} {valor_sacado:.2f} em {data_saque.strftime('%d/%m/%Y %H:%M')}")
            
        if not data_transferencia and not data_saque:
                print(messages[lang]['no_withdrawal'])
        elif option == "4":
                create_bank_account(lang)
        elif option == "0":  # Exit option
                print(messages[lang]['goodbye'])
                break  # Exit the loop
        else:
                print("Invalid option, please try again." if lang == 'english' else "Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()
