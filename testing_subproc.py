from process_manager import ProcessController
from dummy_env import DummyEnv
import multiprocessing

_controller = ProcessController()

test_env1 = DummyEnv(1, _controller)

test_env2 = DummyEnv(2, _controller)

test_env3 = DummyEnv(3, _controller)

test_env4 = DummyEnv(4, _controller)

_controller.display_dictionary()

# None = Running

# 0 = Finished

# We will check for anything else.
