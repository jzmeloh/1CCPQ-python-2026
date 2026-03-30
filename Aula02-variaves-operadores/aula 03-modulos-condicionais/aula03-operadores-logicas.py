#logica e (and)


verificar_email = True
verificar_senha = True
verifica_login = verificar_email and verificar_senha
print(verifica_login)

if verifica_login:
    print("entrar no programa")


    #logica OU (or)

    logica_ou = False or True or False
    print(logica_ou)



    #operador de negação (not)

    negacao = not False
    print(negacao)


    if not verifica_login:
        print("esqueceu pnc?")



