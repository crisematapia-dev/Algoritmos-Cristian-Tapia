#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debefinalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un programa que lea los datos de las cuentas corrientes e informe:● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que: ○ Estado de la cuenta: ○ “Acreedor” si el saldo es > 0. ○ “Deudor” si el saldo es < 0. ○ “Nulo” si el saldo es = 0. ● b) La suma total de los saldos acreedores."""
total = 0

cuenta = 0

for i in range(3):

    cuenta = int(input("Ingrese numero de cuenta: "))
    saldo = int(input("Ingrese saldo: "))

    print("Cuenta:", cuenta)

    if saldo > 0:
        print("Estado: Acreedor")
        total = total + saldo

    if saldo < 0:
        print("Estado: Deudor")

    if saldo == 0:
        print("Estado: Nulo")

print("Suma total acreedores:", total)