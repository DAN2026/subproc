from process_manager import ProcessController
from dummy_env import DummyEnv
import multiprocessing
import time
import threading

if __name__ == "__main__":
    
    _proc_controller = ProcessController()
    
    _target_1 = DummyEnv(1, _proc_controller)
    
    _target_2 = DummyEnv(1, _proc_controller)
    
    thread_1 = threading.Thread(
        target=_target_1.test_threading
    )
    
    thread_1.start()
    
    # thread_1.join() # So this forces the interpreter to wait for this to be done
    
    print("Woah im past the thread")
    
    current_threads = threading.enumerate()

    print(f"There are currently {len(current_threads)} threads running.")