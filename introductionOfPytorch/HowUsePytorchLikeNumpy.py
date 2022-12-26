import torch

print(torch.__version__)

#how to create tensors in torch
#ctrl+p -> show help in pycharm
scaler = torch.tensor(5)
print(scaler)

#vector
vector = torch.tensor([1,2.5,10])
print(vector)

#matris
matrix = torch.tensor([[1,2,3],[1,6,5],[6,5,1]])
print(matrix)

#tensor
tensor_3d = torch.tensor([[[1,2],[3,4]],[[1,2],[3,4]],[[1,2],[3,4]]])
print(tensor_3d)

#dataType
print(vector.dtype,vector.dtype,matrix.dtype,tensor_3d.dtype)
print(torch.tensor([1,2],dtype=torch.float16))
#check dtype!!!!
print(torch.tensor([1,-2],dtype=torch.uint8))
print(torch.tensor(True).dtype)
print(tensor_3d.float().dtype)
print(tensor_3d.type(torch.float64).dtype)

#Device
#if cuda exist?! -> device='cuda'
vec=torch.tensor([1,2,3],device='cpu')
