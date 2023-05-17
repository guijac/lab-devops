import unittest
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_hello_world(self):
        response = self.app.get('/')
        self.assertEqual("<h1>Hello World!</h1>", response.get_data(as_text=True)
                          , "Deu Ruim no test_print_hello_world!")

    def test_http_code(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code, "Deu ruim no test_http_code!")

if __name__ == "__main__":
    unittest.main()