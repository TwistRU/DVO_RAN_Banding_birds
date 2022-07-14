from utils import Data


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_unique_columns_values(columns):
    cursor = Data.conn.cursor()
    query = "SELECT DISTINCT "
    for i in columns:
        query += f"{i}, "

    result = cursor.execute(query[:len(query) - 2] + " from RESULT_TABLE")

    values = []
    for i in result:
        s = ""
        for j in i:
            if j is not None:
                s += f"{j} "
        s = s[:len(s) - 1]
        if s != "":
            values.append(s)

    cursor.close()
    return values


def get_data_by_columns(pairs_col_val):
    cursor = Data.conn.cursor()
    query = "SELECT * from RESULT_TABLE WHERE"
    added = False
    for pair in pairs_col_val:
        if pair[1] != '':
            added = True
            if pair[0] != 'genus_and_species':
                if is_number(pair[1]):
                    query += f" {pair[0]} = {str(pair[1])} and"
                if pair[1] == 'None':
                    query += f" {pair[0]} IS NULL and"
                else:
                    query += f" {pair[0]} = '{pair[1]}' and"
            else:
                query += f" instr('{pair[1]}',genus) and instr('{pair[1]}',species) and"

    if added:
        query = query[:len(query) - 4]
    else:
        query = query[:len(query) - 6]

    table = cursor.execute(query)

    values = [i for i in table]

    cursor.close()
    return values
