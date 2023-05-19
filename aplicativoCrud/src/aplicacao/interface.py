from validacoes import validacoes


def menu():
    print("qual funcao deseja acessar?")
    print("[1] marcar consulta")
    print("[2] acessar todas consultas")
    print("[3] acessar consulta por id")
    print("[4] atualizar uma consulta")
    print("[5] deletar consulta")
    print("[6] medidas de tendencia central da quantidade de consultas")

    try:
        valor = validacoes.validar_inteiro()
    except TypeError as e:
        print(e)
        menu()
    else:
        if valor < 1 or valor > 6:
            print("O valor deve ser menor que 1 e maior que 6, digite novamente. ")
            menu()
        else:
            return valor
