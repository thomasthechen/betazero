'''
@author George Hotz
'''
import numpy as np 
import torch
import torch.nn as nn
import torch.nn.functional as F 
from torch.utils.data import Dataset 
from torch import optim


import numpy as np 
import torch
import torch.nn as nn
import torch.nn.functional as F 
from torch.utils.data import Dataset 
from torch import optim


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # in: 13 by 8 by 5
        self.a1 = nn.Conv2d(13, 16, kernel_size=3, padding=1)
        self.a2 = nn.Conv2d(16, 16, kernel_size=3, padding=1)
        self.a3 = nn.Conv2d(16,32, kernel_size=3, stride=2)

        self.b1 = nn.Conv2d(32,32,kernel_size=3, padding = 1)
        self.b2 = nn.Conv2d(32,32,kernel_size=3, padding = 1)
        self.b3 = nn.Conv2d(32,64, kernel_size=3, stride=2)

        self.c1 = nn.Conv2d(64, 64, kernel_size=2, padding=1)
        self.c2 = nn.Conv2d(64, 64, kernel_size=2, padding=1)
        self.c3 = nn.Conv2d(64, 128, kernel_size=2, stride=2)

        self.d1 = nn.Conv2d(128, 128, kernel_size=1)
        self.d2 = nn.Conv2d(128, 128, kernel_size=1)
        self.d3 = nn.Conv2d(128, 128, kernel_size=1)

        self.last = nn.Linear(128, 2)

    def forward(self, x):
        x = F.relu(self.a1(x))
        x = F.relu(self.a2(x))
        x = F.relu(self.a3(x))

        x = F.relu(self.b1(x))
        x = F.relu(self.b2(x))
        x = F.relu(self.b3(x))

        x = F.relu(self.c1(x))
        x = F.relu(self.c2(x))
        x = F.relu(self.c3(x))

        x = F.relu(self.d1(x))
        x = F.relu(self.d2(x))
        x = F.relu(self.d3(x))



        x = x.view(-1, 128)
        
        x = self.last(x)

        
        x1 = x[:, 0]
        x2 = x[:, 1]
        x1 = torch.sigmoid(x1)

        return x1 * x2