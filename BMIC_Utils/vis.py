from typing import Tuple
import pandas as pd
import numpy as np


def get_mri_indices(mri:np.ndarray) -> Tuple[int, int, int]:
    """
    Takes a 3D MRI scan as input and returns the (x, y, z) indices of the
    best channels to visualize in the scan.
    
    :param mri: A 3D MRI scan, which is a 3-dimensional array representing the 
                image data of the MRI scan
    :return: A tuple of three integers, which represent the x, y, and z indices 
                of the best channels to visualize in the given MRI image.
    """
    nz_indices = mri.nonzero()
    df = pd.DataFrame(np.array(nz_indices).T, columns=['x', 'y', 'z'])
    x_dy = df.groupby('x')['y'].agg(np.ptp)
    x_idx = int(x_dy.idxmax())

    y_dz = df.groupby('y')['z'].agg(np.ptp)
    y_idx = int(y_dz.idxmax())

    z_dx = df.groupby('z')['x'].agg(np.ptp)
    z_idx = int(z_dx.idxmax())
    return x_idx, y_idx, z_idx