from typing import Dict, List
from helpers.dataReader import DataReader


class UserModel:
    """CRUD wrapper for data/users.json."""

    def __init__(self, path: str = "data/users.json"):
        self.reader = DataReader(path)

    # ---------- read ----------
    def all(self) -> List[Dict]:
        return self.reader.get()

    # ---------- helper ----------
    def _rewrite(self, rows: List[Dict]):
        self.reader.clearData()
        for r in rows:
            self.reader.addItem(r)
        self.reader.saveData()

    # ---------- upsert (by id) ----------
    def upsert(self, record: Dict):
        uid = record["id"]
        rows = self.all()
        for i, row in enumerate(rows):
            if row["id"] == uid:
                rows[i] = record
                self._rewrite(rows)
                return
        rows.append(record)
        self._rewrite(rows)

    # ---------- delete ----------
    def delete(self, uid: int):
        self._rewrite([r for r in self.all() if r["id"] != uid])

    # ---------- next id ----------
    def next_id(self) -> int:
        ids = [r["id"] for r in self.all()]
        return max(ids, default=0) + 1
