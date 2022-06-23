import logging
import logstash
import sys


class Logging(object):
    def __init__(self, logger_name='python-logger',
                 log_stash_host='localhost',
                 log_stash_upd_port=5959

                 ):
        self.logger_name = logger_name
        self.log_stash_host = log_stash_host
        self.log_stash_upd_port = log_stash_upd_port


    def get(self):
        logging.basicConfig(
            filename="logfile",
            filemode="a",
            format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )

        self.stderrLogger = logging.StreamHandler()
        logging.getLogger().addHandler(self.stderrLogger)
        self.logger = logging.getLogger(self.logger_name)
        self.logger.addHandler(logstash.LogstashHandler(self.log_stash_host,
                                                        self.log_stash_upd_port,
                                                        version=1))
        return self.logger



instance = Logging(log_stash_upd_port=5959, log_stash_host='localhost', logger_name='soumil')
logger = instance.get()

count = 0
from time import sleep
while True:

    count = count + 1

    if count % 2 == 0:
        logger.error('Error Message Code Faield :{} '.format(count))
    else:
        logger.info('python-logstash: test logstash info message:{} '.format(count))

