from graphene.test import Client
from .schema import schema

def test_hey():
    client = Client(schema)
    executed = client.execute('''{ hey }''')
    assert executed == {
        'data': {
            'hey': 'hello!'
        }
    }