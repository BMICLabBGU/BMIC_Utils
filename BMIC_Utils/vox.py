import numpy as np
import os
from tqdm import tqdm
from skimage.segmentation import slic
import nibable as nig


def loadNII(nii_path, with_affine=True):
    nii_image = nib.load(nii_path)
    nii_array = nii_image.get_fdata()
    if with_affine:
        return nii_array,nii_image.affine
    return nii_array

def saveNII(nii_path,voxel, affine=np.eye(4)):
    nib_obj = nib.Nifti1Image(voxel.astype(np.int16), affine)
    nib.save(nib_obj, nii_path)
    

def get3dSeg(
    scan: np.ndarray,
    n_seg: int = 500,
    sigma=10,
    compactness=0.01,
    limits=None,
    min_size=0.5,
) -> np.ndarray:
    
    mask = None
    if limits:
        mask = (scan > limits[0]) * (scan < limits[1])
    if mask.max() == 0:
        mask = np.ones_like(scan)
        scan = np.zeros_like(scan)
    segments = slic(
        scan,
        n_segments=n_seg,
        sigma=sigma,
        mask=mask,
        compactness=compactness,
        channel_axis=None,
        start_label=1,
        min_size_factor=min_size,
    )
    return segments


def segmentCT(files, out_fld, n_seg, limits):
    for f_path in tqdm(files):
        full_path = os.path.join(in_fld, f_path)

        scan, affine = loadNII(full_path)
        # print("Size:", scan.shape)
        seg_map = get3dSeg(
            scan, sigma=0, compactness=0.01, n_seg=n_seg, limits=limits, min_size=0.1
        )
        saveNII(os.path.join(out_fld, f_path), seg_map, affine)
    return len(files)
