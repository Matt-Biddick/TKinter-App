import unittest
import app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.table_name, self.table_records = app.fetch_db()

    def tearDown(self):
        pass
  
    def test_pre_process_returns_tuple(self):
        self.assertIsInstance(app.pre_process(self.table_name, self.table_records), tuple)

    def test_fetch_db_returns_tuple(self):
        self.assertIsInstance(app.fetch_db(), tuple)

if __name__ == '__main__':
    unittest.main()