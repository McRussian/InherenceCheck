from datetime import datetime


class Logger:
    def __init__(self, filename: str):
        self.__filename = filename

    def __write_messages(self, msg: str):
        with open(self.__filename, 'a') as fin:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fin.write(f'{now} :: {msg}')

    def warning(self, msg: str):
        self.__write_messages(f'Warning: {msg}')

    def error(self, msg: str):
        self.__write_messages(f'Error: {msg}')
