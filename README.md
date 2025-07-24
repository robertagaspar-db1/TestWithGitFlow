# Login System

- This project is a simple authentication system (signup, login, logout) built with good design practices and SOLID principles.

## Project Structure

```text
login_system/
├── interfaces.py         # Interfaces and contracts (abstractions)
├── storage.py            # Concrete storage implementations
├── user_service.py       # Business rules (signup, login, logout)
├── auth_controller.py    # Command Line Interface (CLI)
└── main.py               # Application entry point

