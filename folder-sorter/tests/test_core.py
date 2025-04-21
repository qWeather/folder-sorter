import tempfile
import os
from unittest import TestCase, main, mock
from core import folder_sorter

@mock.patch("builtins.print")
class TestFolderSorter(TestCase):
    def setUp(self):
        self.file_types = ["txt", "pdf", "PDF", "py", "PY", "png", "PNG", "jpeg", "JPEG", "jpg", "JPG", "docx", "csv"]
        self.temp_dir = tempfile.TemporaryDirectory()

        for i, file_type in enumerate(self.file_types):
            test_path = os.path.join(self.temp_dir.name, f'file_{i}.{file_type}')
            open(test_path, "w").close()

        os.mkdir(f'{self.temp_dir.name}\\temp_subdir')
        self.temp_subdir = os.path.join(f'{self.temp_dir.name}\\temp_subdir', 'file_subdir.pdf')
        open(self.temp_subdir, "w").close()
        return super().setUp()

    def tearDown(self):
        self.temp_dir.cleanup()
        return super().tearDown()

    def test_folders_created(self, _):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=True)
        self.assertTrue(os.path.exists(f"{self.temp_dir.name}\\PDFs"))
        self.assertTrue(os.path.exists(f"{self.temp_dir.name}\\Images"))
        self.assertTrue(os.path.exists(f"{self.temp_dir.name}\\Python"))

    def test_correct_files_moved(self, _):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=False)
        for file in os.listdir(f"{self.temp_dir.name}\\PDFs"):
            ext = os.path.splitext(file)[1].lower()
            self.assertTrue(ext in ['.pdf', '.PDF'])
        for file in os.listdir(f"{self.temp_dir.name}\\Images"):
            ext = os.path.splitext(file)[1].lower()
            self.assertTrue(ext in ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'])
        for file in os.listdir(f"{self.temp_dir.name}\\Python"):
            ext = os.path.splitext(file)[1].lower()
            self.assertTrue(ext in ['.py', '.PY'])

    def test_output_messages_dry_run(self, mock_print):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=True)
        mock_print.assert_any_call(f"Would move file_1.pdf to folder PDFs")
        mock_print.assert_any_call(f"Would move file_2.PDF to folder PDFs")
        mock_print.assert_any_call(f"Would move file_3.py to folder Python")
        mock_print.assert_any_call(f"Would move file_4.PY to folder Python")
        mock_print.assert_any_call(f"Would move file_5.png to folder Images")
        mock_print.assert_any_call(f"Would move file_6.PNG to folder Images")
        mock_print.assert_any_call(f"Would move file_7.jpeg to folder Images")
        mock_print.assert_any_call(f"Would move file_8.JPEG to folder Images")
        mock_print.assert_any_call(f"Would move file_9.jpg to folder Images")
        mock_print.assert_any_call(f"Would move file_10.JPG to folder Images")
        mock_print.assert_any_call(f"Would have moved 10 file(s) in total.")

    def test_output_messages_no_dry_run(self, mock_print):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=False)
        mock_print.assert_any_call(f"Moved file_1.pdf to folder PDFs")
        mock_print.assert_any_call(f"Moved file_2.PDF to folder PDFs")
        mock_print.assert_any_call(f"Moved file_3.py to folder Python")
        mock_print.assert_any_call(f"Moved file_4.PY to folder Python")
        mock_print.assert_any_call(f"Moved file_5.png to folder Images")
        mock_print.assert_any_call(f"Moved file_6.PNG to folder Images")
        mock_print.assert_any_call(f"Moved file_7.jpeg to folder Images")
        mock_print.assert_any_call(f"Moved file_8.JPEG to folder Images")
        mock_print.assert_any_call(f"Moved file_9.jpg to folder Images")
        mock_print.assert_any_call(f"Moved file_10.JPG to folder Images")
        mock_print.assert_any_call(f"Moved 10 file(s) in total.")

    def test_non_matching_files_not_moved(self, _):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=False)
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\PDFs\\file_0.txt"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\PDFs\\file_11.docx"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\PDFs\\file_12.csv"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Python\\file_0.txt"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Python\\file_11.docx"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Python\\file_12.csv"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Images\\file_0.txt"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Images\\file_11.docx"))
        self.assertFalse(os.path.exists(f"{self.temp_dir.name}\\Images\\file_12.csv"))

    def test_subdirs_skipped(self, _):
        folder_sorter(folder_path=self.temp_dir.name, dry_run=False)
        self.assertFalse(os.path.exists(f"{self.temp_subdir}\\test_subdir.pdf"))

if __name__ == '__main__':
    main()