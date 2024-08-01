# PYBank: Simulador de Caixa Eletrônico

Este repositório contém um simulador de caixa eletrônico baseado em Python. O simulador permite que os usuários realizem operações básicas de caixa eletrônico, como seleção de idioma, seleção de moeda, transferência de dinheiro, saque de dinheiro, visualização de extratos e criação de conta bancária. Ele suporta dois idiomas (Inglês e Português Brasileiro) e várias moedas (Dólares Americanos, Real Brasileiro, Euro e Libras Esterlinas).

## Recursos

Suporte a múltiplos idiomas: Inglês e Português Brasileiro.

Opções de moedas múltiplas: Dólares Americanos (US$), Real Brasileiro (R$), Euro (€) e Libras Esterlinas (£).

Operações básicas de caixa eletrônico: Transferência de dinheiro, saque de dinheiro e visualização de extrato.

Combinações de notas para saques, garantindo denominações válidas de notas.

Mensagens e confirmações amigáveis ao usuário.

Criação de Conta: Os usuários podem criar novas contas bancárias fornecendo suas informações pessoais, como nome, ID (CPF), data de nascimento e endereço.

Detalhes da Conta: Cada conta bancária exibe o número da conta, número da agência, notas disponíveis, saldo atual e as informações do cliente associado.

## Classe Client

A classe Client representa um cliente individual e armazena suas informações pessoais. Ela possui os seguintes atributos:

  name: O nome do cliente.

  client_id: O ID (CPF) do cliente.

  date_of_birth: A data de nascimento do cliente.

  home_address: O endereço do cliente.

A classe também inclui um método __str__ que retorna uma representação em string das informações do cliente.

## Classe BankAccount

A classe BankAccount representa uma conta bancária e gerencia os detalhes da conta. Ela possui os seguintes atributos:

  account_number: Um número de conta único gerado automaticamente.

  balance: O saldo atual da conta, inicialmente definido como 1000.

  client: O cliente associado à conta.

  currency_symbol: O símbolo da moeda selecionada.

  available_notes: As denominações disponíveis para a moeda selecionada.

A classe inclui os seguintes métodos:

  withdraw(amount): Subtrai o valor especificado do saldo da conta, se houver fundos suficientes.
  
  get_balance(): Retorna o saldo atual da conta.

__str__: Retorna uma representação em string dos detalhes da conta, incluindo o número da conta, número da agência, nome do banco, moeda, notas disponíveis, saldo e as informações do cliente associado.

## Como Usar

### Seleção de Idioma

Prompt: "Escolha o idioma: 1) Inglês ; 2) Português_BR"

Entrada do Usuário: Digite 1 para Inglês ou 2 para Português_BR.

### Seleção de Moeda

Prompt: "Por favor, selecione a moeda desejada: 1 - Dólares Americanos (US$); 2 - Real Brasileiro (R$); 3 - Euro (€); 4 - Libras (£)"

Entrada do Usuário: Digite 1, 2, 3 ou 4 com base na moeda desejada.

Confirmação: O aplicativo confirmará a moeda selecionada, por exemplo, "A moeda escolhida foi Dólares Americanos (US$)".

### Menu Principal

Uma vez que a moeda é selecionada, o usuário verá o menu principal. Aqui, o usuário pode escolher transferir dinheiro, sacar dinheiro ou visualizar o extrato do usuário.

Prompt: "MENU:\n1 - Transferência\n2 - Saque\n3 - Extrato\nEscolha uma opção: "

Entrada do Usuário: Digite 1, 2 ou 3 com base na operação desejada.

### Transferir Dinheiro

Prompts:

a. "Por favor, informe o nome do banco:"

b. "Por favor, informe o número da conta a ser creditada:"

c. "Por favor, informe o número da agência:"

d. "Por favor, informe o valor a ser transferido:"

Entrada do Usuário: Forneça os detalhes e o valor da transferência.

Confirmação: O aplicativo confirmará a transferência bem-sucedida e atualizará seu saldo.

### Sacar Dinheiro

Prompt: "Valor do saque:"

Entrada do Usuário: Digite o valor desejado para saque (deve ser múltiplo de 10).

Confirmação: O aplicativo imprimirá as notas e atualizará o saldo do usuário.

### Visualizar Extrato

Prompt: "Extrato em preparação..."

Saída: O aplicativo mostrará o saldo atual do usuário e as transferências e saques recentes.

### Criação de conta bancária

A função create_bank_account lida com a criação de uma nova conta bancária. Ela solicita que o usuário forneça suas informações pessoais, cria uma instância de Client e, em seguida, cria uma instância de BankAccount associada ao cliente. A função também seleciona a moeda para a conta e exibe uma mensagem de confirmação após a criação bem-sucedida da conta.

### Tratamento de Entrada Inválida

Se o usuário fornecer uma entrada inválida em qualquer etapa, o aplicativo notificará o usuário e solicitará que ele/ela/elu tente novamente.

### Exemplo de Uso

Selecionar Idioma:

Entrada: 1

Saída: "O usuário selecionou o idioma Inglês."

Selecionar Moeda:

Entrada: 2

Saída: "A moeda escolhida foi Real Brasileiro (R$)."

Menu Principal:

Entrada: 1

Saída: Solicita detalhes da transferência e valor.

## Transferir Dinheiro:

Entrada: Forneça nome do banco, número da conta, número da agência e valor da transferência.

Saída: "Transferência de R$ X,XX realizada com sucesso para a conta X na agência Y do banco Z!"

Menu Principal:

Entrada: 3

Saída: Mostra saldo atual e transações recentes.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/caio-videmelo/Python_ATM.git
```

Navegue até o diretório do projeto:

```bash
cd src
```

Execute a aplicação:

```bash
python python_atm.py
```

## Requisitos

Python 3.x

Biblioteca pytz

## Dependências

Instale as dependências usando o seguinte comando:

```bash
pip install pytz
```
## Licença

Este projeto é licenciado sob a Licença MIT.

## Agradecimentos

Este projeto é inspirado na necessidade de um simulador básico de caixa eletrônico para praticar programação em Python e entender operações bancárias básicas.

## Contribuições

Contribuições são bem-vindas! Por favor, faça um fork deste repositório e envie um pull request para quaisquer melhorias ou correções de bugs.
