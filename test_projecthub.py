import unittest, json

from unittest.mock import patch, mock_open
from main import is_valid_project_name, add_project, save_projects, load_projects, main

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

    def test_add_project_saves_to_json(self):
        projects = []
        mocked_file = mock_open()

        with patch("builtins.input", return_value="Aprender Python"), \
            patch("builtins.open", mocked_file):
            add_project(projects)

        written_data = "".join(
            call.args[0] for call in mocked_file().write.call_args_list
        )

        self.assertEqual(
            json.loads(written_data),
            ["Aprender Python"]
        )

    def test_save_projects(self):
        projects = ["Aprender Python", "Crear ProjectHub"]
        mocked_file = mock_open()

        with patch("builtins.open", mocked_file):
            save_projects(projects)

        written_data = "".join(
            call.args[0] for call in mocked_file().write.call_args_list
        )

        self.assertEqual(
            json.loads(written_data),
            projects
        )

class TestLoadProject(unittest.TestCase):
    def test_load_projects(self):
        projects = ["Aprender Python", "Crear ProjectHub"]
        mocked_file = mock_open(read_data='["Aprender Python", "Crear ProjectHub"]')

        with patch("builtins.open",side_effect=[FileExistsError, mocked_file.return_value]):
            loaded_projects = load_projects()

        self.assertEqual(
            loaded_projects,
            projects
        )

    def test_load_projects_when_file_does_not_exist(self):
        mocked_file = mock_open(read_data="[]")

        with patch("builtins.open", mocked_file):
            loaded_projects = load_projects()

        self.assertEqual(loaded_projects, [])

    def test_invalid_file_type(self):
        mocked_file = mock_open(read_data="Esto no es un JSON")
        
        with patch("builtins.open",side_effect=[FileExistsError, mocked_file.return_value]):
            loaded_projects = load_projects()

        self.assertIsNone(loaded_projects)

    def test_main_stops_when_projects_cannot_load(self):

        with patch("main.load_projects", return_value = None), \
        patch("main.display_menu") as mocked_menu:
            main()
            mocked_menu.assert_not_called()

    def test_load_projects_rejects_invalid_name(self):
        mocked_file = mock_open(read_data='["Proyecto 1", 1234]')

        with patch("builtins.open",side_effect=[FileExistsError, mocked_file.return_value]):
            loaded_projects = load_projects()

        self.assertIsNone(loaded_projects)

    def test_valid_json_rejects_invalid_type(self):
        mocked_file = mock_open(read_data='"Proyecto 1"')

        with patch("builtins.open",side_effect=[FileExistsError, mocked_file.return_value]):
            loaded_projects = load_projects()

        self.assertIsNone(loaded_projects)