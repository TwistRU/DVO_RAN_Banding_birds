from utils import Data
from database.db_dicts import dict_result_table


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

    values = set()
    for i in result:
        s = ""
        for j in i:
            if j is not None:
                s += f"{j} "
        s = s[:len(s) - 1]
        if s != "":
            values.add(s)

    cursor.close()
    return list(values)


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
                else:
                    query += f" {pair[0]} = '{pair[1]}' and"
            else:
                query += f" instr('{pair[1]}',genus) and instr('{pair[1]}',species) and"

    if added:
        query = query[:len(query) - 4]
    else:
        query = query[:len(query) - 6]

    table = cursor.execute(query)
    values = [list(i) for i in table]
    values.insert(0, list(dict_result_table.values()))

    cursor.close()
    return values


def morphology_selector(genus_and_species):
    columns = ['№ кольца', 'Год отлова', 'Пол', 'Возраст EURING', '% пневматизации', 'Вес', 'Клюв от лба',
               'Клюв от ноздри', 'Крыло min', 'Крыло max', 'Цевка', 'Хвост', 'Длина головы', '№ сетки']

    query = "SELECT ring, strftime('%Y', date_of_capture_in_season) as year_of_capture, " \
            "gender, age_EURING, pneumatization, weight, beak_from_forehead, beak_from_nostril, " \
            "wing_min, wing_max, tarsus, tail, head_length, mesh_number FROM RESULT_TABLE " \
            f"WHERE instr('{genus_and_species}', genus) AND instr('{genus_and_species}', species)"

    cursor = Data.conn.cursor()

    table = cursor.execute(query)
    values = [list(i) for i in table]
    values.insert(0, columns)

    cursor.close()
    return values
