from typing import List
from src.core.specs.pagination import Pagination
from src.core.specs.general_spec_params import GeneralSpecParams
from src.core.entities.crawler import Crawler


class ICrawlerRepository:
    async def get_all_urls(self, general_spec_params: GeneralSpecParams):
        pass
