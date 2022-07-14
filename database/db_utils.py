import openpyxl

from utils import Data


def load_tables_to_DB(files: list, progress_callback, max_progress_callback) -> list:
    """
    return Errors. If errors are empty, then load is successful.
    files[0] - Таблица результатов мечения
    files[1] - Таблица дат работ
    files[2] - Таблица координат работ
    """
    errors = []
    # Таблица результатов мечения
    columns_from_tagging_table = ["C", "D", "E", "F", "G", "H", "I", "J", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "AA", "AC", "AD", "AF", "AI", "AK", "AO", "AR", "AS", "CI"]
    result_table = openpyxl.open(files[0], data_only=True)
    result_sheet = result_table.active
    max_progress_callback.emit (result_sheet.max_column)
    result_columns = [result_sheet[column_name] for column_name in columns_from_tagging_table]
    result = list()
    for i in range(len(result_sheet["A"])):
        tmp = []
        for column in result_columns:
            tmp.append(column[i].value)
        result.append(tuple(tmp))
        progress_callback.emit()
    Data.conn.executemany("""
    INSERT INTO RESULT_TABLE VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
    """, result[1:])
    Data.conn.commit()
    # Таблица дат работ
    columns_from_dates_table = ["A", "B", "C"]
    dates_table = openpyxl.open(files[1], data_only=True)
    dates_sheet = dates_table.active
    dates_columns = [dates_sheet[column_name] for column_name in columns_from_dates_table]
    dates = list()
    for i in range(len(dates_sheet["A"])):
        tmp = []
        for column in dates_columns:
            tmp.append(column[i].value)
        dates.append(tuple(tmp))
        progress_callback.emit()
    Data.conn.executemany("""
    INSERT INTO DATES_OF_WORK VALUES (?, ?, ?);
    """, dates[1:])
    Data.conn.commit()
    # Таблица координат работ
    columns_from_coordinates_table = ["A", "B", "C", "D", "E", "F"]
    coordinates_table = openpyxl.open(files[2], data_only=True)
    coordinates_sheet = coordinates_table.active
    coordinates_columns = [coordinates_sheet[column_name] for column_name in columns_from_coordinates_table]
    coordinates = list()
    for i in range(len(coordinates_sheet["A"])):
        tmp = []
        for column in coordinates_columns:
            tmp.append(column[i].value)
        coordinates.append(tuple(tmp))
        progress_callback.emit()
    Data.conn.executemany("""
    INSERT INTO COORDINATES_OF_WORK VALUES (?, ?, ?, ?, ?, ?)
    """, coordinates[1:])
    Data.conn.commit()
    return errors
