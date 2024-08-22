import os
import csv
import unittest

class TestFruitSales(unittest.TestCase):

    csv_file = "fruit.csv"

    def test_file_exists(self):
        assert os.path.exists(self.csv_file) == True, "csv file does not exist"
 
    
    def test_columns_exist(self):
        expected_columns = ['Apples','Bananas']
        with open('fruit.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames
            for col in expected_columns:
                assert col in reader.fieldnames
    
    def test_values_exist(self):
        expected_values = [{'Apples': '35', 'Bananas': '21'}, 
                            {'Apples': '41', 'Bananas': '34'}]
        with open('fruit.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            assert data == expected_values



if __name__ == "__main__":
    unittest.main(verbosity=2)