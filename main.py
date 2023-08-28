from simulation import SquaredSequentialSurfaceSimulation
from inputs import DummyInput
from output import Console

sample_input = ["5 5", "1 2 N", "L M L M L M L M M",
                "3 3 E", "M M R M M R M R R M"]
input_obj = DummyInput(sample_input)
output = Console()
SquaredSequentialSurfaceSimulation(input_obj=input_obj, output=output).run()
