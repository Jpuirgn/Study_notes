# concurrency.py (Chaos Edition)
import threading

counter = 0
loops = 1_000_000

# --- EXPLANATION OF PYTHON'S GIL AND CONCURRENCY ---
# 1. What is the GIL (Global Interpreter Lock)?
# The GIL is a special lock inside Python. It ensures that only ONE thread 
# can execute Python bytecode at any given exact microsecond, even if your 
# computer has a multi-core CPU. 
#
# 2. Why did the code work perfectly WITHOUT the dummy function?
# Modern Python is highly optimized. When you run a simple math operation 
# like "counter += 1" in a tight loop, it happens so fast that the Python 
# interpreter rarely bothers to pause the thread and yield the GIL. The thread 
# finishes the "read -> add -> write" steps without being interrupted.
#
# 3. Why does adding the dummy function cause the expected "chaos"?
# Calling ANY function (even an empty one) forces the Python interpreter 
# to check if it should release the GIL and let another thread run. 
# By placing this function call right between reading and writing the variable,
# we artificially force the OS to trigger a Context Switch at the worst possible moment!
# ---------------------------------------------------

def force_context_switch():
    pass

def worker():
    global counter
    for _ in range(loops):
        # Step 1: Read the shared variable
        temp = counter      
        
        # Step 2: The Tripwire! 
        # This function call forces the Operating System to potentially 
        # pause this thread and let the other thread run exactly at this vulnerable moment.
        force_context_switch() 
        
        # Step 3: Write back the updated value
        counter = temp + 1

# Create two independent threads
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

# Start both threads at the exact same time
thread1.start()
thread2.start()

# Wait for both to finish
thread1.join()
thread2.join()

print(f"Expected final value : {loops * 2}")
print(f"Actual final value   : {counter}")