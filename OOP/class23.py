from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        print("Here is the read abstract stream")


class FileStream(Stream):
    def read(self):
        print("Reading data from a file stream.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network stream.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


stream = FileStream()
stream.open()
