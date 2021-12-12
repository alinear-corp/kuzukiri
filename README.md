[日本語](https://github.com/alinear-corp/kuzukiri/blob/main/README.ja.md)

# kuzukiri
A simple text segmenter

## What's this?
This is a python library for text segmentation of Japanese text.

## Features
* Text segmentation by simple rules,
  * rule-based, no machine learning, 
  * so you can assume results.
* comparably fast. It's written in rust-lang.

## Install
### from source code

```bash
pip install setuptools-rust
python setup.py install
```

## Usage

```python
import kuzukiri

segmenter = kuzukiri.Segmenter()
text = "これはテストです。文分割します。"
sentences = segmenter.split(text)
print(sentences)  # => ['これはテストです。', '文分割します。']
```

For details, see `examples` and `tests` directories.

## License
MIT

## Dependencies
* [PyO3](https://pyo3.rs) : to compile rust code for python.
* [unicode_normalization crate](https://docs.rs/unicode-normalization/latest/unicode_normalization/index.html) : for NFKC normalization
