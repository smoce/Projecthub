import unittest

from unittest.mock import patch, mock_open
from main import is_valid_project_name, add_project

class TestProjectName(unittest.TestCase):
    def test_valid_project_name(self):
        self.assertTrue(is_valid_project_name("Aprender python"))
    
    def test_empty_project_name(self):
        self.assertFalse(is_valid_project_name(""))
    
    def test_whitespace_project_name(self):
        self.assertFalse(is_valid_project_name("   "))

    def test_project_name_none(self):
        self.assertFalse(is_valid_project_name(None))
        
class TestAddProject(unittest.TestCase):
    def test_add_valid_project(self):
        projects = []

        with patch("builtins.input",return_value="Aprender Python"), \
        patch("builtins.open",mock_open()):
            add_project(projects)
        
        self.assertEqual(projects,["Aprender Python"])


    def test_add_invalid_project(self):
        projects = []

        with patch("builtins.input",return_value="   "), \
        patch("builtins.open",mock_open()):
            add_project(projects)
        
        self.assertEqual(projects,[])