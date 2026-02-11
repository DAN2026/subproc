import subprocess
from abc import ABC,abstractmethod

class BaseProcess(ABC):
    
    def __init__(self, process_name):
        self._process_name = process_name
        self._state = "Not Running"
        self._pid = ""
        
    @abstractmethod
    def launch(self):
        pass
    
    @abstractmethod    
    def end(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass
    
    