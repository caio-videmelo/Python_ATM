# Caixa Eletrônico

Este projeto implementa um caixa eletrônico simples que permite realizar depósitos, saques e gerar extratos. O sistema suporta diferentes combinações de notas para o saque e exibe informações detalhadas sobre transações.

## Funcionalidades

1. **Depósito**
   - Permite que o usuário deposite uma quantia de dinheiro.
   - Solicita informações sobre o banco, número da conta e agência.
   - Atualiza o saldo com o valor depositado.

2. **Saque**
   - Permite que o usuário saque uma quantia de dinheiro.
   - Exibe combinações possíveis de notas disponíveis (R$ 10,00, R$ 20,00 e R$ 50,00).
   - Verifica se o valor do saque é múltiplo de 10 e se está dentro dos limites permitidos.
   - Atualiza o saldo e registra a data e hora do saque com o fuso horário de São Paulo.

3. **Extrato**
   - Mostra o saldo atual.
   - Exibe informações sobre o último saque, incluindo a data e hora no fuso horário de São Paulo.

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
