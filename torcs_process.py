from base_process import BaseProcess
import subprocess, time

class TorcsProcess(BaseProcess):
    
    def __init__(self, env_id):
        
        self._env_id = env_id
        
        self._name = f"Torcs-env-{self._env_id}" 

        super().__init__(
            process_name=self._name
        )
        
    
    def launch(self):
        self._process = subprocess.Popen("notepad.exe")
        self._pid = self._process.pid
        self._state = "Running"
    
    def reset(self):
        pass        
    
    def end(self):
        
        if self._process:
            print(f"Closing {self._process_name}")            
        
    