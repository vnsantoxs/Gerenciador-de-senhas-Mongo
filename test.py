import unittest
from src import *

class TestCRUDFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_app(self):
        create_app('AppTest', '12345')

    def test_list_apps(self):
        apps = list_apps()

    def test_update_app(self):
        update_app('AppTest', '54321')

    def test_search_app(self):
        app = search_app('AppTest')

    def test_delete_app(self):
        delete_app('AppTest')

if __name__ == '__main__':
    num_execucoes = 15

    for _ in range(num_execucoes):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCRUDFunctions)
        unittest.TextTestRunner(verbosity=2).run(suite)
