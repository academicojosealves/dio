def __init__(self, saldo_inicial=0):
    self.saldo = saldo_inicial

def depositar(self, montante):
    if montante > 0:
        self.saldo += montante
        print(f"Depósito de R${montante:.2f} realizado com sucesso.")
    else:
        print("O valor para depósito deve ser positivo.")

def sacar(self, montante):
    if 0 < montante <= self.saldo:
        self.saldo -= montante
        print(f"Saque de R${montante:.2f} realizado com sucesso.")
    elif montante > self.saldo:
        print("Saldo insuficiente para o saque.")
    else:

        print("O valor para saque deve ser positivo.")

def visualizar_saldo(self):
    print(f"O saldo atual é de R${self.saldo:.2f}")


depositar(0,500.00)
visualizar_saldo()
sacar(200)
visualizar_saldo()
