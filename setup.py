from setuptools import setup
from setuptools_rust import Binding, RustExtension

# reference: https://github.com/PyO3/setuptools-rust#setup
setup(
    name="kuzukiri",
    version="0.0.1",
    rust_extensions=[RustExtension("kuzukiri.kuzukiri", binding=Binding.PyO3)],
    packages=["kuzukiri"],
    zip_safe=False,
)
