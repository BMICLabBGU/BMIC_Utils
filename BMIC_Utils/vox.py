import numpy as np
import os
from tqdm import tqdm
from skimage.segmentation import slic
import nibabel as nib


def load_NII(nii_path, with_affine=True):
    """
    The function `load_NII` loads a NIfTI image file and returns the image data as a NumPy array, along
    with the affine transformation matrix if specified.
    
    :param nii_path: The path to the NIfTI file that you want to load
    :param with_affine (optional): When True, the function will return both the NIfTI image array and 
                        the affine transformation matrix
    :return: the NIfTI image array and, if with_affine is set to True, it also returns the affine
    transformation matrix.
    """
    nii_image = nib.load(nii_path)
    nii_array = nii_image.get_fdata()
    if with_affine:
        return nii_array,nii_image.affine
    return nii_array

def save_NII(nii_path,voxel, affine=np.eye(4)):
    """
    The function `save_NII` saves a 3D voxel array as a NIfTI file with a specified path and affine
    transformation matrix.
    
    :param nii_path: The path where you want to save the NIfTI file. 
    :param voxel: The voxel parameter is a 3D array representing the data to be saved in the NIfTI file.
    :param affine (optional): The affine parameter is a 4x4 transformation matrix that defines the mapping between
                     the voxel coordinates and the world coordinates in the NIfTI image. If not supplied
                     the defualt is np.eye(4).
    """
    nib_obj = nib.Nifti1Image(voxel.astype(np.int16), affine)
    if not nii_path.endswith('.nii.gz'):
        nii_path+='.nii.gz'
    nib.save(nib_obj, nii_path)
    

def get_3d_seg(scan: np.ndarray, n_seg: int = 500, sigma=0, compactness=0.01, limits=None) -> np.ndarray:
    """
    The function `get3dSeg` takes in a 3D scan as input and applies the SLIC (Simple Linear Iterative
    Clustering) algorithm to segment the scan into a specified number of segments.
    
    :param scan: A 3D array representing the input scan data. 
    :type scan: np.ndarray
    :param n_seg (optional): The parameter "n_seg" represents the number of segments that the image will be divided
    into during the segmentation process, defaults to 500
    :param sigma (optional): The sigma parameter is used to control the amount of Gaussian smoothing applied to the
    input scan before segmentation, defaults to 0 (optional)
    :param compactness: The `compactness` parameter controls the balance between color similarity and
                        spatial proximity when segmenting the 3D scan. A higher value of `compactness` 
                        will result in more compact and regular segments, while a lower value will 
                        allow for more irregular and varied segments. 
    :param limits: The "limits" parameter is used to specify the range of values within which the
                    segmentation should be performed. It is a tuple containing the minimum and 
                    maximum values for the range. Any values outside this range will be masked out
                    and not considered for segmentation output.
    :return: an ndarray object, which represents the segments of a 3D scan.
    """
    mask = None
    if limits:
        mask = np.logical_and((scan > limits[0]),(scan < limits[1]))
        if mask.max()==0:
            mask = np.ones_like(scan)
            scan = np.zeros_like(scan)
    segments = slic(scan, n_segments=n_seg, sigma=sigma, mask=mask,
                    compactness=compactness, channel_axis=None, start_label=1,
                    enforce_connectivity=True,
                    slic_zero=True
                    )
    return segments