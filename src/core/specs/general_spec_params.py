class GeneralSpecParams:
    max_page_size = 10

    def __init__(self):
        self.page_index = 1
        self._page_size = 5
        self.command = ""

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = min(value, self.max_page_size)

