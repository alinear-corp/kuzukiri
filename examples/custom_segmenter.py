import kuzukiri


def main():
    segmenter = kuzukiri.Segmenter(
        terminals={"."},
        parentheses={"(": ")"},
        force={"\n"},
    )
    text = "半角ピリオド.(括弧も半角のみ.)(括弧内に改行\nがある場合は強制的に分割)"
    sentences = segmenter.split(text)
    print(sentences)  # => ['半角ピリオド.', '(括弧も半角のみ.)(括弧内に改行\n', 'がある場合は強制的に分割)']


if __name__ == '__main__':
    main()
