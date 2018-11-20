## -*- coding: utf-8 -*-
import flask
import psycopg2

import app
import config
import blinker


def connect_to_database():
    """Connection to DB and cash this connection"""
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            database=config.DB_NAME, host=config.DB_HOST,
            user=config.DB_USER, password=config.DB_PASS)
    return flask.g.dbconn


def _rollback_db():
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')


flask.got_request_exception.connect(_rollback_db, app)


def set_in_db(sql, *args):
    curs = get_cursor()
    curs.execute(sql, args)
    _commit_db()


def _commit_db():
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.commit()
        conn.close()
        delattr(flask.g, 'dbconn')


flask.request_finished.connect(_commit_db, app)


def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)

        return cur.fetchone()


def execute(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)




def get_cursor():
    return connect_to_database().cursor()


def get_sql_result_in_dict_format(sql, **args):
    curs = get_cursor()
    curs.execute(sql, args)

    columns = [column[0] for column in curs.description]
    results = []
    for row in curs.fetchall():
        results.append(dict(zip(columns, row)))
    return results
