import unittest
import document_analysis as da
import json
import sys

text = open("sample.txt", "r")
class Unit_Test(unittest.TestCase):
    def test_word_frequency(self):
        with open('analysis_result.json','r') as file:
            results = json.load(file)
        self.assertEqual(da.word_analysis(text),results)
    
if __name__ == '__main__':
    print('Start my test')
    unittest.main()
