# Preface:
        # Make sure to have conda installed on your computer to use pytorch
        # HOMEPATH ~ % bash Miniconda3-latest-MacOSX-x86_64.sh
        # HOMEPATH ~ % touch .bash_profile // Troubleshoot commands
        # HOMEPATH ~ % open ~/.bash_profile //Troubleshoot commands                
        # HOMEPATH ~ % source ~/.zshrc   // Troubleshoot commands

        #  conda install pytorch torchvision -c pytorch

        # To activate this environment for pytorch, use
        #
        #     $ conda activate env_pytorch 
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
      
        # python3

    
#########################################################################
# import the require libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import torch.optim as optim 
import numpy as np
import matplotlib.pyplot as plt # for plotting
from PIL import Image
from torch.autograd import Variable

#########################################################################
# Define a convolution neural network with layers conv1 -> pool -> conv2 -> pool -> flat
class CNN_classifier(nn.Module):
  def __init__(self):
    super(CNN_classifier, self).__init__()
    self.name = "CNN_classifier"
    self.conv1 = nn.Conv2d(3, 5, 5) # (num input channels, num output channels, kernel dim)
    self.pool = nn.MaxPool2d(2, 2) # #kernel_size, stride (reduce the image size by selecting a max value) (down sampling)
    self.conv2 = nn.Conv2d(5, 10, 5) 
    self.fc1 = nn.Linear(10 * 53 * 53, 64)
    self.fc2 = nn.Linear(64, 9) # 9 because 1 output per classssss!!!
  def forward(self, x):
    x = self.pool(F.relu(self.conv1(x))) #(img)->conv1->relu->pool
    x = self.pool(F.relu(self.conv2(x))) # (x)->conv2->relu->pool
    # 10 *53 * 53 = x now
    x = x.view(-1, 10 * 53 * 53) # flatten
    x = F.relu(self.fc1(x)) 
    x = self.fc2(x)
    return x
def predict_image(image):
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index
#########################################################################

#########################################################################
# Upload our image
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
# Ref from the current directory
im_path = "git/wavechord/SignLanguageDetectionCNN/ian.jpg"
im = Image.open(im_path)
#########################################################################

#########################################################################
# Upload our model
test_transforms = transforms.Compose([ transforms.Resize((224,224)), transforms.ToTensor()])
torch.manual_seed(8) # set the random seed

model = CNN_classifier()
device = torch.device("cuda" if torch.cuda.is_available() 
                                  else "cpu")
model.to(device)
use_cuda = False
if torch.cuda.is_available():
    model.cuda()
model_path =  "git/wavechord/SignLanguageDetectionCNN/bs32_lr0.001_epoch29/model_CNN_classifier_bs32_lr0.001_epoch29"
model.load_state_dict(torch.load(model_path), map_location=torch.device('cpu') )
model.eval()
# print our model parameters
print(model)
#########################################################################

#########################################################################
# predict our image
predict_image(im)
#########################################################################

