from base_process import BaseProcess
import subprocess, time

class TorcsProcess(BaseProcess):
    
    def __init__(self, env_id):
        
        self._env_id = env_id
        
        self._name = f"Torcs-env-{self._env_id}" 

        super().__init__(
            process_name=self._name
        )
        
        self.pid = ""
    
    def launch(self):
        # Launch bs
        self.pid = subprocess.Popen("notepad.exe").pid
        pass
    
    def reset(self):
        return super().reset()
    
    def end(self):
        return super().end()    
    