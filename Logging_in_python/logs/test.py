from logger import logging
def add(a,b):
    logging.info("Addition operation taking place")
    return a + b


logging.debug('Add function is about to call now')
add(10, 7)
