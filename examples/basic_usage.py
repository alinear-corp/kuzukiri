import kuzukiri


def main():
    segmenter = kuzukiri.Segmenter()
    text = "これはテストです。文分割します。"
    sentences = segmenter.split(text)
    print(sentences)  # => ['これはテストです。', '文分割します。']


if __name__ == '__main__':
    main()
