from Multicaster import Multicaster
import logging

sender=Multicaster('224.0.0.1','55555')
sender.logger.logger.setLevel(logging.DEBUG)
sender.send()

