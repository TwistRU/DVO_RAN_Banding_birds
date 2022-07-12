from sqlite3 import connect

from utils import Data


def setup_DB():
    if Data.IS_DEBUG:
        Data.conn = connect("test.db")
    else:
        Data.conn = connect(":memory:")

def define_db_tables():
    """
    C - ring -                      № кольца\n
    D - date_of_capture_in_season - Дата отлова в сезон\n
    E - date_of_tagging -           Дата мечения\n
    F - returns -                   Возвраты\n
    G - date_of_return -            Дата возврата\n
    H - date_of_death -             Дата гибели\n
    I - genus -                     Род\n
    J - species -                   Вид\n
    N - gender -                    Пол\n
    O - age_EURING -                Возраст EURING\n
    P - age -                       Возвраст\n
    Q - pneumatization -            % пневматизации\n
    R - richness -                  Балл жирности\n
    S - muscle -                    Балл мышцы\n
    T - weight -                    Вес\n
    U - beak_from_forehead -        Клюв от лба\n
    V - beak_from_nostril -         Ключ от ноздри\n
    W - wing_min -                  Крыло min\n
    X - wing_max -                  Крыло max\n
    Y - tarsus -                    Цевка\n
    AA - tail -                     Хвост\n
    AC - head_length -              Длина головы\n
    AD - mesh_number -              № сетки\n
    AF - biotope_code -             Код биотопа\n
    AI - mesh_footage -             Метраж сетей\n
    AK - check_time -               Время проверки\n
    AO - place_of_tagging -         Место мечения\n
    AR - latitude_of_tagging -      Широта мечения\n
    AS - longitude_of_tagging -     Долгото мечения\n
    CI - molting_stage -            Стадия линьки\n
    """
    Data.conn.execute("""
    CREATE TABLE IF NOT EXISTS RESULT_TABLE ( 
        ring,
        date_of_capture_in_season,
        date_of_tagging,
        returns,
        date_of_return,
        date_of_death,
        genus,
        species,
        latin_name,
        rus_name,
        count_of_birds,
        gender,
        age_EURING,
        age,
        pneumatization,
        richness,
        muscle,
        weight,
        beak_from_forehead,
        beak_from_nostril,
        wing_min,
        wing_max,
        tarsus,
        tarsus2,
        tail,
        tail_rast,
        head_length,
        mesh_number,
        mesh_number2,
        biotope_code,
        number_of_networks_small,
        number_of_networks_drozd_big,
        network_footage,
        relative_population,
        check_time,
        weather,
        notes,
        collection,
        place_of_tagging,
        place_of_return,
        tagger,
        latitude_of_tagging,
        longitude_of_tagging,
        body_length,
        belly_length,
        beak_from_corners_of_mouth,
        beak_height,
        beak_width,
        beak_width_at_nostril_level,
        beak_height_at_nostril_level,
        wing_tip,
        AI_bigger_than_BVKPM,
        AI_smaller_than_BVKPM
    )
    """)

