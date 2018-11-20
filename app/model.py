import datetime

from flask import jsonify

from app.db import connect_to_database, get_sql_result_in_dict_format, set_in_db, query_one, _rollback_db, _commit_db, \
    get_cursor, execute

search_users = " SELECT * FROM users WHERE  lower(name) LIKE  '%%{0}%%'  " \
               "OR lower(nick) LIKE '%%{1}%%' ORDER BY user_id LIMIT '{2}' ; "

check_created_pers_chat = " SELECT * FROM chat WHERE  lower(name) LIKE  '%%{0}%%'  " \
                          "OR lower(nick) LIKE '%%{1}%%' ORDER BY user_id LIMIT '{2}' ; "

list_chats = "SELECT * FROM chat WHERE chat_id IN (SELECT chat_id FROM member WHERE user_id = %(user_id)s);"

search_chats = " SELECT * FROM users WHERE  lower(name) LIKE  '%%{0}%%'  " \
               "OR lower(nick) LIKE '%%{1}%%' ORDER BY user_id LIMIT '{2}' ; "


def search_users_in_db(query, limit):
    return get_sql_result_in_dict_format(search_users.format(query.lower(), query.lower(), limit))


def create_pers_chat_in_db(user_id, user_id_comp):
    chat_id = query_one("INSERT INTO chat (is_group_chat) VALUES (False) RETURNING chat_id ;")[0]
    add_member_to_chat(user_id, chat_id)
    add_member_to_chat(user_id_comp, chat_id)
    _commit_db()
    return get_sql_result_in_dict_format("""SELECT * FROM chat WHERE chat_id = %(chat_id)s ;""" , chat_id= chat_id)


def add_member_to_chat(member_id, chat_id):
    result = query_one("""
        INSERT INTO member (user_id,chat_id)
        VALUES(%(member_id)s, %(chat_id)s)
        RETURNING new_messages;
    """, member_id=int(member_id), chat_id=int(chat_id))
    return result


def list_chats_in_db(user_id):
    return get_sql_result_in_dict_format(list_chats ,  user_id=user_id)


def create_message_in_db(chat_id, user_id, content, attach_id):
    message_id = query_one("""
    INSERT INTO messages (chat_id, user_id, content)
    VALUES (%(chat_id)s, %(user_id)s, %(content)s)
    RETURNING message_id ;""", chat_id=chat_id, user_id=user_id, content=content)[0]
    # if (attach_id):
    #     execute("""
    #         INSERT INTO attachment (chat_id, user_id, message_id)
    #         VALUES (%(chat_id)s, %(user_id)s, %(message_id)s) ;""",
    #             chat_id=chat_id, user_id=user_id, message_id=message_id)

    execute("""
        UPDATE chat
        SET last_message=%(content)s
        WHERE chat_id=%(chat_id)s""", content=content, chat_id=chat_id)

    execute("""
        UPDATE member
        SET new_messages=new_messages+1
        WHERE chat_id=%(chat_id)s
        AND user_id<>%(user_id)s""", chat_id=chat_id, user_id=user_id)

    _commit_db()

    return get_sql_result_in_dict_format("""SELECT * FROM messages WHERE message_id = %(message_id)s ;""", message_id=message_id)


def read_message_in_db(message_id, user_id):
    execute("""
        UPDATE member
        SET new_messages=new_messages-1, last_read_message_id = %(message_id)s
        WHERE chat_id = (SELECT chat_id FROM messages WHERE message_id=%(message_id)s)
        AND user_id=%(user_id)s""", message_id=message_id, user_id=user_id)

    _commit_db()

    return get_sql_result_in_dict_format("""SELECT * FROM member WHERE chat_id = (SELECT chat_id FROM messages WHERE message_id=%(message_id)s)
        AND user_id=%(user_id)s""", message_id=message_id, user_id=user_id)


def list_messages_for_chat(chat_id):
    return get_sql_result_in_dict_format("""SELECT * FROM messages WHERE chat_id = %(chat_id)s ;""", chat_id = chat_id)
