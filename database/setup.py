from sqlite3 import connect
from utils import Data
import sqlite3
import datetime


def adapt_time_iso(val: datetime.time) -> str:
    return val.isoformat()


def convert_time(val: str) -> datetime.time:
    return datetime.time.fromisoformat(val)


def setup_DB() -> bool:
    sqlite3.register_converter("time", convert_time)
    sqlite3.register_adapter(datetime.time, adapt_time_iso)
    Data.conn = connect("database.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                        check_same_thread=False)
    exists = Data.conn.execute("""
    SELECT COUNT(1) FROM RESULT_TABLE;
    """).fetchone()[0] > 0
    if not exists: define_db_tables()
    return exists


def define_db_tables():
    """
    RESULT_TABLE
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
        AS - longitude_of_tagging -     Долгота мечения\n
        CI - molting_stage -            Стадия линьки\n
    DATES_OF_WORK
        A - place_of_tagging -          Место мечения\n
        B - start_date -                Дата начала работ\n
        C - end_date -                  Дата завершения работ\n
    COORDINATES_OF_WORK
        A - country_code -              Код страны\n
        B - counrty_name -              Страна\n
        C - region_name -               Регион\n
        D - place_of_tagging -          Место мечения\n
        E - latitude_of_tagging -       Широта\n
        F - longitude_of_tagging -      Долгота\n
    """
    Data.conn.execute("""
        DROP TABLE IF EXISTS RESULT_TABLE;
    """)
    Data.conn.execute("""
        DROP TABLE IF EXISTS DATES_OF_WORK;
    """)
    Data.conn.execute("""
        DROP TABLE IF EXISTS COORDINATES_OF_WORK;
    """)
    Data.conn.execute("""
        CREATE TABLE DATES_OF_WORK (
            place_of_tagging,
            start_date,
            end_date
        );
    """)
    Data.conn.execute("""
        CREATE TABLE COORDINATES_OF_WORK (
            country_code,
            country_name,
            region_name,
            place_of_tagging,
            latitude_of_tagging,
            longitude_of_tagging
        );
    """)
    Data.conn.execute("""
        CREATE TABLE RESULT_TABLE ( 
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
