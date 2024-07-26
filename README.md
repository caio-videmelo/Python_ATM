# Caixa Eletrônico

Este projeto implementa um caixa eletrônico simples que permite realizar depósitos, saques e gerar extratos. O sistema suporta diferentes combinações de notas para o saque e exibe informações detalhadas sobre transações.

## Funcionalidades

### 1. Menu de seleção de idioma:

Este projeto suporta dois idiomas afim de oferecer maior acessibilidade. Ao inicializar o programa, é apresentado ao usuário um menu de seleção de idioma. Aqui vai como funciona:

### Como usar o menu de seleção de idioma:

Prompt inicial:Quando um programa começa, ele apresenta a seguinte mensagem:

```bash
Choose the language: 1) English ; 2) Portuguese_BR
```

### Selecionando o idioma:

Usuários podem escolher seu idioma de preferência digitano os números correspondentes:

1 para Inglês

2 para Português (Brasil)

### Mensagem de confirmação:

Após fazer a seleção, o programa confirma a escolha do usuário:

### Se inglês for selecionado:

```bash
The user selected the English language.
```

### Se português for selecionado:

```bash
O usuário selecionou Português_BR.
```

### Interação subsequente:

Uma vez que um idioma é selecionado, todas as mensagens subsequentes e outputs serão apresentados no idioma escolhido. Isso inclui:

- Mensagens de saque

- Instruções de transferência

- Menu de opções

- Mensagens de erro

### Exemplo de funcionamento:

### Usuário seleciona inglês:

Choose the language: 1) English ; 2) Portuguese_BR

Choose an option (1 or 2): 1

The user selected the English language.

AVAILABLE NOTES: R$ 10.00, R$ 20.00, R$ 50.00

MENU:

1 - Transfer

2 - Withdrawal

3 - Statement

Choose an option:

### Usuário seleciona português:

Escolha o idioma: 1) Inglês ; 2) Português_BR

Escolha uma opção (1 ou 2): 2

O usuário selecionou Português_BR.

NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00

MENU:

1 - Transferência

2 - Saque

3 - Extrato

Escolha uma opção:

2. **Transferência**
 
   - Permite que o usuário transfira uma quantia de dinheiro.
   - Solicita informações sobre o nome do banco, número da conta e agência.
   - Atualiza o saldo com o valor transferido.

3. **Saque**

   - Permite que o usuário saque uma quantia de dinheiro.
   - Exibe combinações possíveis de notas disponíveis (R$ 10,00, R$ 20,00 e R$ 50,00).
   - Verifica se o valor do saque é múltiplo de 10 e se está dentro dos limites permitidos.
   - Atualiza o saldo e registra a data e hora do saque com o fuso horário de São Paulo.

5. **Extrato**
 
   - Mostra o saldo atual.
   - Exibe informações sobre a última operação realizada, incluindo a data e hora no fuso horário de São Paulo.

## Requisitos

- Python 3.x
- Biblioteca `pytz` para gerenciamento de fuso horário (instalável via `pip install pytz`)

## Como Executar

1. Clone o repositório:
   ```bash
   git clone <(https://github.com/caio-videmelo/Python_ATM)>
   ```

2. Navegue até o diretório do projeto:
```bash
   cd <(https://github.com/caio-videmelo/Python_ATM/src/)>
```

3. Execute o script:
```bash
python_atm.py
```

## Detalhes do Fuso Horário

A data e hora dos saques são registradas no fuso horário de São Paulo (America/Sao_Paulo) para garantir a precisão das informações temporais.

## Requisitos

Python 3.x

## Contribuições

Se desejar contribuir com o projeto, siga estas etapas:

Faça um fork do repositório.

Crie uma nova branch para suas alterações (git checkout -b minha-nova-feature).

Faça commit das suas alterações (git commit -am 'Adiciona nova funcionalidade').

Faça push para a branch (git push origin minha-nova-feature).

Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
