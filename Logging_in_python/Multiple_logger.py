import logging

"""Create logger for module 1"""
logger1 = logging.getLogger('Module_1')
logger1.setLevel(logging.DEBUG)

""" Create logger for module 2 """
logger2 = logging.getLogger('Module_2')
logger2.setLevel(logging.WARNING)

"""Configure logging settings"""
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

"""Log message with different loggers"""
logger1.debug('This is the debug msg for logger1')
logger2.warning('This is the warning msg for logger2')
logger2.error('This is the error msg for logger2')


