import unittest
import os
from dispatcher import PackageDispatcher

# TODO: Make these dynamic. Since we have classification dynamically configurable these would fail with configuration changes (not ideal)
class TestPackageDispatcher(unittest.TestCase):
    def setUp(self):
        # Ensure the config file path is correct
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '..', 'config.ini')
        self.dispatcher = PackageDispatcher(config_file=config_path)

    def test_standard_package(self):
        self.assertEqual(self.dispatcher.sort(10, 10, 10, 5), "STANDARD")
        self.assertEqual(self.dispatcher.sort(100, 50, 20, 19), "STANDARD")
        self.assertEqual(self.dispatcher.sort(149, 149, 149, 19.9), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(149.99, 149.99, 149.99, 19.99), "SPECIAL")

    def test_bulky_package(self):
        self.assertEqual(self.dispatcher.sort(100, 100, 100, 5), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(150, 10, 10, 5), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(200, 200, 200, 10), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(150, 150, 150, 19.99), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(self.dispatcher.sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(100, 100, 100, 25), "REJECTED")
        self.assertEqual(self.dispatcher.sort(149.99, 149.99, 149.99, 20), "REJECTED")

    def test_rejected_package(self):
        self.assertEqual(self.dispatcher.sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(self.dispatcher.sort(200, 200, 200, 50), "REJECTED")
        self.assertEqual(self.dispatcher.sort(150, 150, 150, 20), "REJECTED")
        self.assertEqual(self.dispatcher.sort(150, 150, 150, 50), "REJECTED")

    def test_edge_cases(self):
        self.assertEqual(self.dispatcher.sort(1000000 / (150 * 150), 150, 150, 19.99), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(100, 100, 1000000 / (100 * 100), 19.99), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(149.99, 149.99, 149.99, 19.99), "SPECIAL")
        self.assertEqual(self.dispatcher.sort(150, 149.99, 149.99, 20), "REJECTED")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.dispatcher.sort(-10, 10, 10, 5)

        with self.assertRaises(ValueError):
            self.dispatcher.sort(0, 10, 10, 5)

        with self.assertRaises(ValueError):
            self.dispatcher.sort('a', 10, 10, 5)

        with self.assertRaises(ValueError):
            self.dispatcher.sort(10, 10, 10, -5)

        with self.assertRaises(ValueError):
            self.dispatcher.sort(10, 10, 10, 0)

        with self.assertRaises(ValueError):
            self.dispatcher.sort(10, 10, 10, 'b')

if __name__ == '__main__':
    unittest.main()
