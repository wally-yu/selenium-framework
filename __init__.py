import sys
import os

SUPPORTED_VERSIONS = [(3, 6), (3, 5)]

python_major_version = sys.version_info[0]
python_minor_version = sys.version_info[1]

if (python_major_version, python_minor_version) not in SUPPORTED_VERSIONS:
    formatted_supported_versions = ['{}.{}'.format(mav, miv) for mav, miv in SUPPORTED_VERSIONS]
    err_msg = 'This version of Python ({}.{}) is not supported!\n'.format(python_major_version, python_minor_version) +\
              'Selenium Framework only tested under the following versions of ' \
              'Python for now: {}'.format(formatted_supported_versions)
    raise RuntimeError(err_msg)


# Guildlines to upload project to pypi:
# https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
# upload:  twine upload dist/*
