from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="passtoken",
    version="0.1.0",
    rust_extensions=[RustExtension("passtoken.passtoken", binding=Binding.cpython)],
    packages=["passtoken"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)