from base_process import BaseProcess, ProcessState
import subprocess, time

class TorcsProcess(BaseProcess):
    
    __slots__ = ['_env_id']

    def __init__(self, env_id):
        
        self._env_id = env_id
        
        super().__init__(
            process_name=f"torcs-env-{self._env_id}"
        )
        
    
    def launch(self):
        self._process = subprocess.Popen("notepad.exe")
        self._pid = self._process.pid
        
    def reset(self):
        self.end()
        self.launch()
        pass        
    
    def end(self):
        self._process.terminate()
        pass
        
    