import os

from setuptools import setup
from setuptools_rust import Binding, RustExtension

# reference: https://github.com/PyO3/setuptools-rust#setup
setup(
    name="kuzukiri",
    version="0.1.2",
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
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            "README.md",
        ), encoding="utf-8",
    ).read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/alinear-corp/kuzukiri",
        "Documentation": "https://alinear-corp.github.io/kuzukiri/",
    },
    license="MIT",
)
