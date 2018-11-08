"""Controllers"""
from flask import request, jsonify
from app import app
from app.model import search_users_in_db, list_chats_in_db, create_pers_chat_in_db


@app.route('/api/login/')
def login():
    """ login controller"""
    pass


@app.route('/api/search_users/', methods=["GET", "POST"])
def search_users():
    """ search-users controller"""
    if request.method == "GET":
        params = request.args.to_dict()
        if params.__contains__('query'):
            query = str(params['query'])
        else:
            response = jsonify({"Parameters Error": "query"})
            response.mimetype = 'application/json'
            response.status_code = 404
            return response
        if params.__contains__('limit'):
            limit = int(params['limit'])
        else:
            response = jsonify({"Parameters Error": "limit"})
            response.mimetype = 'application/json'
            response.status_code = 404
            return response

        # WHY REVERSE json?
        response = jsonify({"users": search_users_in_db(query,limit)})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response


    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/search_chats/', methods=["GET", "POST"])
def search_chats():
    """ search-chats controller"""
    if request.method == "GET":
        params = request.args.to_dict()
        if params.__contains__('query'):
            query = str(params['query'])
        else:
            response = jsonify({"Parameters Error": "query"})
            response.mimetype = 'application/json'
            response.status_code = 404
            return response
        if params.__contains__('limit'):
            limit = int(params['limit'])
        else:
            response = jsonify({"Parameters Error": "limit"})
            response.mimetype = 'application/json'
            response.status_code = 404
            return response
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

    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/list_chats/', methods=["GET", "POST"])
def list_chats():
    """list_chats controller"""
    if request.method == "GET":
        #user_id = request.cookies.get('user_id')
        user_id = 1

        response = jsonify({"chats": list_chats_in_db(user_id)})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 404})
    response.status_code = 405
    return response


@app.route('/api/create_pers_chat/', methods=["GET", "POST"])
def create_pers_chat():
    """create_pers_chat controller"""
    if request.method == "GET":
        user_id = str(request.args.get('user_id'))
       # my_user_id = request.cookies.get('user_id')

        my_user_id = 2
        # SELECT FROM DATABASE
        #ТУТ 3 сущности нужно создать в базе - чат и два мембера
        chat = {
            "chat_id": 22,
            "is_group_chat": False,
            "topic": "Clint Eastwood",
            "last_message": "asfgg",
            "new_messages": 0,
            "last_read_message_id": 0
        }

        response = jsonify({"chat":  create_pers_chat_in_db(user_id, my_user_id)})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response
    if request.method == "POST":
        #user_id = request.args.get('user_id')
        #my_user_id = request.cookies.get('user_id')
        user_id=1
        my_user_id=2
        # CREATE CHAT IN DATABASE

        chat = {
            "chat_id": 22,
            "is_group_chat": False,
            "topic": "Clint Eastwood",
            "last_message": "",
            "new_messages": 0,
            "last_read_message_id": 0
        }

        response = jsonify({"chat": create_pers_chat_in_db(user_id, my_user_id)})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 404})
    response.status_code = 404
    return response


@app.route('/api/create_group_chat/', methods=["GET", "POST"])
def create_group_chat():
    """create_group_chat controller"""
    if request.method == "GET":
        topic = str(request.args.get('topic'))
        # SELECT FROM DATABASE
        chat = {
            "chat_id": 52,
            "is_group_chat": True,
            "topic": " East",
            "last_message": "",
            "new_messages": 0,
            "last_read_message_id": 0
        }

        response = jsonify({"chat": [chat]})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response
    if request.method == "POST":
        user_id = request.args.get('user_id')
        # CREATE CHAT IN DATABASE

        chat = {
            "chat_id": 52,
            "is_group_chat": True,
            "topic": " East",
            "last_message": "",
            "new_messages": 0,
            "last_read_message_id": 0
        }

        response = jsonify({"chat": [chat]})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 404})
    response.status_code = 404
    return response


@app.route('/api/add_members_to_group_chat/', methods=["GET", "POST"])
def add_members_to_group_chat():
    """add_members_to_group_chat controller"""
    if request.method == "POST":
        chat_id = request.form.get('chat_id')
        user_ids = request.form.get('user_ids')
        # ADD IN CHAT IN DATABASE

        response = jsonify({})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/leave_group_chat/', methods=["GET", "POST"])
def leave_group_chat():
    """leave_group_chat controller"""
    if request.method == "POST":
        chat_id = request.form.get('chat_id')

        # LEAVE CHAT IN DATABASE

        response = jsonify({})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/send_message/', methods=["GET", "POST"])
def send_message():
    """send_message controller"""
    if request.method == "POST":
        chat_id = request.form.get('chat_id')
        content = request.form.get('content')
       # if request.form.contains('attach_id'):
          #  attach_id = request.form.get('attach_id')

        # CREATE MESSAGE IN DATABASE
        mess = {
            "message_id": 20,
            "chat_id": 33,
            "user_id": 23,
            "content": "HEEEEEKKK",
            "added_at": 124354623,
        }

        response = jsonify({"message": mess})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/read_message/', methods=["GET", "POST"])
def read_message():
    """read_message controller"""
    if request.method == "POST":
        message_id = request.form.get('message_id')

       # if request.form.contains('content'):
           # attach_id = request.form.get('content')

        # CHANGE UNREAD MESSAGES IN DATABASE
        chat = {
            "chat_id": 5,
            "is_group_chat": True,
            "topic": " East",
            "last_message": "",
            "new_messages": 4,
            "last_read_message_id": 13
        }

        response = jsonify({"chat": chat})
        response.mimetype = 'application/json'
        response.status_code = 200
        return response

    response = jsonify({"Error": 405})
    response.status_code = 405
    return response


@app.route('/api/upload_file/', methods=["GET", "POST"])
def upload_file():
    """upload_file controller"""
    if request.method == "POST":
        content = request.form.get('content')
        chat_id = request.form.get('chat_id')

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


    response = jsonify({"Error": 405})
    response.status_code = 405
    return response
