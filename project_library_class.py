## Beskrivning av bok och info om bok i klassen
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        # Bok som är tillgänglig tills den lånas.
        self.is_borrowed = False

    ## Lånar bok om den inte redan är lånad. Utgår från att den inte är lånad.
    def borrow_book(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    # Lämna tillbaka bok om den är lånad.
    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

    ## Hur boken ska visas som text.
    def __str__(self):
        status = "Utlånad" if self.is_borrowed else "Tillgänglig"
        return f"{self.title} av {self.author} ({self.year}) - {status}"

## Lista på alla objekt (böcker) i biblioteket skapat i filen.
books = [
    Book("Greven av Monte Cristo", "Alexandre Dumas", 1844),
    Book("Emil i Lönneberga", "Astrid Lindgren", 1963),
    Book("Häxorna", "Roald Dahl", 1983),
    Book("Matilda", "Roald Dahl", 1988)
]


def list_books(book_list=None):
    if book_list is None:
        book_list = books

    if not book_list:
        print("Det finns inga böcker att visa.")
        return

    print("\nBöcker:")
    # enumerate ger varje bok ett nummer som användaren kan välja.
    for number, book in enumerate(book_list, start=1):
        print(f"{number}. {book}")

## Läser in via input info och lägger till bok i bibliotek.
def add_book():
    print("\n Lägg till en bok")
    title = input("Titel: ").strip()
    author = input("Författare: ").strip()
    year_input = input("Utgivningsår : ").strip()

    ## Kontroll så att titel och författare inte är tomt.
    if not title or not author:
        print("Fälten får inte vara tomma!")
        return

    ## Kontroll av årtal med siffror.
    if not year_input.isdigit():
        print("Utgivningsår måste vara heltal.")
        return

    ## Skapar ett objekt (bok) och lägger det sist i listan.
    books.append(Book(title, author, int(year_input)))
    print(f"{title} har lagts till i biblioteket.")

## (Input)Sökning av böcker med hjälp av söktext titel och författare
def search_books():
    search_text = input("Ange titel eller författare: ").strip().lower()

    ## Hindra tom sökning
    if not search_text:
        print("Du måste ange titel eller författare!")
        return

    ## Skapar en lista med objekt (böcker) som matchar sökningen.
    results = [
        book for book in books
        if search_text.lower() in book.title.lower()
        or search_text.lower() in book.author.lower()
    ]

    ## Visar träffarna eller ett meddelande om ingen bok hittades.
    if results:
        list_books(results)
    else:
        print("Ingen bok som du angivit hittades.")

## Visar en lista och låter användaren välja en bok med dess nummer.
def choose_book(book_list=None):
    if book_list is None:
        book_list = books

    if not book_list:
        print("\nDet finns inga böcker i biblioteket.")
        return None

    list_books(book_list)

    try:
        selected_book_number = int(
            input("Välj numret på boken: ").strip()
        )
    except ValueError:
        print("Du måste skriva ett heltal.")
        return None

    ## Kontroll att nummer motsvarar bok i listan
    if not 1 <= selected_book_number <= len(book_list):
        print("Angivet nummer eller bok finns inte")
        return None

    return book_list[selected_book_number - 1]

## Lån av tillgänglig bok.
def borrow_book():
    print("\nLåna en bok: ")

    # Skapar en lista av böcker som inte är utlånade.
    available_books = [
        book for book in books
        if not book.is_borrowed
    ]

    book = choose_book(available_books)
    if book is None:
        return

    # Frågar användaren om lånet ska bekräftas.
    response = input(
        f'Vill du låna "{book.title}"? (j/n): '
    ).strip().lower()

    if response not in ("j", "ja"):
        print("Lån avbrutet.")
        return

    # Ändrar bokens status till utlånad.
    if book.borrow_book():
        print(
            f'Du har lånat boken "{book.title}", '
            f'skriven av {book.author}.'
        )

## Lämnar tillbaka en bok.
def return_book():
    print("\nLämna tillbaka en bok:")
    book = choose_book()
    if book is None:
        return

    if book.return_book():
        print(f'"{book.title}" har lämnats tillbaka.')
    else:
        print("Boken är inte utlånad.")

def edit_book():
    print("\nÄndra en bok.")

    book = choose_book()
    if book is None:
        return

    new_title = input(f"Ny titel ({book.title}): ").strip()

    new_author = input(f"Ny författare ({book.author}): ").strip()

    new_year = input(f"Nytt utgivningsår ({book.year}): ").strip()

    # Kontrollerar intput/int på året innan boken ändras.
    if new_year and not new_year.isdigit():
        print("Utgivningsåret måste vara i siffror.")
        return

    # Tom inmatning betyder att det gamla värdet behålls.
    if new_title:
        book.title = new_title

    if new_author:
        book.author = new_author

    if new_year:
        book.year = int(new_year)

    print(f'"{book.title}" har uppdaterats!')


## Tar bort en bok från biblioteket.
def remove_book():
    print("\nTa bort en bok:")
    book = choose_book()
    if book is None:
        return

    books.remove(book)
    print(f'"{book.title}" har tagits bort.')
