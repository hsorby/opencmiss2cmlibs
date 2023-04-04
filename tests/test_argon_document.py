import os.path
import shutil
import unittest

from upgradeargondocuments import main

here = os.path.dirname(__file__)
resources_dir = os.path.join(here, "resources")
backups_dir = os.path.join(resources_dir, "backups")
expected_dir = os.path.join(resources_dir, "expected")
inputs_dir = os.path.join(resources_dir, "inputs")


class ArgonDocumentsTestCase(unittest.TestCase):

    def _compare_files(self, sub_dir, name):
        with open(os.path.join(expected_dir, sub_dir, name)) as f:
            expected_content = f.read()

        with open(os.path.join(inputs_dir, sub_dir, name)) as f:
            actual_content = f.read()

        self.assertEqual(expected_content, actual_content)

    def test_argon_doc(self):
        sub_dir = "argon_doc"
        input_dir = os.path.join(inputs_dir, sub_dir)

        main([input_dir])

        self.assertTrue(os.path.isfile(os.path.join(input_dir, "argon_doc.json")))
        self._compare_files(sub_dir, "argon_doc.json")

        shutil.copyfile(os.path.join(backups_dir, sub_dir, "argon_doc.json"), os.path.join(inputs_dir, sub_dir, "argon_doc.json"))

    def test_multiple_argon_doc(self):
        sub_dir = "multiple_argon_docs"
        input_dir = os.path.join(inputs_dir, sub_dir)

        main([input_dir])

        self.assertTrue(os.path.isfile(os.path.join(input_dir, "argon_doc_1.json")))
        self._compare_files(sub_dir, "argon_doc_1.json")
        self.assertTrue(os.path.isfile(os.path.join(input_dir, "argon_doc_2.json")))
        self._compare_files(sub_dir, "argon_doc_2.json")

        shutil.copyfile(os.path.join(backups_dir, sub_dir, "argon_doc_1.json"), os.path.join(inputs_dir, sub_dir, "argon_doc_1.json"))
        shutil.copyfile(os.path.join(backups_dir, sub_dir, "argon_doc_2.json"), os.path.join(inputs_dir, sub_dir, "argon_doc_2.json"))

    def test_not_argon_doc(self):
        sub_dir = "not_argon_doc"
        input_dir = os.path.join(inputs_dir, sub_dir)

        main([input_dir])

        self.assertTrue(os.path.isfile(os.path.join(input_dir, "not_actually_json.json")))


if __name__ == "__main__":
    unittest.main()
