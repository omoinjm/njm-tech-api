from src.core.repositories.crawler_repository_interface import ICrawlerRepository


class ICommandRepository(ICrawlerRepository):
    def __init__(self, configuration):
        self._configuration = configuration

    async def get_all_urls(self, generalSpecParams: GeneralSpecParams):
        return Pagination(
            page_index=generalSpecParams.PageIndex,
            page_size=generalSpecParams.PageSize,
            data=clients,
            count=count,
        )

