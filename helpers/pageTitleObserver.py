# helpers/pageTitleObserver.py
from PySide6.QtCore import QObject


class PageTitleObserver(QObject):
    """
    Updates the main-window title whenever the current page changes.

    How it works
    ------------
    • Listens to QStackedWidget.currentChanged(int).
    • Tries to read a title from **either**:
        1) the page widget itself
        2) its first child widget (covers the “placeholder + controller” pattern)
        3) falls back to widget.objectName()
    • Calls `on_change(str)` with that title (pass self.setWindowTitle).

    Title sources
    -------------
    A widget may expose its title by:
        pageTitle = "Static Title"        # string attribute
    or
        def pageTitle(self) -> str: ...   # callable returning string
    """

    def __init__(self, stacked, on_change):
        super().__init__(stacked)  # parent for auto-cleanup
        self._stacked = stacked
        self._on_change = on_change

        stacked.currentChanged.connect(self._update)
        self._update(stacked.currentIndex())  # emit initial title

    # ---------- internal helpers ----------
    def _extract_title(self, widget):
        """Return title str or None."""
        if hasattr(widget, "pageTitle"):
            attr = widget.pageTitle
            if isinstance(attr, str):
                return attr
            if callable(attr):
                try:
                    return attr()
                except Exception:
                    pass
        return None

    def _update(self, index: int):
        page = self._stacked.widget(index)
        title = self._extract_title(page)

        # fallback: peek at first child (controller inside placeholder)
        if (
            title is None
            and page is not None
            and page.layout()
            and page.layout().count()
        ):
            child = page.layout().itemAt(0).widget()
            title = self._extract_title(child)

        self._on_change(title or page.objectName())
