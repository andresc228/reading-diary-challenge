from datetime import datetime

class Note:

    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        else:
            new_notes = Note(text, page, date)
            self.notes.append(new_notes)
            return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        note_pages = []

        for note in self.notes:
            if note.page == page:
                note_pages.append(note)

        return note_pages

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        pages_count = {}

        for note in self.notes:
            if note.page in pages_count:
                pages_count[note.page] += 1
            else:
                pages_count[note.page] = 1

        return max(pages_count, key=pages_count.get)

    def __str__(self) -> str:

        if self.rating == Book.EXCELLENT:
            rating_str = "excellent"
        elif self.rating == Book.GOOD:
            rating_str = "good"
        elif self.rating == Book.BAD:
            rating_str = "bad"
        else:
            rating_str = "unrated"

        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nRating: {rating_str}"


from datetime import datetime


class ReadingDiary:

    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False

        self.books[isbn] = Book(isbn, title, author, pages)
        return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)

        if book is None:
            return False

        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Book | None:
        if not self.books:
            return None

        max_notes = 0
        book_result = None

        for book in self.books.values():
            notes_count = len(book.notes)

            if notes_count > max_notes:
                max_notes = notes_count
                book_result = book

        if max_notes == 0:
            return None

        return book_result

