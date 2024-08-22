import os
import unittest
import pandas as pd

class TestFruitSales(unittest.TestCase):

    csv_file = "fruit.csv"

    def test_file_exists(self):
        assert os.path.exists(self.csv_file) == True, "csv file does not exist"
 
    
    def test_columns_exist(self):
        expected_columns = ['Apples','Bananas']
        try:
            df = pd.read_csv(self.csv_file)
            for col in expected_columns:
                assert col in df.columns
        except Exception as e:
            assert False, e
    
    def test_values_exist(self):
        try:
            df = pd.read_csv(self.csv_file)
            expected_values = {'Apples': [35,41],'Bananas':  [21,34]}
            for key in expected_values.keys():
                assert expected_values[key] in df[key].values
        except Exception as e:
            assert False, e

if __name__ == "__main__":
    unittest.main(verbosity=2)