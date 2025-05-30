from collections import deque
from datetime import date
from typing import Deque, Dict, List
from helpers.dataReader import DataReader


class LendModel:
    """
    FIFO + O(1) index by SKU.
    Each record schema:
      {sku,isbn,title,author,cover,user,borrowed,due,status('borrowed'|'returned'),returned?}
    """

    def __init__(self, path="data/lends.json", max_len=5000):
        self.reader = DataReader(path)
        self.max_len = max_len
        self._queue: Deque[Dict] = deque(self.reader.get(), maxlen=max_len)
        self._index: Dict[str, Dict] = {r["sku"]: r for r in self._queue}

    # ------------- internal -------------
    def _flush(self):
        self.reader.clearData()
        for r in self._queue:
            self.reader.addItem(r)
        self.reader.saveData()

    # ------------- public -------------
    def borrow(self, rec: Dict):
        sku = rec["sku"]
        if sku in self._index:
            raise ValueError("SKU already borrowed")

        if len(self._queue) == self.max_len:
            old = self._queue.popleft()
            self._index.pop(old["sku"], None)

        self._queue.append(rec)
        self._index[sku] = rec
        self._flush()

    def return_book(self, sku: str, day: str | None = None):
        r = self._index.get(sku)
        if not r:
            raise KeyError("not found")
        r["status"] = "returned"
        r["returned"] = day or date.today().isoformat()
        self._flush()

    def all(self) -> List[Dict]:
        return list(reversed(self._queue))

    def search(self, key: str) -> List[Dict]:
        k = key.lower()
        return [
            r
            for r in self.all()
            if k in r["title"].lower()
            or k in r["author"].lower()
            or k in r["isbn"].lower()
            or k in r["sku"].lower()
            or k in r.get("user", "").lower()
        ]
