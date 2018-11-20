import unittest

from flask import json

from app import app


class AppTest(unittest.TestCase):
    """Class with tests for app controllers"""

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_send_message(self):
        rpc_query = {"jsonrpc": "2.0", "method": "send_message", \
                     "params": ["40", "Message text", "16"], "id": 23}

        rv = self.app.post('/api/', data=json.dumps(rpc_query), \
                           content_type='application/json')

        self.assertTrue("'content': 'Message text'" in str(json.loads(rv.data)))



    def test_list_messages(self):
        rpc_query = {"jsonrpc": "2.0", "method": "list_messages", \
                     "params": ["40"], "id": 1}

        rv = self.app.post('/api/', data=json.dumps(rpc_query), \
                           content_type='application/json')

        self.assertTrue("'content': 'Message text'" in str(json.loads(rv.data)))


    def test_read_message(self):
        rpc_query = {"jsonrpc": "2.0", "method": "read_message", \
                     "params": ["17"], "id": 15}

        rv = self.app.post('/api/', data=json.dumps(rpc_query), \
                           content_type='application/json')

        self.assertTrue("'last_read_message_id': 17" in str(json.loads(rv.data)))






