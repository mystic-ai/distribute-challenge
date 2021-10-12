# Welcome to the Neuro Challenge (Level 2)

Now that you've distributed a function, it is time to distribute a class object. At Neuro we focus on building an API 
on ML compute so it is important that you know how to distribute more complex objects such as ML models.

Modify/improve the previous challenge to allow distributing 
across different workers the child class `MyModel` that inherits from the parent class `NpuModel`.

#### Example parent and child class

```python
# Parent class
class NpuModel:
    def __init__(self, *args, **kwargs):

    def run(self):
        return None

    def save(self):
        return None

    def load(self):
        return None

# Child class
class MyModel(NpuModel):
    def __init__(self):
        super().__init__()

    def prediction(self, x):
        out = self.model.predict(x)
        return out

    def run(self, x):
        out = self.prediction(x)
        return out
```

### Deliverable
Build on top of your previous API, the following:
- Build a function called `artifact`, found inside [init file](__init__.py) that will be used as decorator to pass 
  the required model to the parent class.
- Build a parent class called `NpuModel`, found inside [objects.py](objects.py) that will allow handling artifacts and distribute the compute defined on the child class.
- Build the pytorch and xgboost objects, called `PytorchModel` and `XgboostModel` respectively, found inside [frameworks.py](frameworks.py) that will provide any required info as to what type of object is and how to serialise it for your distributing API. 
- If the above is completed, [Pytorch example](pytorch_usage.py) and [Xgbost example](xgboost_usage.py) should work as expected.