import os
import sys
import logging
from logging import handlers

"""
This is the common logger configuration script for travel bot

"""

class LogFilter(logging.Filter):
    """Filters (lets through) all messages with level < LEVEL"""
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        # "<" instead of "<=": since logger.setLevel is inclusive, this should
        # be exclusive
        return record.levelno < self.level
    
#### Configure logger
LOG_FILENAME = os.getcwd()+"/smart_learning.log"
WRITE_TO_CONSOLE = True
logging.getLogger().setLevel(logging.DEBUG)

#### FILE LOGGER HANDLER
# define a Handler which writes DEBUG messages or higher to the file
fh = handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=(1048576*5), backupCount=10)
fh.setLevel(logging.DEBUG)
# set a format which is simpler for console use
f_format = logging.Formatter('%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)-30.30s:%(lineno)d]  %(message)s')
# tell the handler to use this format
fh.setFormatter(f_format)

#### CONSOLE LOGGER HANDLER
# define a Handler which writes INFO messages or higher to the sys.stderr
stdout_hdlr = logging.StreamHandler(sys.stdout)
stderr_hdlr = logging.StreamHandler(sys.stderr)
stdout_hdlr.addFilter(LogFilter(logging.WARNING))

stdout_hdlr.setLevel(logging.DEBUG if WRITE_TO_CONSOLE else logging.WARNING)
stderr_hdlr.setLevel(max(logging.DEBUG, logging.WARNING))
# messages lower than WARNING go to stdout
# messages >= WARNING (and >= STDOUT_LOG_LEVEL) go to stderr

# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s [%(levelname)-5.5s] [%(name)-20.20s:%(lineno)d] %(message)s')
# tell the handler to use this format
stdout_hdlr.setFormatter(formatter)
stderr_hdlr.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger().addHandler(stdout_hdlr)
logging.getLogger().addHandler(stderr_hdlr)
logging.getLogger().addHandler(fh)


#### Excluded libraries from LOGGING
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("quepy").setLevel(logging.WARNING)
logging.getLogger("elasticsearch").setLevel(logging.WARNING)
logging.getLogger("bs4").setLevel(logging.WARNING)