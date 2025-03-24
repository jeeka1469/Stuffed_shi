```python
import logging

# Define setup logger function to configure logger
def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    l.setLevel(level)   # Setting log level
    
    # Formatting log output
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    
    # Configuring file handler and attaching it to logger
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    l.addHandler(fileHandler)

    # Configuring stream handler and attaching it to logger
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    l.addHandler(streamHandler)

# Call function to setup logger and get reference to that logger
logger = setup_logger('log', 'log_file.log')

# Usage: logger.info('message') 
```