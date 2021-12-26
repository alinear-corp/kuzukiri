from setuptools import setup
from setuptools_rust import Binding, RustExtension

# reference: https://github.com/PyO3/setuptools-rust#setup
setup(
    name="kuzukiri",
    version="0.1.0",
    rust_extensions=[RustExtension("kuzukiri.kuzukiri", binding=Binding.PyO3)],
    packages=["kuzukiri"],
    zip_safe=False,
    classfiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Japanese",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Rust",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Text Processing",
    ],
    keywords=[
        "NLP", "Natural Language Processing",
        "Text Segmentation", "Python", "Rust",
        "Japanese", "Preprocessing",
        "Text Processing",
    ],
    platforms=["Windows", "Linux", 'macOS'],
)
