"""Controllers"""
from flask import request, jsonify
from app import app, jsonrpc
import json
from app.model import search_users_in_db, list_chats_in_db, create_pers_chat_in_db, create_message_in_db, \
    list_messages_for_chat, read_message_in_db



@jsonrpc.method('login')
def login():
    """ login controller"""
    pass


@jsonrpc.method('search_users', validate=True)
def search_users(query, limit):
    """ search-users controller"""
    response = jsonify({"users": search_users_in_db(query, limit)})
    return response


@jsonrpc.method('search_chats', validate=True)
def search_chats(query, limit):
    """ search-chats controller"""

    # SELECT FROM DATABASE

    chat1 = {
        "chat_id": 22,
        "is_group_chat": False,
        "topic": "Clint Eastwood",
        "last_message": "asfgg",
        "new_messages": 39,
        "last_read_message_id": 214
    }
    chat2 = {
        "chat_id": 242,
        "is_group_chat": False,
        "topic": "wood",
        "last_message": "gg",
        "new_messages": 3,
        "last_read_message_id": 21
    }

    response = jsonify({"chats": [chat1, chat2]})
    response.mimetype = 'application/json'
    response.status_code = 200
    return response


@jsonrpc.method('list_chats', validate=True)
def list_chats():
    """list_chats controller"""
    user_id = 2
    # user_id = request.cookies.get('user_id')
    response = jsonify({"chats": list_chats_in_db(user_id)})
    return response


@jsonrpc.method('create_pers_chat', validate=True)
def create_pers_chat(user_id):
    """create_pers_chat controller"""
    my_user_id = 1
    # my_user_id = request.cookies.get('user_id')

    response = jsonify({"chat": create_pers_chat_in_db(user_id, my_user_id)})

    return response


@jsonrpc.method('create_group_chat', validate=True)
def add_members_to_group_chat(chat_id, user_ids):
    """add_members_to_group_chat controller"""

    # ADD IN CHAT IN DATABASE

    response = jsonify({})
    return response


@jsonrpc.method('leave_group_chat', validate=True)
def leave_group_chat(chat_id):
    """leave_group_chat controller"""

    # LEAVE CHAT IN DATABASE

    response = jsonify({})
    return response


@jsonrpc.method('send_message', validate=True)
def send_message(chat_id, content, attach_id):
    """send_message controller"""
    # my_user_id = request.cookies.get('user_id')
    my_user_id = 1
    response = jsonify({"message": create_message_in_db(chat_id, my_user_id, content, attach_id)})
    return response


@jsonrpc.method('list_messages', validate=True)
def list_messages(chat_id):
    """list all messages for chat"""
    response = jsonify({"messages": list_messages_for_chat(chat_id)})
    return response


@jsonrpc.method('read_message', validate=True)
def read_message(message_id):
    """read_message controller"""
    # my_user_id = request.cookies.get('user_id')
    my_user_id = 1
    response = jsonify({"member": read_message_in_db(message_id, my_user_id)})
    return response


@jsonrpc.method('upload_file', validate=True)
def upload_file(chat_id, content):
    """upload_file controller"""
    # ADD file in DATABASE
    attachement = {
        "attach_id": 1,
        "message_id": 214,
        "chat_id": 41,
        "user_id": 21,
        "type": "image",
        "url": "attach/sdjk34kljn3kbk.jpg"
    }

    response = jsonify({"attach": attachement})
    response.mimetype = 'application/json'
    response.status_code = 200
    return response
