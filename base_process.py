import subprocess
from abc import ABC,abstractmethod


from enum import Enum, auto

class ProcessState(Enum):
    RUNNING = auto()
    FINISHED = auto()
    NOT_STARTED = auto()
    CRASHED = auto()
    
class BaseProcess(ABC):
    
    __slots__ = ['_process_name', '_state', '_pid', '_process']
    
    def __init__(self, process_name):
        self._process_name = process_name
        self._state = ProcessState.NOT_STARTED
        self._pid = "No Process ID"
        self._process = "No Process Object"
        
    @abstractmethod
    def launch(self):
        pass
    
    @abstractmethod    
    def end(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass
    
    
    