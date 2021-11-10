# Welcome to the Neuro Challenge

Your goal is to create a service that can receive user-provided functions (see example function below) remotely and distribute their execution amongst multiple workers. Users can interact with the service via a Python client you should also create. 
Example function:

```python
import time

def func(x):
    time.sleep(x)
    return x*x
```

The client-side API to run the above function on the service should look like:

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
- Write the Python module `distribute_challenge` which provides the client-side API above.
- Build the API service that allows remote function submission.
  Submitted functions should be distributed to workers for execution and the
  results returned to the client.
  - The number of workers should be configurable when starting the service.
  - The user function is sent to a single worker. Workers run a single user function at a time.
- Load test the API and demonstrate with a monitoring system of your choice throughput and allocation to each worker. Measure how your system scales with the number of workers and functions.
- You can use open source libraries to help you solve the challenge, however the more of your own skills you show the better! **Note: Ray cannot be used**.

#### Architecture diagram of deliverable

![alt text](https://uploads-ssl.webflow.com/5fbf86f72a3ba641ee136dbe/618c0ad1dd5c84a42917d914_Group%201.png)

