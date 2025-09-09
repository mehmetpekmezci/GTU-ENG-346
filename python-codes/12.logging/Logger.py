import logging
import os
import datetime
import time

class Logger :
    def __init__(self,appName):

        SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))
        SCRIPT_NAME=os.path.basename(SCRIPT_DIR)
        LOG_DIR=SCRIPT_DIR+"/log"
        RECORD_TIMESTAMP=str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y.%m.%d_%H.%M.%S'))

        if not os.path.exists(LOG_DIR):
           os.makedirs(LOG_DIR)

        ## CONFUGRE LOGGING
        self.logger=logging.getLogger(appName)
        self.logger.setLevel(logging.INFO)
        #logger.setLevel(logging.DEBUG)
        # create file handler and set level to debug
        loggingFileHandler = logging.FileHandler(LOG_DIR+'/'+appName+'-'+RECORD_TIMESTAMP+'.log')
        loggingFileHandler.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        loggingConsoleHandler = logging.StreamHandler()
        loggingConsoleHandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        loggingFileHandler.setFormatter(formatter)
        loggingConsoleHandler.setFormatter(formatter)
        self.logger.addHandler(loggingFileHandler)
        self.logger.addHandler(loggingConsoleHandler)

    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)


