import mysql.connector
from abc import ABC


class DateBase:
    __cursor = None
    __connection = None

    @classmethod
    def connect(cls):
        cls.__connection = mysql.connector.connect(
            host="109.206.169.221",
            user="seschool_01",
            password="seschool_01",
            database="seschool_01"
        )

        cls.__cursor = cls.__connection.cursor()

    @classmethod
    def cursor(cls):
        return cls.__cursor

    @classmethod
    def commit(cls):
        cls.__connection.commit()


class Table(ABC):
    @staticmethod
    def add(values: dict):
        pass
    @staticmethod
    def get_fields_name():
        pass
    @staticmethod
    def find(values: dict):
        pass
    @staticmethod
    def delete(values: dict):
        pass