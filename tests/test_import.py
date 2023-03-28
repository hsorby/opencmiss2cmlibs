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

    def test_basic_import(self):
        basic_dir = os.path.join(inputs_dir, "basic")
        capture_err = io.StringIO()
        capture_out = io.StringIO()
        with contextlib.redirect_stderr(capture_err), contextlib.redirect_stdout(capture_out):
            main("libocm2cml.fixes", [basic_dir])

        self.assertTrue(os.path.isfile(os.path.join(basic_dir, "importopencmiss.py")))

        with open(os.path.join(expected_dir, "basic", "importopencmiss.diff")) as f:
            content = f.read()

        capture = capture_out.getvalue().replace("\t", "    ")
        self.assertEqual(content.format(input_dir=basic_dir), capture)

    def test_from_write_import(self):
        from_write_dir = os.path.join(inputs_dir, "from_write")
        capture_err = io.StringIO()
        capture_out = io.StringIO()
        with contextlib.redirect_stderr(capture_err), contextlib.redirect_stdout(capture_out):
            main("libocm2cml.fixes", ["-w", "-n", from_write_dir])

        self.assertTrue(os.path.isfile(os.path.join(from_write_dir, "importopencmiss.py")))

        with open(os.path.join(expected_dir, "from_write", "importopencmiss.diff")) as f:
            content = f.read()

        capture = capture_out.getvalue().replace("\t", "    ")
        self.assertEqual(content.format(input_dir=from_write_dir), capture)

        with open(os.path.join(from_write_dir, "importopencmiss.py")) as f:
            content = f.read()

        self.assertEqual("from cmlibs import zinc\n", content)

        shutil.copyfile(os.path.join(backups_dir, "from_write", "importopencmiss.py"), os.path.join(inputs_dir, "from_write", "importopencmiss.py"))


if __name__ == "__main__":
    unittest.main()
