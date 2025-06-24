import unittest
from unittest.mock import patch, MagicMock
from app import app

class StudentAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.mysql')
    def test_get_students(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Arpit', 'arpit@example.com', 'CS')]
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/api/students')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Arpit', str(response.data))

    @patch('app.mysql')
    def test_add_student(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.post('/api/students', json={
            'name': 'Alice', 'email': 'alice@example.com', 'course': 'Math'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student added', str(response.data))

    @patch('app.mysql')
    def test_update_student(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.put('/api/students/1', json={
            'name': 'Updated', 'email': 'updated@example.com', 'course': 'Physics'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student updated', str(response.data))

    @patch('app.mysql')
    def test_delete_student(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.delete('/api/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student deleted', str(response.data))

if __name__ == '__main__':
    unittest.main()
