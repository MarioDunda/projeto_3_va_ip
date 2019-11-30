
def main():
    print("""
[ 1 ] - Gerenciar Clubes
[ 2 ] - Gerenciar Campeonato
[ 0 ] - Sair
    """)
    menu = input("Digite uma opção: ")

    if(menu == "1"):
        print("clubes")
    elif(menu == "2"):
        print("campeonato")
    elif(menu == "0"):
        print('exit')
    else:
        print("Digite um comando valido")
        main()
main()
