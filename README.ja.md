# kuzukiri
シンプルな文分割ツール

## これは何？
複数文からなる日本語文書を文ごとに分割するためのPythonライブラリです。

## 特徴
* シンプルなルールによる分割
  * 完全なルールベースです。機械学習等は使っていません
  * ルールがシンプルなので入力から結果を予測可能
* Rustで書かれているため高速 

## インストール
### PyPIからインストールする場合

```bash
pip install kuzukiri
```

### ソースコードからインストールする場合

```bash
pip install setuptools-rust
python setup.py install
```

## 使い方

```python
import kuzukiri

segmenter = kuzukiri.Segmenter()
text = "これはテストです。文分割します。"
sentences = segmenter.split(text)
print(sentences)  # => ['これはテストです。', '文分割します。']
```

詳細は `examples` ディレクトリまたは `tests` ディレクトリを参照してください。

## ライセンス
MIT

## 依存関係
* RustのコードをPythonから呼び出すために、 [PyO3](https://pyo3.rs) を利用しています。
* unicode正規化の処理は [unicode_normalization crate](https://docs.rs/unicode-normalization/latest/unicode_normalization/index.html) を利用しています。
