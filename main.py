from process_manager import ProcessController
from dummy_env import DummyEnv

_controller = ProcessController()

test_env = DummyEnv(1, _controller)

_controller.display_dictionary()

test_env.test_launch()

_controller.display_dictionary()