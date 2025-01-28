from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize_book import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displaying = DisplayConsole() if method_type == "console"\
                else DisplayReverse()
            displaying.display_book(book)
        elif cmd == "print":
            printing = PrintConsole() if method_type == "console"\
                else PrintReverse()
            printing.print_book(book)
        elif cmd == "serialize":
            serialize = SerializeJson() if method_type == "json"\
                else SerializeXml()
            return serialize.serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
