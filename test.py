import unittest
import sys

from simulation import SquaredSequentialSurfaceSimulation
from inputs import DummyInput, FileInput
from output import Console


class TestDomain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initial_expected_input_output(self):
        sample_input = ["5 5", "1 2 N", "L M L M L M L M M",
                        "3 3 E", "M M R M M R M R R M"]
        sim = SquaredSequentialSurfaceSimulation().calculate(sample_input)
        self.assertEqual(sim, ["1 3 N", "5 1 E"])

    def test_collision_during_simulation(self):
        sample_input = ["5 5", "1 2 N", "L M L M L M L M M",
                        "3 3 W", "M M R M M R M R R M"]
        sim = SquaredSequentialSurfaceSimulation().calculate(sample_input)
        self.assertEqual(sim, ["1 3 N", "Collision!"])

    def test_collision_start(self):
        sample_input = ["5 5", "1 2 N", "L M L M L M L M M",
                        "1 3 N", "M M R M M R M R R M"]
        sim = SquaredSequentialSurfaceSimulation().calculate(sample_input)
        self.assertEqual(sim, ["1 3 N", "Collision!"])

    def test_out_of_plateau(self):
        sample_input = ["5 5", "1 2 N", "L M M M L M L M L M M",
                        "3 3 E", "M M R M M R M R R M"]
        sim = SquaredSequentialSurfaceSimulation().calculate(sample_input)
        self.assertEqual(sim, ["Out of Plateau!", "5 1 E"])


class TestInput(unittest.TestCase):

    def test_dummy(self):
        sample_input = ["5 5", "1 2 N", "L M M M L M L M L M M",
                        "3 3 E", "M M R M M R M R R M"]
        dummy = DummyInput(sample_input)
        self.assertEqual(dummy.read(), sample_input)

    def test_file(self):
        fileInput = FileInput("input_test.txt")
        self.assertEqual(fileInput.read(),
                         ["5 5", "1 2 N", "L M L M L M L M M",
                         "3 3 E", "M M R M M R M R R M"])


class MockConsole():

    def __init__(self):
        self.vals = []

    def write(self, value):
        if value != "\n":
            self.vals.append(value)

    def flush(self):
        pass


class TestOutput(unittest.TestCase):

    def test_console(self):
        sys.stdout = MockConsole()
        output = Console()
        output.send(["Out 1", "Out 2"])
        output.send(["Out 3"])
        self.assertEqual(sys.stdout.vals, ["Out 1", "Out 2", "Out 3"])


class TestIntegrations(unittest.TestCase):

    def test_main_case_file(self):
        sys.stdout = MockConsole()
        fileIn = FileInput("input_test.txt")
        out = Console()
        SquaredSequentialSurfaceSimulation(input_obj=fileIn, output=out).run()
        self.assertEqual(sys.stdout.vals, ["1 3 N", "5 1 E"])
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
