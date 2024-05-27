# Logging configuration for the application

import logging
import logging.config
import os

# Set the logging configuration
# Look at it at python.org/doc/2.7/library/logging.config.html
logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'logging.conf'))

# Create a logger 
logger = logging.getLogger(___name___) # __name__ is the module name -> logging.py

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Log handling
# The logging module provides a powerful and flexible logging framework.
# At its simplest, log messages are sent to a file or to sys.stderr.
# The logging system can be configured directly from Python or can be loaded from a user-defined configuration file.
# Loggers expose the interface that application code directly uses.
# Handlers send the log records (created by loggers) to the appropriate destination.
# Filters provide a finer grained facility for determining which log records to output.
# Formatters specify the layout of log records in the final output.
# The logging module is intended to be thread-safe without any special work needing to be done by its clients.
# It achieves this though using threading locks; there is one lock to serialize access to the module's shared data, and each handler also creates a lock to serialize access to its underlying I/O.

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning message')
logger.error('This is an error message')

# Output:
# 2021-07-15 15:00:00,000 - __main__ - WARNING - This is a warning message
# 2021-07-15 15:00:00,000 - __main__ - ERROR - This is an error message

# You can also set the logging configuration in a separate file.
# logging.conf
# [loggers]
# keys=root,exampleLogger

import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('exampleLogger')

logger.debug('This is a debug message')

# Very good is the python json logger library!!!!!!!!!