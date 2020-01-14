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
        print('\nConnection OK\n')
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
            print('\nInitial Post OK\n')
    def test_fail_component_missing(self):
        with self.app as client:
            result = client.post(
                '/api',
                data=json.dumps(dict(version='1', owner='testapp', status='ok')),
                content_type='application/json'
            )
            self.assertIn('400', result.status)
            self.assertIn('component is missing', result.data)
            print('\nComponent Missing error OK\n')
    def test_fail_version_missing(self):
        with self.app as client:
            result = client.post(
                '/api',
                data=json.dumps(dict(component='1', owner='testapp', status='ok')),
                content_type='application/json'
            )
            self.assertIn('400', result.status)
            self.assertIn('version is missing', result.data)
            print('\nVersion Missing error OK\n')
    def test_fail_owner_missing(self):
        with self.app as client:
            result = client.post(
                '/api',
                data=json.dumps(dict(component='1', version='testapp', status='ok')),
                content_type='application/json'
            )
            self.assertIn('400', result.status)
            self.assertIn('owner is missing', result.data)
            print('\nOwner Missing error OK\n')
    def test_fail_status_missing(self):
        with self.app as client:
            result = client.post(
                '/api',
                data=json.dumps(dict(component='1', version='testapp', owner='ok')),
                content_type='application/json'
            )
            self.assertIn('400', result.status)
            self.assertIn('status is missing', result.data)
            print('\nStatus Missing error OK\n')
if __name__ == '__main__':
    unittest.main()
