import importlib.util
import pathlib
import unittest

spec = importlib.util.spec_from_file_location(
    "task_state_machine", pathlib.Path(__file__).with_name("task_state_machine.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class StateMachineTests(unittest.TestCase):
    def test_allowed_transition(self):
        module.validate_transition(module.TaskState.QUEUED, module.TaskState.RESEARCHING)

    def test_disallowed_transition(self):
        with self.assertRaises(ValueError):
            module.validate_transition(module.TaskState.COMPLETED, module.TaskState.RESEARCHING)

if __name__ == "__main__":
    unittest.main()
