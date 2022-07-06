from sqlite3 import connect

from utils import Data


def setup_DB():
    if Data.IS_DEBUG:
        Data.conn = connect("test.db")
    else:
        Data.conn = connect(":memory:")



