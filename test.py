import unittest
from main import SquaredSequentialSurfaceSimulation


class TestDomain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initial_expected_input_output(self):
        sample_input = ["5 5", "1 2 N", "L M L M L M L M M",
                        "3 3 E", "M M R M M R M R R M"]
        sim = SquaredSequentialSurfaceSimulation().run(sample_input)
        self.assertEqual(sim, ["1 3 N", "5 1 E"])


if __name__ == "__main__":
    unittest.main()
