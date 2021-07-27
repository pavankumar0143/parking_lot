import pytest
import json

from parking_lot.run_commands import RunCommands


with open("./tests/test_data/run_commands_data.json") as fp:
    test_commads = json.load(fp)

run_command_obj = RunCommands()

@pytest.mark.parametrize("test_input", test_commads)
def test_run_command(test_input):

    test_command = test_input["input"].split(" ")

    output = run_command_obj.run_command(test_command)

    assert output == test_input["output"]