# Welcome to the Neuro Challenge

Your goal is to create a system that enables distributed computation of a given function.
Example given function,
```
def func(x):
    return x*x
```

### Deliverable
- The function will be serialised and sent to a local server where it will be distributed across different workers.
- The number of workers will be allocated to maximise throughput.

#### Interface
```
# Build a decorator as interface between the function to compute and your distributed infrastructure
@compute_this()
def func(x):
    return x*x
```
#### Stress test
```
# Run this to test
for i in range(20):
    out = func(i)
```






