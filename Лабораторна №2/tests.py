import unittest
import numpy as np
from main import generate_array, analyze_list

class TestAnalyzeList(unittest.TestCase):
    def test_generate_array_length(self):
        """Перевіряє, чи масив має правильну довжину."""
        arr = generate_array()
        self.assertEqual(len(arr), 10)
    
    def test_generate_array_range(self):
        """Перевіряє, чи всі елементи масиву в заданому діапазоні."""
        arr = generate_array()
        self.assertTrue(np.all((arr >= 5) & (arr < 20)))
    
    def test_analyze_list(self):
        """Перевіряє коректність аналізу списку."""
        test_arr = np.array([5, 7, 5, 10, 7, 7, 15, 15, 10, 5])
        unique_elements, counts = analyze_list(test_arr)
        expected_elements = np.array([5, 7, 10, 15])
        expected_counts = np.array([3, 3, 2, 2])
        
        np.testing.assert_array_equal(unique_elements, expected_elements)
        np.testing.assert_array_equal(counts, expected_counts)
    
if __name__ == '__main__':
    unittest.main()