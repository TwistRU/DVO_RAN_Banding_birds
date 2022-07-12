import xlrd, openpyxl

from utils import Data


def load_tables_to_DB(files: list) -> list:
    """
    return Erros. If errors are empty, then load is successful.
    files[0] - Таблица результатов мечения
    files[1] - Таблица дат работ
    files[2] - Таблица координат работ
    """
    errors = []
    result_table = openpyxl.open(files[0])
    result_sheet = result_table.active
    return errors
