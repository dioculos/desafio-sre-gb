#!/usr/bin/env python
import unittest, json
import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_connect(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        print('Connection OK')
    def test_post(self):
        with self.app as client:
            sent = {'component':'testcomp','version':'1','owner':'testapp','status':'ok'}
            result = client.post(
                '/api',
                data=json.dumps(dict(component='testcomp',version='1', owner='testapp', status='ok')),
                content_type='application/json'
            )                

            self.assertIn(
                '{"Request":{"component":"testcomp"',
                result.data
            )
            self.assertIn(
                '"owner":"testapp","status":"ok","version":"1"}}',
                result.data
            )            
if __name__ == '__main__':
    unittest.main()
