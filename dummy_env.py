#region Imports

from torcs_process import TorcsProcess
from typing import TYPE_CHECKING
import time

if TYPE_CHECKING:
    from process_manager import ProcessController
    
#endregion    

class DummyEnv:
    def __init__(self, env_id, process_controller : ProcessController):
        
        self._id = env_id
        self._process_controller = process_controller
        
        _torcs_process = TorcsProcess(
            env_id=self._id
        )
        
        self._process_name = _torcs_process._process_name
        
        self._process_controller.register_process(
            process=_torcs_process
        )
        

        

        
    
    
    def test_multiproc(self):
        
        self._process_controller.launch(self._process_name)
        
        time.sleep(2)
        
        self._process_controller.end(self._process_name)
        
    def test_threading(self):
        
        self._process_controller.launch(self._process_name)
        
        time.sleep(2)
        
        self._process_controller.end(self._process_name)
    