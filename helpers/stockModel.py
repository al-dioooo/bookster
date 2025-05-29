from typing import Dict, List
from helpers.dataReader import DataReader


class StockModel:
    """CRUD helper for stocks.json"""

    def __init__(self, path: str = "data/stocks.json"):
        self.reader = DataReader(path)

    # ---------- read ----------
    def all(self) -> List[Dict]:
        return self.reader.get()

    # ---------- upsert (replace all rows for an ISBN) ----------
    def replace_for_isbn(self, isbn: str, new_rows: List[Dict]):
        rows = [r for r in self.all() if r["isbn"] != isbn] + new_rows
        self.reader.clearData()
        for r in rows:
            self.reader.addItem(r)
        self.reader.saveData()
