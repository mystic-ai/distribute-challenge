# Welcome to the Neuro Challenge

Your goal is to create a system that enables distributed computation of a given function.
With a function such as,

```python
import time

def func(x):
    time.sleep(x)
    return x*x
```

The API to run this function on the remote system should look like:

```python
import time

from distribute_challenge import compute_this

@compute_this()
def func(x):
    time.sleep(x)
    return x*x
    
out = func(2).run()
assert out == 4
```

### Deliverable
- Write a Python module which matches the API design above.
- Build a system backing the API that distributes a given function across different workers on a 'remote' cluster. The number of workers should be configurable.
- Load test the API and demonstrate with a monitoring system of your choice throughput and allocation to each worker. Measure how your system scales with the number of workers.
- You can use open source libraries to help you solve the challenge, however the more of your own skills you show the better! **Note: Ray cannot be used**.
