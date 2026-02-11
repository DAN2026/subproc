import subprocess
from abc import ABC,abstractmethod

class BaseProcess(ABC):
    
    def __init__(self, process_name):
        self._process_name = process_name
        self._state = "Not Running"
    
    @abstractmethod
    def launch(self):
        print(f"Launched process: {self._process_name}")
    
    @abstractmethod    
    def end(self):
        print(f"Ended process: {self._process_name}")
    
    @abstractmethod
    def reset(self):
        print(f"Restarted process: {self._process_name}")

    
    