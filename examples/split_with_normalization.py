import kuzukiri


def main():
    segmenter = kuzukiri.Segmenter()
    text = " 文章の前後の空白スペースは除去されます。　ﾕﾆｺｰﾄﾞＮＦＫＣ正規化がなされます。"
    sentences = segmenter.split_with_norm(text)
    print(sentences)  # => ['文章の前後の空白スペースは除去されます。', 'ユニコードNFKC正規化がなされます。']


if __name__ == '__main__':
    main()
