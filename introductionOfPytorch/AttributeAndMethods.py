import torch

tensor_3d = torch.tensor([[[1,2,3],[3,5,4]]])
matrix = torch.tensor([[1,3],[5,8]])
print(tensor_3d.shape)
print(tensor_3d.size())
print(tensor_3d.max())

print(tensor_3d.float().mean())
print(tensor_3d.float().std())
print(matrix.t())

matrix = torch.tensor([[1.1,3],[5,8.6]])
matrix.ceil_()
print(matrix)