""" Storage Module """

from enum import Enum
import pymongo


class Databases(Enum):
    """ Supported Databases """
    Mongo = 1


class Mongo:
    """ MongoDB Storage """

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.client = pymongo.MongoClient(
                "mongodb+srv://" +
                user +
                ":" +
                password +
                "@" +
                "<cluster-url>/" +
                "test?retryWrites=true&w=majority")

    def store(self, obj):
        """ Save the data """
        print(obj)


class Storage:
    """ Storage Class """
    def __init__(self, user, password, db_type):
        self.user = user
        self.password = password
        self.type = db_type
        self._last_type = db_type
        self.driver = None

        self.set_driver()

    def is_valid(self):
        """ Return True if this object is valid """
        if not self.user or not self.password:
            print('Required storage user and password.')
            return False
        return True

    def set_driver(self):
        """ Generates the corresponding storage method """
        if str(self.type).lower() == 'mongo':
            self.driver = Mongo(self.user, self.password)
            self._last_type = self.type

    def attach(self, obj):
        """ Stores new information in some source """
        if not self.is_valid():
            return

        if self._last_type != self.type:
            self.set_driver()

        self.driver.store(obj)
