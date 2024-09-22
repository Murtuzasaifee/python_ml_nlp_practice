from logger import logging

logger = logging.getLogger("Custom Name")

def add(a,b):
    logger.debug(f"Adding {a} and {b}")
    return a+b


add(10,28)
logger.info("Finished adding")