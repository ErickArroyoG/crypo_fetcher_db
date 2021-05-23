""" Storage Module """

from enum import Enum
import pymongo


class Databases(Enum):
    """ Supported Databases """
    Mongo = 1


class Mongo:
    """ MongoDB Storage """

    def __init__(self, user, password, cluster, database):
        # self.user = user
        # self.password = password
        if not cluster:
            print("\nRequired MongoDB param \"cluster\" " +
                  "in var \"PBA_DB_PARAMS\"!\n")
            return

        url = "mongodb+srv://" + \
              user + \
              ":" + \
              password + \
              "@" + \
              cluster + \
              "/" + \
              database + \
              "?retryWrites=true&w=majority"

        self.client = pymongo.MongoClient(url)

    def store(self, obj):
        """ Save the data """
        print(self.client.crypto.btc_mx.insert_one({
             'ask': str(obj.ask),
             'bid': str(obj.bid),
             'high': str(obj.high),
             'last': str(obj.last),
             'low': str(obj.low),
             'created:_at': obj.created_at,
             'vwap': str(obj.vwap)}).inserted_id)


class Storage:
    """ Storage Class """
    def __init__(self, user, password, database, db_type, params):
        self.user = user
        self.password = password
        self.database = database
        self.type = db_type
        self._last_type = db_type
        self.params = {}
        self.driver = None

        self.fill_params(params)
        self.set_driver()

    def fill_params(self, params):
        """ Set the param object """
        for prm in params.split(','):
            param = prm.split('=')
            self.params[param[0]] = param[1]

    def is_valid(self):
        """ Return True if this object is valid """
        if not self.user or not self.password:
            print('Required storage user and password.')
            return False
        return True

    def set_driver(self):
        """ Generates the corresponding storage method """
        if str(self.type).lower() == 'mongo':
            self.driver = Mongo(
                    self.user,
                    self.password,
                    self.params.get('cluster'),
                    self.database)
            self._last_type = self.type

    def attach(self, obj):
        """ Stores new information in some source """
        if not self.is_valid():
            return

        if self._last_type != self.type:
            self.set_driver()

        self.driver.store(obj)
