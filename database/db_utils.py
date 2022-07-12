import xlrd, openpyxl

from utils import Data


def load_tables_to_DB(files: list) -> list:
    """
    return Erros. If errors are empty, then load is successful.
    files[0] - Таблица результатов мечения
    files[1] - Таблица дат работ
    files[2] - Таблица координат работ
    """
    columns_from_table = ["C", "D", "E", "F", "G", "H", "I", "J", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "AA", "AC", "AD", "AF", "AI", "AK", "AO", "AR", "AS", "CI"]
    errors = []
    result_table = openpyxl.open(files[0])
    result_sheet = result_table.active
    result_columns = [result_sheet[column_name] for column_name in columns_from_table]
    result = list()
    for i in range(len(result_sheet["A"])):
        tmp = []
        for column in result_columns:
            tmp.append(column[i])
        result.append(tuple(tmp))
    Data.conn.executemany(f"""
    insert into RESULT_TABLE values ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?");
    """, result[1:])
    Data.conn.commit()
    return errors
