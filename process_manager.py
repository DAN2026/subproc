import subprocess
from dummy_env import DummyEnv
from base_process import BaseProcess

class ProcessController:
    
    def __init__(self):
        self._process_dict: dict[str, BaseProcess] = {}
        pass
    
    
    def register_process(self,  process : BaseProcess ):
        self._process_dict[process._process_name] = process
    
    def unregister_process(self, process_name):
        self._process_dict.pop(process_name)
        
    def display_dictionary(self):
        for key, value in self._process_dict.items():
            print(f"Key: {key}\n State: {value._state}\n PID: {value._pid}")       
        
    def update_process_pid(self, process_name):
        self._process_dict.get(
            key = process_name
        )
        
    def launch(self, process_name):
        self._process_dict.get(process_name).launch()
        pass
    
    
    
    