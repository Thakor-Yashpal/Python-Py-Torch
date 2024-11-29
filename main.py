import torch
import numpy as np

print(torch.__version__)
torch.cuda.is_available()

x = torch.rand(5, 3)
print(x)
