import sys
import datetime
from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

# Concrete Formatter: time-based
class TimeFormatter(Formatter):
    def __init__(self, time_format='%Y-%m-%d %H:%M:%S'):
        self.time_format = time_format

    def format(self, message: str) -> str:
        timestamp = datetime.datetime.now().strftime(self.time_format)
        return f"{timestamp} {message}"

# Observer: LogHandler interface
class LogHandler(ABC):
    @abstractmethod
    def handle(self, formatted_message: str):
        pass

class StreamHandler(LogHandler):
    def __init__(self, stream=sys.stderr):
        self.stream = stream

    def handle(self, formatted_message: str):
        self.stream.write(formatted_message + "\n")
        
class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler: LogHandler):
        self.handlers.append(handler)

    def log(self, message: str):
        formatted = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted)

if __name__ == "__main__":
    formatter = TimeFormatter('%Y-%m-%d %H:%M:%S')
    logger = Logger(formatter)
    logger.add_handler(StreamHandler(sys.stderr))
    logger.log("Test log message.")
