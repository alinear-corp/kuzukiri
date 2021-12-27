"""
kuzukiri is a rule-based text segmenter for Japanese.


## Example
```
import kuzukiri

segmenter = kuzukiri.Segmenter()
text = "これはテストです。文分割します。"
sentences = segmenter.split(text)
print(sentences)  # => ['これはテストです。', '文分割します。']
```
"""

from .kuzukiri import *  # noqa

__copyright__ = 'Copyright (C) ALINEAR Corporation'
__version__ = '0.1.1'
__license__ = 'MIT'
__author__ = "ALINEAR Corporation"
__url__ = "https://github.com/alinear-corp/kuzukiri"
