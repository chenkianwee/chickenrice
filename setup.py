import sys

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Testapp requires python >= 3.6")

from setuptools import find_packages, setup

REQUIRES = [
    'pyqtgraph',
    'PyOpenGL',
]

setup(
    # basic package metadata
    name='chickenrice',
    version= 0.10,
    description='chicken rice app',
    long_description="chicken rice app",
    license='GPL3',
    author='authorx',
    author_email='authorx@email.com',
    url='chickenrice.comx',
    classifiers="test",

    # details needed by setup
    install_requires=REQUIRES,
    python_requires=">=3.6",
    packages=find_packages(),
    package_data={},
    entry_points={'gui_scripts': ['chickenrice = chickenrice.__main__:main']},
)