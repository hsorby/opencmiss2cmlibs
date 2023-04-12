OpenCMISS 2 CMLibs
==================

This tool is meant to help update code from using OpenCMISS python packages to CMLibs python packages.

Install with::

  pip install opencmiss2cmlibs

Usage::

  opencmiss2cmlibs <directory-of-python-packge-to-update>

This displays a diff of the changes on *stdout*.
To make the changes in-place and not create a backup file use::

  opencmiss2cmlibs -w -n <directory-of-python-packge-to-update>

This form of the command is best suited for use with code that is under version control, Git or the like.
