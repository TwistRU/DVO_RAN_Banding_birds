from sqlite3 import connect
from utils import Data
import sqlite3
import datetime


def adapt_time_iso(val: datetime.time) -> str:
    return val.isoformat()


def convert_time(val: str) -> datetime.time:
    return datetime.time.fromisoformat(val)


def setup_DB():
    sqlite3.register_converter("time", convert_time)
    sqlite3.register_adapter(datetime.time, adapt_time_iso)
    if Data.IS_DEBUG:
        Data.conn = connect("test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    else:
        Data.conn = connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    define_db_tables()


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
        DROP TABLE IF EXISTS RESULT_TABLE;
    """)
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
            tail,
            head_length,
            mesh_number,
            biotope_code,
            mesh_footage,
            check_time,
            place_of_tagging,
            latitude_of_tagging,
            longitude_of_tagging,
            molting_stage
        );
    """)
