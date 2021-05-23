#!venv/bin/python3
""" Script to fetch BTC price """

from os import environ
from time import sleep
from storage import Storage
import bitso


ENVS = {
        'user': {
            'val': None,
            'name': 'PBA_KEY'},
        'pass': {
            'val': None,
            'name': 'PBA_PASS'},
        'delay': {
            'val': 10,
            'name': 'PBA_DELAY'},
        'db_type': {
            'val': 'mongo',
            'name': 'PBA_DB_TYPE'},
        'db_user': {
            'val': None,
            'name': 'PBA_DB_USR'},
        'db_pass': {
            'val': None,
            'name': 'PBA_DB_PASS'},
        'db_name': {
            'val': None,
            'name': 'PBA_DB_NAME'},
        'db_params': {
            'val': '',
            'name': 'PBA_DB_PARAMS'},
}

for k in ENVS:
    ENVS[k]['val'] = environ.get(ENVS[k]['name']) or ENVS[k]['val']


def main(envs):
    """ Main function """

    missing_envs = ', '.join([
        envs[v]['name'] for v in envs if not envs[v]['val']
    ])

    if missing_envs:
        print(
                'Enviroment variables required: ' +
                missing_envs
        )
        return

    for key in envs:
        envs[key] = envs[key]['val']

    api = bitso.Api(envs['user'], envs['pass'])
    store = Storage(
            envs['db_user'],
            envs['db_pass'],
            envs['db_name'],
            envs['db_type'],
            envs['db_params'])

    # books = api.available_books()

    #  for book in books.books:
    #      if book.find('mxn') != -1:
    #          print(book)

    #  if books.index .find(btnBook):
    #      print(books[btnBook])

    # btcBook = books.btc_mxn
    # api.balances().btc.available

    while True:
        btc = api.ticker("btc_mxn")
        store.attach(btc)
        sleep(envs['delay'])


main(ENVS)
