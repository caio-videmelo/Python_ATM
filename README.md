# Caixa Eletrônico

Este projeto simula um caixa eletrônico com funcionalidades básicas de saque, depósito e emissão de extrato. O código está escrito em Python e foi desenvolvido para gerenciar transações de saque e depósito, além de fornecer um extrato das transações realizadas.

## Funcionalidades

### 1. **Saque**

Permite ao usuário sacar um valor especificado e fornece combinações possíveis de notas para o saque. O caixa eletrônico suporta notas de R$ 10,00, R$ 20,00 e R$ 50,00. As opções são apresentadas ao usuário, que pode escolher a combinação desejada. O valor sacado é subtraído do saldo disponível e registrado para futuras referências.

- **Requisitos:** O valor deve ser múltiplo de R$ 10,00 e não pode exceder R$ 600,00.
- **Atualizações:** Atualiza o saldo disponível e registra o valor sacado e a data/hora do saque.

### 2. **Depósito**

Permite ao usuário depositar um valor em uma conta bancária. O usuário deve informar o nome do banco, o número da conta, o número da agência e o valor a ser depositado.

- **Requisitos:** O valor deve ser um número positivo.
- **Atualizações:** Adiciona o valor depositado ao saldo disponível do caixa eletrônico.

### 3. **Extrato**

Emite um extrato mostrando o saldo atual e as informações do último saque realizado, se houver. O extrato inclui:

- **Saldo atual:** O saldo disponível após todas as operações realizadas.
- **Último saque:** A data/hora e o valor do último saque realizado.

## Instruções de Uso

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu_usuario/caixa-eletronico.git
    cd caixa-eletronico
    ```

2. **Execute o script:**

    ```bash
    python python_atm.py
    ```

3. **Siga as instruções exibidas no menu:**

    - **1 - Depósito:** Informe os detalhes do depósito.
    - **2 - Saque:** Informe o valor a ser sacado e escolha a combinação de notas.
    - **3 - Extrato:** Visualize o saldo atual e as informações do último saque.

## Exemplo de Execução

```plaintext
NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00
MENU:
1 - Depósito
2 - Saque
3 - Extrato
Escolha uma opção: 2
Favor informar o valor a ser sacado:
Valor do saque: R$ 50
Combinações de notas disponíveis:
Opção 1: 1 nota(s) de R$ 50,00
Escolha a combinação de notas desejada: 1
Imprimindo, aguarde as notas serem contabilizadas e impressas...
1 nota(s) de R$ 50,00
Saque realizado com sucesso!
MENU:
1 - Depósito
2 - Saque
3 - Extrato
Escolha uma opção: 3
Extrato em preparação...
Saldo atual de R$ 950.00
Saque realizado em 26/07/2024 15:50 no valor de R$ 50.00
