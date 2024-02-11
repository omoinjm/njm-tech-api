class Pagination:
    def __init__(
        self,
        page_index,
        page_size,
        count,
        data,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.count = count
        self.data = data
