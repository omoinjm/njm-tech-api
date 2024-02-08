# controllers/__init__.py
from src.api.controllers.api_controller import ApiController
from src.api.controllers.crawler_controller import CrawlerController, crawler

# Create an array of hashmaps
blueprint_array = [
    {"instance": CrawlerController, "blueprint": crawler},
]

