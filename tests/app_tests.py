"""Unit-tests for app"""
import unittest

from app import app


class AppTest(unittest.TestCase):
    """Class with tests for app controllers"""

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_search_users(self):
        """Test search-users controller"""

        response = self.app.get('/search_users/?query=sdgs&limit=6')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{"users":[{"avatar":"avatar1.png",'
                         b'"name":"Clint Eastwood","nick":"the.good",'
                         b'"user_id":22},{"avatar":"avatar2.png","name":"Cliwood","nick":"od",'
                         b'"user_id":222},{"avatar":"avatar3.png","name":"intwood","nick":"god",'
                         b'"user_id":262}]}\n', response.data)
        response_wrong = self.app.post('/search_users/')
        self.assertEqual(405, response_wrong.status_code)

    def test_search_chats(self):
        """Test search-chats controller"""
        response = self.app.get('/search_chats/?query=sdgs&limit=6')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)

        self.assertEqual(b'{"chats":[{"chat_id":22,"is_group_chat":false,"last_message":"asfgg",'
                         b'"last_read_message_id":214,"new_messages":39,'
                         b'"topic":"Clint Eastwood"},'
                         b'{"chat_id":242,"is_group_chat":false,"last_message":"gg",'
                         b'"last_read_message_id":21,'
                         b'"new_messages":3,"topic":"wood"}]}\n', response.data)
        response_wrong = self.app.post('/search_chats/')
        self.assertEqual(405, response_wrong.status_code)

    def test_list_chats(self):
        """Test list-chats controller"""
        response = self.app.get('/list_chats/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)

        self.assertEqual(b'{"chats":[{"chat_id":22,"is_group_chat":false,"last_message":"asfgg",'
                         b'"last_read_message_id":214,"new_messages":39,'
                         b'"topic":"Clint Eastwood"}]}\n', response.data)
        response_wrong = self.app.post('/list_chats/')
        self.assertEqual(405, response_wrong.status_code)

    def test_create_pers_chats(self):
        """Test create-pers-chats controller"""
        response = self.app.get('/create_pers_chat/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{"chat":[{"chat_id":22,"is_group_chat":false,'
                         b'"last_message":"asfgg",'
                         b'"last_read_message_id":0,"new_messages":0,'
                         b'"topic":"Clint Eastwood"}]}\n', response.data)
        response_wrong = self.app.post('/create_pers_chat/')
        self.assertEqual(200, response_wrong.status_code)
        self.assertEqual('application/json', response_wrong.mimetype)

    def test_create_group_chats(self):
        """Test create-group-chats controller"""
        response = self.app.get('/create_group_chat/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        print(response.data)
        self.assertEqual(b'{"chat":[{"chat_id":52,"is_group_chat":true,'
                         b'"last_message":"","last_read_message_id":0,'
                         b'"new_messages":0,"topic":" East"}]}\n', response.data)
        response_wrong = self.app.post('/create_group_chat/')
        self.assertEqual(200, response_wrong.status_code)
        self.assertEqual('application/json', response_wrong.mimetype)
        self.assertEqual(b'{"chat":[{"chat_id":52,"is_group_chat":true,'
                         b'"last_message":"",'
                         b'"last_read_message_id":0,"new_messages":0,'
                         b'"topic":" East"}]}\n', response_wrong.data)

    def test_add_members_to_group_chat(self):
        """Test add_members_to_group_chat controller"""
        response = self.app.post('/add_members_to_group_chat/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{}\n', response.data)
        response_wrong = self.app.get('/add_members_to_group_chat/')
        self.assertEqual(405, response_wrong.status_code)

    def test_leave_group_chat(self):
        """Test leave_group_chat controller"""
        response = self.app.post('/leave_group_chat/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{}\n', response.data)
        response_wrong = self.app.get('/leave_group_chat/')
        self.assertEqual(405, response_wrong.status_code)

    def test_send_message(self):
        """Test send_message controller"""
        response = self.app.post('/send_message/', data=dict(
            chat_id=34,
            content="dfhjdj"))
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{"message":{"added_at":124354623,"chat_id":33,"content":"HEEEEEKKK",'
                         b'"message_id":20,"user_id":23}}\n', response.data)
        response_wrong = self.app.get('/send_message/')
        self.assertEqual(405, response_wrong.status_code)

    def test_read_message(self):
        """Test read_message controller"""
        response = self.app.post('/read_message/', data=dict(
            message_id=34))
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{"chat":{"chat_id":5,"is_group_chat":true,'
                         b'"last_message":"",'
                         b'"last_read_message_id":13,"new_messages":4,'
                         b'"topic":" East"}}\n', response.data)
        response_wrong = self.app.get('/read_message/')
        self.assertEqual(405, response_wrong.status_code)

    def test_upload_file(self):
        """Test upload_file controller"""
        response = self.app.post('/upload_file/', data=dict(
            chat_id=4,
            content="ddj"))
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.mimetype)
        self.assertEqual(b'{"attach":{"attach_id":1,"chat_id":41,'
                         b'"message_id":214,"type":"image",'
                         b'"url":"attach/sdjk34kljn3kbk.jpg",'
                         b'"user_id":21}}\n', response.data)
        response_wrong = self.app.get('/upload_file/')
        self.assertEqual(405, response_wrong.status_code)

    if __name__ == "__main__":
        unittest.main()
