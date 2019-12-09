
def main():
    print("""
[ 1 ] - Gerenciar Clubes
[ 2 ] - Gerenciar Campeonato
[ 0 ] - Sair
    """)
    menu = input("Digite uma opção: ")

    if(menu == "1"):
        from main_clubs import main_clubs
        main_clubs()
    elif(menu == "2"):
        from main_champ import main_champ
        main_champ()
    elif(menu == "0"):
        print('exit')
    else:
        print("Digite um comando valido")
        main()
main()
