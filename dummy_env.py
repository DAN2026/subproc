from torcs_process import TorcsProcess
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from process_manager import ProcessController
    
class DummyEnv:
    def __init__(self, env_id, process_controller : ProcessController):
        
        self._id = env_id
        self._process_controller = process_controller
        
        _process = TorcsProcess(
            env_id=self._id
        )
        
        self._process_name = _process._name
        
        self._process_controller.register_process(
            process=_process
        )
        
        pass
    
    def test_launch(self):
        self._process_controller.launch(
            process_name=self._process_name
        )
        pass
    
    def test_reset(self):
        pass
    
    def test_end(self):
        pass