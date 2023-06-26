from logging import *

LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'

basicConfig(filename='logfile.log', level=DEBUG, filemode="w", format=LOG_FORMAT, style="{")

debug("This is debug")
info("This is info")
warning("This is warning")
error("This is error")
critical("This is critical")
