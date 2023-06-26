from logging import *

LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'

basicConfig(filename='logfile.log', format=LOG_FORMAT, filemode="w", level=INFO, style="{")

logger = getLogger("admin")

logger.info("Admin is login")
logger.warning('Admin logged out')
