# Welcome to the Neuro Challenge

Your goal is to create a system that enables distributed computation of a given function.
Example given function,
```python
def func(x):
    return x*x
```

### Deliverable
- Build an API that distributes a given function across different workers.
- The number of workers will be allocated to maximise throughput.
- Load test the API and demonstrate with a monitoring system of your choice throughput and allocation to each worker.

#### Interface
```python
@compute_this()
def func(x):
    return x*x

out = func(x).compute()
```