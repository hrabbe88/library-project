# Importera funktionerna för programmets meny
from project_library_class import (
    add_book,
    borrow_book,
    remove_book,
    return_book,
    search_books,
    list_books,
    edit_book,
)

# Skriv ut programmets meny

def print_menu():
    print("""
    ===== BIBLIOTEK =====
    1. Visa alla böcker
    2. Lägg till en bok
    3. Sök efter en bok
    4. Låna en bok
    5. Lämna tillbaka en bok
    6. Ta bort en bok
    7. Redigera bok
    8. Avsluta
    """)

##Loopar igenom menyn tills alternativ 8 väljs och avbryter loop (break).
def main():
    while True:
        print_menu()
        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            remove_book()
        elif choice == "7":
            edit_book()
        elif choice == "8":
            print("Programmet avslutas...")
            break
        else:
            print("Ogiltigt val. Välj ett alternativ mellan 1 till 8.")


if __name__ == "__main__":
    main()