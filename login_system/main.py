from storage import JsonUserRepository, JsonSessionManager
from user_service import UserService
from auth_controller import AuthController

def main():
    user_repo = JsonUserRepository()
    session_manager = JsonSessionManager()
    service = UserService(user_repo, session_manager)
    controller = AuthController(service)
    controller.run()

if __name__ == "__main__":
    main()
