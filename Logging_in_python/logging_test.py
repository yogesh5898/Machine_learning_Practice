import logging

""" Configure basic logging settings """
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

""" Log message with different severity level"""
logging.debug('This is debug msg')
logging.warning('This is warning msg')
logging.error('This is error msg')
logging.info('This is info msg')
logging.critical('This is critical msg')


""" Configuring Logging """
