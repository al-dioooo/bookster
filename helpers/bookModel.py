from helpers.fileHelper import JsonFileHelper


class BookModel:
    def __init__(self, jsonPath="data/books.json"):
        self.file = JsonFileHelper(jsonPath)
        self.books = []
        self.load()

    def load(self):
        data = self.file.read()
        # If empty JSON object {}, convert to empty list []
        self.books = data if isinstance(data, list) else []

    def save(self):
        self.file.write(self.books)

    def getAll(self):
        return self.books

    def getById(self, bookId):
        return next((book for book in self.books if book["id"] == bookId), None)

    def add(self, bookData):
        bookData["id"] = self._generateId()
        self.books.append(bookData)
        self.save()
        return bookData

    def update(self, bookId, newData):
        for book in self.books:
            if book["id"] == bookId:
                book.update(newData)
                self.save()
                return book
        return None

    def delete(self, bookId):
        originalLen = len(self.books)
        self.books = [book for book in self.books if book["id"] != bookId]
        if len(self.books) < originalLen:
            self.save()
            return True
        return False

    def _generateId(self):
        existing_ids = [book.get("id", 0) for book in self.books]
        return max(existing_ids, default=0) + 1
