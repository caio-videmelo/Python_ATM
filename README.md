# Simulador de Caixa Eletrônico

Este repositório contém um simulador de caixa eletrônico baseado em Python. O simulador permite que os usuários realizem operações básicas de caixa eletrônico, como seleção de idioma, seleção de moeda, transferência de dinheiro, saque de dinheiro e visualização de extratos. Ele suporta vários idiomas (Inglês e Português Brasileiro) e várias moedas (Dólares Americanos, Real Brasileiro, Euro e Libras Esterlinas).

## Recursos

Suporte a múltiplos idiomas: Inglês e Português Brasileiro.

Opções de moedas múltiplas: Dólares Americanos (US$), Real Brasileiro (R$), Euro (€) e Libras Esterlinas (£).

Operações básicas de caixa eletrônico: Transferência de dinheiro, saque de dinheiro e visualização de extrato.

Combinações de notas para saques, garantindo denominações válidas de notas.

Mensagens e confirmações amigáveis ao usuário.

## Como Usar

### Passo 1: Seleção de Idioma

Prompt: "Escolha o idioma: 1) Inglês ; 2) Português_BR"

Entrada do Usuário: Digite 1 para Inglês ou 2 para Português_BR.

### Passo 2: Seleção de Moeda

Prompt: "Por favor, selecione a moeda desejada: 1 - Dólares Americanos (US$); 2 - Real Brasileiro (R$); 3 - Euro (€); 4 - Libras (£)"

Entrada do Usuário: Digite 1, 2, 3 ou 4 com base na moeda desejada.

Confirmação: O aplicativo confirmará a moeda selecionada, por exemplo, "A moeda escolhida foi Dólares Americanos (US$)".

### Passo 3: Menu Principal

Uma vez que a moeda é selecionada, o usuário verá o menu principal. Aqui, o usuário pode escolher transferir dinheiro, sacar dinheiro ou visualizar o extrato do usuário.

Prompt: "MENU:\n1 - Transferência\n2 - Saque\n3 - Extrato\nEscolha uma opção: "

Entrada do Usuário: Digite 1, 2 ou 3 com base na operação desejada.

### Passo 4: Transferir Dinheiro

Prompts:

a. "Por favor, informe o nome do banco:"

b. "Por favor, informe o número da conta a ser creditada:"

c. "Por favor, informe o número da agência:"

d. "Por favor, informe o valor a ser transferido:"

Entrada do Usuário: Forneça os detalhes e o valor da transferência.

Confirmação: O aplicativo confirmará a transferência bem-sucedida e atualizará seu saldo.

### Passo 5: Sacar Dinheiro

Prompt: "Valor do saque:"

Entrada do Usuário: Digite o valor desejado para saque (deve ser múltiplo de 10).

Confirmação: O aplicativo imprimirá as notas e atualizará o saldo do usuário.

### Passo 6: Visualizar Extrato

Prompt: "Extrato em preparação..."

Saída: O aplicativo mostrará o saldo atual do usuário e as transferências e saques recentes.

### Passo 7: Tratamento de Entrada Inválida

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
