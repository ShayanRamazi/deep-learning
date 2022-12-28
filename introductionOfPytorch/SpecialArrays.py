import torch

ones = torch.ones((2,3),dtype=torch.int8)
zeros = torch.zeros((1,3))
eyes = torch.eye(10)

eyes.fill_(1.6)
print(eyes)

empty = torch.empty((1,3))
empty.fill_(1.2)
print(empty)

print(torch.full((4,3,2),3.))

