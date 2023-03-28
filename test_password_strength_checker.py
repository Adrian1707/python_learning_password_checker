import unittest
from password_strength_checker import password_strength_checker

class TestPasswordStrengthChecker(unittest.TestCase):

    def test_very_weak(self):
        password = "abc123"
        expected_strength = "Weak"
        actual_strength = password_strength_checker(password)
        self.assertEqual(expected_strength, actual_strength)

    def test_weak(self):
        password = "Abc123"
        expected_strength = "Moderate"
        actual_strength = password_strength_checker(password)
        self.assertEqual(expected_strength, actual_strength)

    def test_moderate(self):
        password = "Abc123!"
        expected_strength = "Strong"
        actual_strength = password_strength_checker(password)
        self.assertEqual(expected_strength, actual_strength)

    def test_strong(self):
        password = "AbCdE123"
        expected_strength = "Strong"
        actual_strength = password_strength_checker(password)
        self.assertEqual(expected_strength, actual_strength)

    def test_very_strong(self):
        password = "AbCdE@123"
        expected_strength = "Very Strong"
        actual_strength = password_strength_checker(password)
        self.assertEqual(expected_strength, actual_strength)

if __name__ == "__main__":
    unittest.main()
