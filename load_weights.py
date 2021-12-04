import os
import torch
import torch.nn as nn
from model import resnet34

def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

