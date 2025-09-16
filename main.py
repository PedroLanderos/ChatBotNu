# main.py
# -*- coding: utf-8 -*-

def menu():
    print("\n=== Centro de Chatbots ===")
    print("1) Bot NU (ExportarPrimerBloque)")
    print("q) Salir")

def main():
    while True:
        menu()
        op = input("> ").strip().lower()
        if op == "1":
            # Importa y ejecuta el bot de ExportarPrimerBloque
            from ExportarPrimerBloque import run_chatbot_nu
            run_chatbot_nu()
        elif op in ("q", "quit", "salir"):
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
