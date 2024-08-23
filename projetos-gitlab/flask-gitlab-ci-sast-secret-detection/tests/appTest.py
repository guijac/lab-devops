import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/')
        self.assertEqual("<h1>Hello World!</h1>", response.get_data(as_text=True)
                          , "Deu Ruim no test_print_hello_world!")

    def test_http_code_health_check(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code, "Deu ruim no test_http_code!")

    def test_print_hello_success(self):
        response = self.app.get('/hello?name=guijac')
        self.assertEqual("Hello, guijac!", response.get_data(as_text=True)
                        , "Deu Ruim no test_print_hello_success!")

    def test_http_code_hello_error(self):
        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code, "Deu Ruim no test_print_hello_error!")

    def test_print_hello_error(self):
        response = self.app.get('/hello')
        self.assertEqual("Nome não informado", response.get_data(as_text=True)
                        , "Deu Ruim no test_print_hello_success!")
        
if __name__ == "__main__":
    unittest.main()