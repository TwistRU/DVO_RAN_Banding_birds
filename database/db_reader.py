from utils import Data


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_unique_column_values(column):
    cursor = Data.conn.cursor()
    column = cursor.execute(f"""SELECT DISTINCT {column} from RESULT_TABLE""")
    values = [str(i[0]) for i in column]

    cursor.close()
    return values


def get_data_by_columns(pairs_col_val):
    cursor = Data.conn.cursor()
    query = "SELECT * from RESULT_TABLE WHERE"
    added = False
    for pair in pairs_col_val:
        if pair[1] != '':
            added = True
            if is_number(pair[1]):
                query += f" {pair[0]} = {str(pair[1])} and"
            else:
                query += f" {pair[0]} = '{pair[1]}' and"

    if added:
        table = cursor.execute(query[:len(query) - 4])
    else:
        table = cursor.execute(query[:len(query) - 6])

    values = [i for i in table]

    cursor.close()
    return values
