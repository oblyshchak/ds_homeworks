import torch 
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt
from torch import optim
import torchviz

nX, nH, nY, nZ = 2, 5, 1, 6

class ThreeLayersNet(nn.Module):
    def __init__(self, nX, nH, nY, nZ):
        super().__init__()
        
        self.layer_1 = nn.Linear(nX, nH)
        self.layer_2 = nn.Linear(nH, nY)
        self.layer_out = nn.Linear(nY, nZ)
        
        self.activate_1 = nn.Sigmoid()
        self.activate_2 = nn.ReLU()
        self.activate_out = nn.Sigmoid()
        
    def forward(self, X):
        X = self.activate_1(self.layer_1(X))
        X = self.activate_2(self.layer_2(X))
        X = self.activate_out(self.layer_out(X))
        return X
    
def fit(model, X, Y, batch_size = 100, train = True):
    model.train(train)
    sumMSE, sumA, numB = 0, 0, int(len(X)/batch_size)
    for i in range(0, numB*batch_size, batch_size):
        xb = X[i: i+batch_size]
        yb = Y[i: i+batch_size]
        y = model(xb)
        mse_tensor = mse(y, yb)
        
        if train:
            optimizer.zero_grad()
            mse_tensor.backward()
            optimizer.step()
        
        sumMSE += mse_tensor.item()
        sumA += (y.round() == yb).float().mean()
    
    return sumMSE/numB, sumA/numB


X = torch.randn(1200, 2)

def interesting_function(x):
    y = (torch.sin(x[:, 0]) + torch.cos(x[:, 1]**2)).float().view(-1,1)
    return y

Y_test = interesting_function(X)

plt.scatter(X.numpy()[:, 0], X.numpy()[:, 1], c=Y_test.numpy())
plt.show()

def homework_function(x):
    y = (torch.sum((x - 0.5)**2, axis=1) < 0.1).float().view(-1,1)
    return y

Y_home = homework_function(X)

plt.scatter(X.numpy()[:, 0], X.numpy()[:, 1], c=Y_home.numpy())
plt.show()

model = ThreeLayersNet(nX, nH, nY, nZ)
mse = nn.MSELoss()  
optimizer = optim.Adam(model.parameters(), lr=0.001)


print( "before:      loss: %.4f accuracy: %.4f" %  fit(model, X,Y_test) )
 
epochs = 1000                                            
for epoch in range(epochs):                              
    MSE_test, A_test = fit(model, X, Y_test)
    MSE_home,A = fit(model, X, Y_home)                               
     
    if epoch % 100 == 0 or epoch == epochs-1:                 
        print(f'TEST epoch: {epoch:5d} MSE_test: {MSE_test:.4f} accuracy: {A_test:.4f}' )
        print(f'HOMEWORK epoch: {epoch:5d} MSE_home: {MSE_home:.4f} accuracy: {A:.4f}' ) 
        

torchviz.make_dot(model(X), params=dict(model.named_parameters()))