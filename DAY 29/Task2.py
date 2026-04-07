import time

def execution_logger(func):
    def wrapper(*args, **kwargs):
        print(f"--- Starting: {func.__name__} ---")
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"--- Finished: {func.__name__} (Duration: {end - start:.4f}s) ---")
        return result
    return wrapper

@execution_logger
def process_data():
    time.sleep(1)
    return "Data Processed"

print(process_data())
