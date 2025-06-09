class Operation:
    
    opType: str
    value: float

    def __init__(self, opType: str, value: float):
        self.opType = opType
        self.value = value

class Account:

    withdraws: int = 0
    balance: float = 0
    operations: list[Operation] = []

    def deposit(self, value: float):
        if value <= 0:
            print("Insira um valor positivo para depósito.")
            return
        op = Operation('depósito', value)
        self.operations.append(op)
        self.balance += value
        print("Depósito efetuado com sucesso.")

    def withdraw(self, value: float):
        if value <= 0:
            print("Insira um valor positivo para o saque.")
            return
        if value > 500:
            print("Não é possível sacar valores acima de R$ 500.")
            return
        if self.balance < value:
            print("\nSaldo insuficiente.")
            print(f"Saldo da conta: R$ {self.balance:.2f}")
            return
        if self.withdraws >= 3:
            print("Limite de saques atingido.")
            return
        op = Operation('saque', value)
        self.operations.append(op)
        self.balance -= value
        self.withdraws += 1
        print("Saque efetuado com sucesso.")

    def check_bank_statement(self):
        print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        EXTRATO
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
        for op in self.operations:
            print(f"{op.opType.title()}: R$ {op.value:.2f}")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")        
        print(f"Saldo da conta: R$ {self.balance:.2f}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")  

account = Account()

def show_ops():
    print("""
    Operações:
    (d) Para depositar
    (s) Para sacar
    (e) Para visualizar extrato
    (c) Para sair
    """)

show_ops()

while True:
    i = input().lower()

    if i == "d":
        print("Valor do depósito: ", end='')
        try:
            v = float(input())
            account.deposit(v)
        except:
            print("Valor inválido.")
    
    elif i == "s":
        print("Valor do saque: ", end='')
        try:
            v = float(input())
            account.withdraw(v)
        except:
            print("Valor inválido.")

    elif i == "e":
        account.check_bank_statement()
    
    elif i == "c":
        break

    else:
        print("Opção inválida.")
    
    show_ops()

print("Fim do programa.")