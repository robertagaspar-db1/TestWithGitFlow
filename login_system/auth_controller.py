class AuthController:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            print("\n1 - Signup\n2 - Login\n3 - Logout\n4 - Quem está logado?\n5 - Sair")
            choice = input("Escolha: ")

            if choice == '1':
                u = input("Usuário: ")
                p = input("Senha: ")
                print(self.service.signup(u, p))
            elif choice == '2':
                u = input("Usuário: ")
                p = input("Senha: ")
                print(self.service.login(u, p))
            elif choice == '3':
                print(self.service.logout())
            elif choice == '4':
                user = self.service.current_user()
                print(f"Usuário logado: {user}" if user else "Ninguém está logado.")
            elif choice == '5':
                break
            else:
                print("Opção inválida.")
