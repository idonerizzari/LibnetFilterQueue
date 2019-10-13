from distutils.core import setup, Extension
from Cython.Distutils import build_ext

VERSION = "3"

cmd = { "build_ext": build_ext }
ext = Extension( "libnetfilterqueue", sources=["libnetfilterqueue.pyx",], libraries=["netfilter_queue"], )

setup(
    cmdclass = cmd,
    ext_modules = [ext],
    name="LibnetFilterQueue",
    version=VERSION,
    license="MIT",
    author="Idone Rizzari",
    author_email="rizzaricreative@icloud.com",
    url="https://github.com/idonerizzari/LibnetFilterQueue",
    description="Python bindings for libnetfilter_queue",
    long_description=open("README.rst").read(),
    download_url="http://pypi.python.org/packages/source/N/LibnetFilterQueue/LibnetFilterQueue-%s.tar.gz" % VERSION,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
    ]
)
