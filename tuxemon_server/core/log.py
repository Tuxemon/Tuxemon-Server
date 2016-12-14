import os
import sys
import logging
from tuxemon_server.core import prepare

# Set our logging levels
LOG_LEVELS = {"debug": logging.DEBUG,
              "info": logging.INFO,
              "warning": logging.WARNING,
              "error": logging.ERROR,
              "critical": logging.CRITICAL}
loggers = {}

if prepare.CONFIG.debug_level in LOG_LEVELS:
    log_level = LOG_LEVELS[prepare.CONFIG.debug_level]
else:
    log_level = logging.INFO

# Set up logging if the configuration has it enabled
if prepare.CONFIG.debug_logging == "1":

    for logger_name in prepare.CONFIG.loggers:

        # Enable logging
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        log_hdlr = logging.StreamHandler(sys.stdout)
        log_hdlr.setLevel(logging.DEBUG)
        log_hdlr.setFormatter(logging.Formatter("%(asctime)s - %(name)s - "
                                                "%(levelname)s - %(message)s"))
        logger.addHandler(log_hdlr)

        loggers[logger_name] = logger


