import textwrap


def menu():
    opcoes = """
    ================ MENU ================

    [d]  Depositar
    [s]  Sacar
    [e]  Exibir extrato
    [nu] Cadastrar usuário
    [nc] Criar conta
    [lc] Listar contas
    [q]  Sair

    Escolha uma opção: """

    return input(textwrap.dedent(opcoes)).strip().lower()


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("\nOperação não realizada: informe um valor positivo.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"

    print("\nDepósito realizado com sucesso!")
    return saldo, extrato


def sacar(
    *,
    saldo,
    valor,
    extrato,
    limite,
    numero_saques,
    limite_saques,
):
    if valor <= 0:
        print("\nOperação não realizada: informe um valor positivo.")

    elif valor > saldo:
        print("\nOperação não realizada: saldo insuficiente.")

    elif valor > limite:
        print(f"\nOperação não realizada: o limite por saque é R$ {limite:.2f}.")

    elif numero_saques >= limite_saques:
        print("\nOperação não realizada: limite diário de saques atingido.")

    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"

        print("\nSaque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")

    if extrato:
        print(extrato, end="")
    else:
        print("Nenhuma movimentação foi realizada.")

    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("=========================================")


def limpar_cpf(cpf):
    return "".join(numero for numero in cpf if numero.isdigit())


def filtrar_usuario(cpf, usuarios):
    cpf = limpar_cpf(cpf)

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

    return None


def criar_usuario(usuarios):
    cpf = limpar_cpf(input("Informe o CPF: "))

    if len(cpf) != 11:
        print("\nCPF inválido. Informe os 11 números.")
        return

    if filtrar_usuario(cpf, usuarios):
        print("\nJá existe um usuário cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input(
        "Informe a data de nascimento (dd/mm/aaaa): "
    ).strip()
    endereco = input(
        "Informe o endereço (logradouro, número - bairro - cidade/UF): "
    ).strip()

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("\nUsuário cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = limpar_cpf(input("Informe o CPF do titular: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado. Cadastre o usuário antes de criar a conta.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
    }

    print("\nConta criada com sucesso!")
    return conta


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta foi cadastrada.")
        return

    print("\n================ CONTAS ================")

    for conta in contas:
        informacoes = f"""
        Agência: {conta["agencia"]}
        Conta:   {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        CPF:     {conta["usuario"]["cpf"]}
        """

        print(textwrap.dedent(informacoes))
        print("-" * 40)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))

            saldo, extrato = depositar(
                saldo,
                valor,
                extrato,
            )

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(
                saldo,
                extrato=extrato,
            )

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1

            nova_conta = criar_conta(
                AGENCIA,
                numero_conta,
                usuarios,
            )

            if nova_conta:
                contas.append(nova_conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nSistema bancário encerrado.")
            break

        else:
            print("\nOpção inválida. Escolha uma opção disponível no menu.")


if __name__ == "__main__":
    main()