import sys
import os

try:
    from setuptools import setup, find_packages
    from setuptools.dist import Distribution
    from setuptools.extension import Extension
except ImportError:
    from distutils.core import setup
    from distutils.core import Distribution
    from distutils.extension import Extension
    
try:
    import numpy
    from Cython.Distutils import build_ext
except ImportError:
    Distribution().fetch_build_eggs(['Cython', 'numpy'])
    import numpy
    from Cython.Distutils import build_ext
    
prjdir = os.path.dirname(__file__)


def read(filename):
    return open(os.path.join(prjdir, filename)).read()


extra_link_args = []
libraries = []
library_dirs = []
include_dirs = []
exec(open('version.py').read())

if sys.platform.startswith('linux'):
    e_c_a = ['-fopenmp', '-O2']
    e_l_a = ['-fopenmp']
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    e_c_a = ['-openmp', '-O2']
    e_l_a = ['-openmp']

setup(
    name='eif',
    version=__version__,
    author='Matias Carrasco Kind , Sahand Hariri, Seng Keat Yeoh',
    author_email='mcarras2@illinois.edu',
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("eif",
                 sources=["_eif.pyx", "eif.cxx"],
                 include_dirs=[numpy.get_include()],
                 extra_compile_args=e_c_a,
                 extra_link_args=e_l_a,
                 language="c++")],
    scripts=[],
    py_modules=['eif_old', 'version'],
    packages=[],
    license='License.txt',
    include_package_data=True,
    description='Extended Isolation Forest for anomaly detection',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/sahandha/eif',
    install_requires=["numpy", "cython"],
)
