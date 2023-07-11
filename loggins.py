from selenium import webdriver

import logging

# Create and Configure Logger

logging.basicConfig(filename="Batch10.txt", format='%(asctime)s %(levelname)s %(message)s', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.error("This is debug message!")
logger.info("This is info message!")
logger.debug("This is warning message!")
logger.warning("This is error message!")
logger.critical("This is critical message!")
