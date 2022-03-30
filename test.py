import unittest
import os
import shutil
import tempfile
import inspect
from textwrap import dedent
from plotter import Plotter


TEST_RESULTS_PATH = 'test_results'
try:
    shutil.rmtree(TEST_RESULTS_PATH)
except OSError:
    pass
os.mkdir(TEST_RESULTS_PATH)

def create_temp_csv(contents):
    temp_fp = tempfile.NamedTemporaryFile(delete=False)
    temp_fp.write(contents)
    temp_fp.close()
    return temp_fp.name

def get_filename_from_frame(frame):
    test_name = frame.f_code.co_name
    return os.path.join(TEST_RESULTS_PATH, test_name + '.png')
