import sys
from datetime import datetime, timedelta, timezone


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
        self.is_new_line = True

    def write(self, message):
        current_time = datetime.now(timezone(timedelta(hours=8)))
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        if self.is_new_line:
            self.terminal.write(formatted_time + " -> ")
            self.log.write(formatted_time + " -> ")
            self.is_new_line = False
        self.terminal.write(message)
        self.log.write(message)
        if message == "\n":
            self.is_new_line = True

    def flush(self):
        pass


if __name__ == '__main__':
    sys.stdout = Logger("test")
    print("测试")
    print("测试")
    print("测试")
    print("测试")
    # log.write("测试")
    # log.write("测试")
    # log.write("测试")
