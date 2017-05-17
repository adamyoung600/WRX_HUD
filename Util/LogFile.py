import logging


"""
LogFile

Controls intialization of the "root" logger to a file including formatting.
Other modules will be able to use the following to get a reference to the logger.

"""
class LogFile ():

    def __init__(self):

        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        fileHandler = logging.FileHandler('wrx-console.log')
        fileHanlder.setLevel(logging.DEBUG)
        fileHanlder.setFormatter(formatter)
        logger = logging.getLogger("root")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHanlder(fileHandler)
        return logger

    def getLogFile(self):
        return logging.getLogger("root")