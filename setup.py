from setuptools import setup, Extension
from Cython.Distutils import build_ext

VERSION = "4"

cmd = { "build_ext": build_ext }
ext = Extension( "netfilterqueue", sources=["netfilterqueue.pyx",], libraries=["netfilter_queue"] )

setup(
    cmdclass            = cmd,
    ext_modules         = [ext],
    name                = "LibnetFilterQueue",
    version             = VERSION,
    license             = "MIT",
    author              = "Idone Rizzari",
    author_email        = "rizzaricreative@icloud.com",
    url                 = "https://github.com/idonerizzari/LibnetFilterQueue",
    description         = "Python bindings for netfilter_queue",
    long_description    = open("README.rst").read(),
    classifiers         = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
    ]
)
