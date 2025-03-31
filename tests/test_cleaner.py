import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import pandas as pd
from data_cleaner import load_and_clean_data

class TestCleaner(unittest.TestCase):
    def test_columns_exist(self):
        df = pd.read_csv("data/processed/cleaned_fires.csv")
        expected_cols = ['FIRE_YEAR', 'DISCOVERY_DATE', 'STAT_CAUSE_DESCR', 
                         'FIRE_SIZE', 'FIRE_SIZE_CLASS', 'LATITUDE', 'LONGITUDE', 'STATE']
        for col in expected_cols:
            self.assertIn(col, df.columns)

if __name__ == '__main__':
    unittest.main()
