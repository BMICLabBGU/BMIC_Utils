from numpy.typing import ArrayLike
from torch import nn
import torch.functional as F
import numpy as np
from scipy.spatial.distance import cdist


# The DiceLoss class is a PyTorch module that calculates the Dice loss for semantic segmentation
# tasks.
class DiceLoss(nn.Module):
    def __init__(self, smooth:int=1) -> None:
        super(DiceLoss, self).__init__()
        self.smooth = smooth

    def forward(self, input:ArrayLike, target:ArrayLike):
        input = F.sigmoid(input)

        input = input.view(-1)
        target = target.view(-1)

        intersection = (input * target).sum()
        dice = (2 * intersection + self.smooth) / (
            input.sum() + target.sum() + self.smooth
        )

        return 1 - dice

# The DiceScore class is used to calculate the score of a dice roll.
class DiceScore():
    def __init__(self,smooth=1) -> None:
        self.smooth=smooth
    
    def __call__(self, input:ArrayLike, target:ArrayLike)-> float:
        intersection = (input*target).sum()
        
        dice = (2*intersection+self.smooth)/(
            input.sum()+target.sum()+self.smooth
        )
        
        return dice
    
def Hausdorff3D(input,target):
    points1 = np.transpose(np.nonzero(input))
    points2 = np.transpose(np.nonzero(target))
    distances = cdist(points1, points2)
    
    hd_dist1 = np.max(np.min(distances,axis=1))
    hd_dist2 = np.max(np.min(distances,axis=0))
    
    return max(hd_dist1,hd_dist2)