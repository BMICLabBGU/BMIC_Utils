import os

# from .pkg_info import __version__
from .info import long_description as __doc__
__doc__ +="""
Quickstart
==========

::
    import BMIC_Utils as bmu
    scan,affine = bmu.load_NII('my_scan.nii.gz',with_affine=True)
    
    seg_map = bmu.vox.get_3d_seg(scan, n_seg = 500)
    bmu.save_NII('my_segmap.nii.gz',affine)
"""

# Module imports
from . import common
from . import io
from . import vox
from . import vis

# object imports
from .common import autoArgs
from .io import json_read,json_write,yaml_read,yaml_write
from .vox import load_NII,save_NII
