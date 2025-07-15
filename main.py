from connection import config
from agents import Runner, Agent


translator = Agent(
    name = "Translator Agent",
    instructions = "You ara a translator agent Who can translate urdu to english"
)

result = Runner.run_sync(
    translator,"Mujhe kal governor house jana hai",
    run_config = config
)

print(result.final_output)