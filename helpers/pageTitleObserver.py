class PageTitleObserver:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def update(self, pageName):
        # Map page names to corresponding titles
        titles = {
            "startPage": "Welcome - Bookster",
            "loginPage": "Login - Bookster",
            "dashboardPage": "Dashboard - Bookster",
            "bookManagementPage": "Book Management - Bookster",
            "userManagementPage": "User Management - Bookster",
        }

        # Default title
        title = titles.get(pageName, "Bookster")
        self.mainWindow.setWindowTitle(title)
