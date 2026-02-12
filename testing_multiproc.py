from process_manager import ProcessController
from dummy_env import DummyEnv
import multiprocessing
import time

if __name__ == "__main__":
    
    _proc_controller = ProcessController()
    
    _target_1 = DummyEnv(1, _proc_controller)
    
    _target_2 = DummyEnv(1, _proc_controller)
    
    _proc_1 = multiprocessing.Process(
        target=_target_1.test_multiproc
    )
    
    _proc_2 = multiprocessing.Process(
        target=_target_2.test_multiproc
    )   
    
    start_time = time.perf_counter()
    
    _proc_1.start()
    
    _proc_2.start()
    
    _proc_1.join()
    
    _proc_2.join()
    
    end_time = time.perf_counter()
    
    print(f"Multiprocess: The process ran for {round(end_time-start_time)} seconds.")
    
    start_time = time.perf_counter()
    
    _target_1.test_multiproc()
    
    _target_2.test_multiproc()
    
    end_time = time.perf_counter()
    
    print(f"Sequential: The process ran for {round(end_time-start_time)} seconds.")
