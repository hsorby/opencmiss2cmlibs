import contextlib
import io
import os.path
import shutil
import unittest

from opencmiss2cmlibs import main

here = os.path.dirname(__file__)
resources_dir = os.path.join(here, "resources")
backups_dir = os.path.join(resources_dir, "backups")
expected_dir = os.path.join(resources_dir, "expected")
inputs_dir = os.path.join(resources_dir, "inputs")


class ImportTestCase(unittest.TestCase):

    def test_basic(self):
        input_dir = os.path.join(inputs_dir, "python3_syntax")
        capture_err = io.StringIO()
        capture_out = io.StringIO()
        with contextlib.redirect_stderr(capture_err), contextlib.redirect_stdout(capture_out):
            main("libocm2cml.fixes", [input_dir])

        self.assertEqual("", capture_out.getvalue())
        self.assertEqual("RefactoringTool: No files need to be modified.\n", capture_err.getvalue())


if __name__ == "__main__":
    unittest.main()
