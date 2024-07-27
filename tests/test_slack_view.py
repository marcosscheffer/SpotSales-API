import unittest
from io import BytesIO
from flask_jwt_extended import create_access_token
import json

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user_model import UserModel
from app.models.position_model import PositionModel

class TestSlackViews(unittest.TestCase):
    def setUp(self):
        self.channel_id = "" # Add a your channel id
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        with self.app.app_context():
            db.create_all()
            
        self.position = PositionModel(title="TestPosition")
        db.session.add(self.position)
        db.session.commit()
        
        self.user = UserModel(name="TestUser", email="TestUser@example.com", 
                              cpf="12345678900", password="12345678", active=True,
                              admin=False, bot=True, position_id=1)
        self.user.encrypt_password()
        db.session.add(self.user)
        db.session.commit()
        
        self.access_token = create_access_token(self.user.id)
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop() 
        

    def test_send_valid_message(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": self.channel_id,
            "message": "Hello, World!"
        }, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn("ts", response.get_data(as_text=True))
        
    def test_send_invalid_message(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "message": ""
        }, headers=headers)
        
        self.assertEqual(400, response.status_code)
    
    def test_send_unauthorized_message(self):
        self.user.active = False
        self.access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": self.channel_id,
            "message": "Hello, World!"
        }, headers=headers)
        
        self.assertEqual(401, response.status_code)
        
    def test_not_send_message(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": "",
            "message": "Hello, World!"
        }, headers=headers)
                
        self.assertEqual(500, response.status_code)
        
    def test_send_ts_message(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": self.channel_id,
            "message": "Hello, World!"
        }, headers=headers)
        
        ts = json.loads(response.get_data(as_text=True))["ts"]

        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": self.channel_id,
            "message": "Hello, World!",
            "ts": ts
        }, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn("ts", response.get_data(as_text=True))

    def test_send_valid_file(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'channel_id': self.channel_id,
            'file': (BytesIO(b'my file contents'), 'test.txt')
        }
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn("ts", response.get_data(as_text=True))
        
    def test_send_invalid_file(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'file': (BytesIO(b''), 'test.txt')
        }
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)
        
        self.assertEqual(400, response.status_code)
    
    def test_send_unauthorized_file(self):
        self.user.active = False
        self.access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'channel_id': self.channel_id,
            'file': (BytesIO(b'my file contents'), 'test.txt')
        }
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)

        self.assertEqual(response.status_code, 401)
        
    def test_not_send_file(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'channel_id': '',
            'file': (BytesIO(b'my file contents'), 'test.txt')
        }
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)

        self.assertEqual(response.status_code, 500)
        
    def test_send_ts_file(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/slack/send/message', json={
            "channel_id": self.channel_id,
            "message": "Hello, World!"
        }, headers=headers)
        ts = json.loads(response.get_data(as_text=True))["ts"]
        
        data = {
            'channel_id': self.channel_id,
            'file': (BytesIO(b'my file contents'), 'test.txt'),
            "ts": ts
        }
        
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)


        self.assertEqual(response.status_code, 200)
        self.assertIn("ts", response.get_data(as_text=True))
        
    
    def test_not_found_file(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'channel_id': self.channel_id
        }
        response = self.client.post('/api/v1/slack/send/file/upload', content_type='multipart/form-data', data=data, headers=headers)

        self.assertEqual(response.status_code, 400)
        
        
        
        