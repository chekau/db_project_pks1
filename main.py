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

class ListenersTable(Table):

    @staticmethod
    def add(values: dict):
        name = values["NAME"]
        age = values["age"]
        query = "INSERT INTO `Listeners` (NAME) VALUES (%s);"
        DateBase.cursor().execute(query, (name,))
        DateBase.commit()

    @staticmethod
    def get_fields_name():
        return ["NAME","age"]
    @staticmethod
    def find(values: dict):
        name = values["NAME"] if "NAME" in values else None
        age = values["age"] if "age" in values else None
        (sort_name, asc) = values["sort"] if "sort" in values else (None,None)

        limit = values["limit"] if "limit" in values else None
        params = []

        if name is not None and age is not None:
            query = "SELECT `NAME`,`age` FROM `Listeners` WHERE `NAME`=%s AND `age`=%s"
            params += [name,age]
        elif name is not None and age is None:
            query = "SELECT `NAME`,`age` FROM `Listeners` WHERE `NAME`=%s"
            params += [name]
        elif name is None and age is not None:
            query = "SELECT `NAME`,`age` FROM `Listeners` WHERE `age`=%s"
            params += [age]

        else:
            query = "SELECT `NAME`,`age` FROM `Listeners`"

        query += f" ORDER BY {sort_name} {asc};"
        print(params)
        print(query)
        DateBase.cursor().execute(query,params)
        return DateBase.cursor().fetchall()


    @staticmethod
    def delete(values: dict):
        name = values["NAME"]
        query = "DELETE FROM `Listeners` WHERE `NAME`=%s;"
        DateBase.cursor().execute(query, (name,))
        DateBase.commit()


