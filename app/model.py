from flask import jsonify

from app.db import connect_to_database, get_sql_result_in_dict_format, set_in_db, query_one, _rollback_db, _commit_db, \
    get_cursor

search_users = " SELECT * FROM users WHERE  lower(name) LIKE  '%%{0}%%'  " \
               "OR lower(nick) LIKE '%%{1}%%' ORDER BY user_id LIMIT '{2}' ; "


check_created_pers_chat = " SELECT * FROM chat WHERE  lower(name) LIKE  '%%{0}%%'  " \
                          "OR lower(nick) LIKE '%%{1}%%' ORDER BY user_id LIMIT '{2}' ; "

list_chats = "SELECT * FROM chat WHERE chat_id IN (SELECT chat_id FROM member WHERE user_id = '%s');"


def search_users_in_db(query, limit):
    return get_sql_result_in_dict_format(search_users.format(query.lower(), query.lower(), limit))


def create_pers_chat_in_db(user_id, user_id_comp):
    chat_id = query_one("INSERT INTO chat (is_group_chat) VALUES (False) RETURNING chat_id")[0]
    add_member_to_chat(user_id,chat_id)
    add_member_to_chat(user_id_comp,chat_id)
    _commit_db()
    return 'Created chat have chat_id = ' + str(chat_id)


def add_member_to_chat(member_id, chat_id):
    result = query_one("""
        INSERT INTO member (user_id,chat_id)
        VALUES(%(member_id)s, %(chat_id)s)
        RETURNING new_messages;
    """, member_id=int(member_id), chat_id=int(chat_id))
    return result


def list_chats_in_db(user_id):
    return get_sql_result_in_dict_format(list_chats % user_id)
