import re
import os
import setuptools

longDescription = """
It's supercalifragilisticexpialidocious
Even though the sound of it
Is something quite atrocious
If you say it loud enough
You'll always sound precocious
Supercalifragilisticexpialidocious
"""

# path constants
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# list of required dependencies
REQS_PATH = os.path.join(PROJECT_ROOT, 'requirements.txt')

with open(REQS_PATH, 'r') as rf:
    reqs = rf.read().splitlines()

# generate the version number
VERSIONFILE="PdfFieldFiller/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSIONFILE}.")

setuptools.setup(
        name='PdfFieldFiller',
        version=verstr,
        description='"PDF Form Field Filling Tool"',
        long_description=longDescription,
        author="Alex Buitron",
        author_email="alex@buitron.com",
        classifiers = [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        python_requires='>=3.6',
        install_requires=reqs,
        packages=["PdfFieldFiller"],
    )