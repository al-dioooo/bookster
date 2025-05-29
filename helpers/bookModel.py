# pages/bookManagement/bookModel.py
"""
Model pembungkus DataReader untuk buku.
- Menyimpan file JSON berisi list buku
- Menyediakan add / update / delete / upsert / getAll
"""

from typing import Dict, List
from helpers.dataReader import DataReader


class BookModel:
    def __init__(self, path: str = "data/books.json"):
        self.reader = DataReader(path)

    # ---------- read ----------
    def getAll(self) -> List[Dict]:
        """Return seluruh list buku (dict)."""
        return self.reader.get()

    # ---------- internal helper ----------
    def _writeAll(self, books: List[Dict]):
        """Timpa file JSON secara atomik dengan list baru."""
        self.reader.clearData()  # kosongkan isi file
        for item in books:
            self.reader.addItem(item)  # tulis lagi satu-persatu
        self.reader.saveData()  # pastikan flush

    # ---------- add ----------
    def add(self, record: Dict):
        """Tambahkan buku baru (tidak cek duplikat)."""
        self.reader.addItem(record)
        self.reader.saveData()

    # ---------- update ----------
    def update(self, isbn: str, record: Dict) -> bool:
        """
        Ganti item yang ISBN-nya cocok.
        Return True jika ditemukan & diganti; False jika tidak ada.
        """
        books = self.getAll()
        for idx, item in enumerate(books):
            if item.get("isbn") == isbn:
                books[idx] = record
                self._writeAll(books)
                return True
        return False

    # ---------- delete ----------
    def delete(self, isbn: str):
        """Hapus buku berdasarkan ISBN."""
        books = [b for b in self.getAll() if b.get("isbn") != isbn]
        self._writeAll(books)

    # ---------- upsert ----------
    def upsert(self, isbn: str, record: Dict):
        """
        Jika ISBN sudah ada → update, jika belum ada → add.
        """
        if not self.update(isbn, record):  # update() return False bila tak ditemukan
            self.add(record)
