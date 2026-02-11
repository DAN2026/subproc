from process_manager import ProcessController
from dummy_env import DummyEnv

_controller = ProcessController()

test_env = DummyEnv(1, _controller)

test_env.test_launch()

