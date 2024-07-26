import time
from datetime import datetime
import pytz

# Variáveis globais
saldo = 1000  # Saldo inicial do caixa eletrônico
valor_sacado = 0  # Valor sacado no último saque
valor_transferido = 0  # Valor transferido na última transferência
data_saque = None  # Data e hora do último saque
data_transferencia = None  # Data e hora da última transferência
transacoes = []  # Lista para armazenar transações

# Fuso horário de São Paulo
saopaulo_tz = pytz.timezone('America/Sao_Paulo')

# Variáveis para mensagens em diferentes idiomas
messages = {
    'english': {
        'welcome': "Choose the language: 1) English ; 2) Portuguese_BR",
        'selected_english': "The user selected the English language.",
        'selected_portuguese': "O usuário selecionou Português_BR.",
        'invalid_data': "Invalid data, ending the operation.",
        'withdrawal_limit': "It's impossible to withdraw this amount from this ATM with the available notes!",
        'insufficient_balance': "Insufficient balance to perform the withdrawal.",
        'available_notes': "AVAILABLE NOTES: R$ 10.00, R$ 20.00, R$ 50.00",
        'menu': "MENU:\n1 - Transfer\n2 - Withdrawal\n3 - Statement\nChoose an option: ",
        'combination_options': "Available note combinations:",
        'success_withdrawal': "Withdrawal successful!",
        'success_transfer': "Transfer of R$ {:.2f} successfully made to account {} at agency {} of bank {}!",
        'statement_preparation': "Statement in preparation...",
        'no_withdrawal': "No withdrawals made yet.",
        'no_transfer': "No transfers made yet.",
        'invalid_option': "Invalid option!",
        'choose_combination': "Choose the desired note combination: ",
        'printing_notes': "Printing, please wait for the notes to be counted and printed...",
        'withdrawal_value': "Withdrawal value: ",
        'transfer_amount': "Please inform the amount to be transferred: ",
    },
    'portuguese': {
        'welcome': "Escolha o idioma: 1) Inglês ; 2) Português_BR",
        'selected_english': "O usuário selecionou o idioma inglês.",
        'selected_portuguese': "O usuário selecionou Português_BR.",
        'invalid_data': "Dados inválidos, encerrando a operação.",
        'withdrawal_limit': "Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!",
        'insufficient_balance': "Saldo insuficiente para realizar o saque.",
        'available_notes': "NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00",
        'menu': "MENU:\n1 - Transferência\n2 - Saque\n3 - Extrato\nEscolha uma opção: ",
        'combination_options': "Combinações de notas disponíveis:",
        'success_withdrawal': "Saque realizado com sucesso!",
        'success_transfer': "Transferência de R$ {:.2f} realizada com sucesso na conta {} da agência {} do banco {}!",
        'statement_preparation': "Extrato em preparação...",
        'no_withdrawal': "Nenhum saque realizado ainda.",
        'no_transfer': "Nenhuma transferência realizada ainda.",
        'invalid_option': "Opção inválida!",
        'choose_combination': "Escolha a combinação de notas desejada: ",
        'printing_notes': "Imprimindo, aguarde as notas serem contabilizadas e impressas...",
        'withdrawal_value': "Valor do saque: ",
        'transfer_amount': "Por favor, informe o valor a ser transferido: ",
    }
}

def calcular_combinacoes(valor):
    notas_disponiveis = [50, 20, 10]
    combinacoes = []

    for quantidade_nota50 in range(0, valor // 50 + 1):
        for quantidade_nota20 in range(0, (valor - quantidade_nota50 * 50) // 20 + 1):
            quantidade_nota10 = (valor - (quantidade_nota50 * 50 + quantidade_nota20 * 20)) // 10
            
            if (quantidade_nota50 * 50 + quantidade_nota20 * 20 + quantidade_nota10 * 10) == valor:
                combinacoes.append((quantidade_nota50, quantidade_nota20, quantidade_nota10))

    combinacoes.sort(key=lambda x: x[0] + x[1] + x[2])
    return combinacoes[:3]

def saque_dinheiro(lang):
    global saldo, valor_sacado, data_saque

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
            partes.append(f"{q50} note(s) of R$ 50.00")
        if q20 > 0:
            partes.append(f"{q20} note(s) of R$ 20.00")
        if q10 > 0:
            partes.append(f"{q10} note(s) of R$ 10.00")

        print(f"Option {i + 1}: {', '.join(partes)}")

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
            print(f"{q50} note(s) of R$ 50.00")
        if q20 > 0:
            print(f"{q20} note(s) of R$ 20.00")
        if q10 > 0:
            print(f"{q10} note(s) of R$ 10.00")
        print(messages[lang]['success_withdrawal'])
        saldo -= valor_saque
        valor_sacado = valor_saque
        data_saque = datetime.now(saopaulo_tz)
    else:
        print(messages[lang]['invalid_option'])

def transferir_dinheiro(lang):
    global saldo, valor_transferido, data_transferencia

    print("Please inform the bank name:")
    banco = input("Bank name: ")
    if not isinstance(banco, str):
        print(messages[lang]['invalid_data'])
        return

    print("Please inform the account number to be credited:")
    conta = input("Account number: ")
    if not conta.isdigit():
        print(messages[lang]['invalid_data'])
        return

    print("Please inform the agency number:")
    agencia = input("Agency number: ")
    if not agencia.isdigit():
        print(messages[lang]['invalid_data'])
        return

    print(messages[lang]['transfer_amount'])
    valor_transferido = input("Transfer amount: R$ ")
    if not valor_transferido.replace(".", "").isdigit():
        print(messages[lang]['invalid_data'])
        return

    valor_transferido = float(valor_transferido)

    # Check if there is sufficient balance
    if valor_transferido > saldo:
        print(messages[lang]['insufficient_balance'])
        return

    saldo -= valor_transferido
    print(messages[lang]['success_transfer'].format(valor_transferido, conta, agencia, banco))
    data_transferencia = datetime.now(saopaulo_tz)

def main():
    global valor_sacado, saldo, data_saque, valor_transferido, data_transferencia

    # Language selection
    print(messages['english']['welcome'])
    language_choice = input("Choose an option (1 or 2): ")
    if language_choice == '1':
        lang = 'english'
        print(messages['english']['selected_english'])
    elif language_choice == '2':
        lang = 'portuguese'
        print(messages['portuguese']['selected_portuguese'])
    else:
        print("Invalid selection, defaulting to English.")
        lang = 'english'

    print(messages[lang]['available_notes'])
    while True:
        print(messages[lang]['menu'])
        opcao = input()
        if opcao == "1":
            transferir_dinheiro(lang)
        elif opcao == "2":
            saque_dinheiro(lang)
        elif opcao == "3":
            print(messages[lang]['statement_preparation'])
            time.sleep(1)
            print(f"Current balance: R$ {saldo:.2f}")
            if data_transferencia:
                print(f"Transfer made on {data_transferencia.strftime('%m/%d/%Y %H:%M')} in the amount of R$ {valor_transferido:.2f}")
            if data_saque:
                print(f"Withdrawal made on {data_saque.strftime('%m/%d/%Y %H:%M')} in the amount of R$ {valor_sacado:.2f}")
            if not data_transferencia and not data_saque:
                print(messages[lang]['no_transfer'])
        else:
            print(messages[lang]['invalid_option'])

if __name__ == "__main__":
    main()
