import neuro-pipeline as pipe
from neuro-pipeline.objects import NpuModel
from neuro-pipeline.frameworks import PytorchModel

import torch

net = torch.nn.Sequential(
    torch.nn.Linear(4, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 1))

x = torch.rand((2, 4), requires_grad=False)

@pipe.artifacts([PytorchModel('model')])
class MyModel(NpuModel):
    def __init__(self):
        super().__init__()

    def prediction(self, x):
        out = self.model(x)
        return out

    def run(self, x):
        out = self.prediction(x)
        return out

model = MyModel()
model.artifacts({'model': net})

out = model.run(x)