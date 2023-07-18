""" Define distribution parameters for BMIC_Utils, including package version

The long description parameter is used to fill settings in setup.py, the
BMIC_Utils top-level docstring, and in building the docs.
We exec this file in several places, so it cannot import BMIC_Utils or use
relative imports.
"""

# nibabel version information
# This is a fall-back for versioneer when installing from a git archive.
# This should be set to the intended next version + dev to indicate a
# development (pre-release) version.
_version_major = 0
_version_minor = 0
_version_micro = 0
_version_extra = '.dev0'

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
VERSION = f"{_version_major}.{_version_minor}.{_version_micro}{_version_extra}"


# Note: this long_description is the canonical place to edit this text.
# It also appears in README.rst, but it should get there by running
# ``tools/refresh_readme.py`` which pulls in this version.
# We also include this text in the docs by ``..include::`` in
# ``docs/source/index.rst``.
long_description = """
=======
BMIC_Utils
=======

Useful functions for BioMedical Imaging DL research

Website
=======

TBA

Mailing Lists
=============

Please send any questions or suggestions to the `BMICLabBGU@gmail.com`

Code
====

TBA

License
=======

BMIC_Utils is licensed under the terms of the MIT license. Some code included
with nibabel is licensed under the BSD license.  Please see the COPYING file
in the BMIC_Utils distribution.

Citing BMIC_Utils
==============

Please see the `available releases`_ for the release of BMIC_Utils that you are
using.  Recent releases have a Zenodo_ `Digital Object Identifier`_ badge at
the top of the release notes.  Click on the badge for more information.

.. _zenodo: https://zenodo.org
.. _Digital Object Identifier: https://en.wikipedia.org/wiki/Digital_object_identifier
"""
