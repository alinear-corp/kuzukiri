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
