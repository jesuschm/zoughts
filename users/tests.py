from django.test import TestCase
from django.test import Client
from core.test_util import query

DUMMY_EMAIL = "dummy@fake.com"
DUMMY_USERNAME = "dummy"
DUMMY_PASS = "123456789qwerty*"

# Inherit from this in your test cases
class GraphQLTestCase(TestCase):

    def setUp(self):
        self._client = Client()
        
    def test_register(self):
        resp = query(client = self._client, 
                        query = '''
                                mutation {
                                    register(
                                        email: "dummy@fake.com",
                                        username: "test_user",
                                        password1: "123456789qwerty*",
                                        password2: "123456789qwerty*",
                                    ) {
                                        success,
                                        errors,
                                        token,
                                        refreshToken
                                    }
                                }
                            ''')
        
        self.assertIn('data', resp),
        self.assertIn('register', resp['data'])
        self.assertEqual(resp.get('data').get('register').get('success'), True)
        self.assertIn('token', resp.get('data').get('register'))
        
    def test_login(self):
        resp = query(client= self._client,
                        query = '''
                                mutation {
                                    tokenAuth(email: "dummy@fake.com", password: "123456789qwerty*") {
                                        success,
                                        errors,
                                        unarchiving,
                                        token,
                                        unarchiving,
                                        user {
                                        pk,
                                        username,
                                        email
                                        }
                                    }
                                    }
                            ''')