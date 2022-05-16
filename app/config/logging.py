import logging

# noinspection PyArgumentList
logging.basicConfig(
    # handlers=[logging.FileHandler('log.txt', 'w', 'utf-8')],
    level=logging.INFO,
    format='{%(pathname)s:%(lineno)d} %(asctime)s - %(levelname)s - %(message)s'
)
