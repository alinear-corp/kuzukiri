import unittest

import kuzukiri


class TestSimpleSplit(unittest.TestCase):
    def setUp(self) -> None:
        self.splitter = kuzukiri.Splitter()

    def test_split_line_normal_text(self):
        test_cases = [
            ("これはテスト文です。", ["これはテスト文です。"]),
            (
                "句点を起点として文分割します。2文あるテキストは2つに分割されるはずです。",
                [
                    "句点を起点として文分割します。",
                    "2文あるテキストは2つに分割されるはずです。",
                ]
            ),
            ("読点は、区切られません。", ["読点は、区切られません。"]),
            (
                "通常の句点だけでなくピリオドでも区切られるはずです．どうでしょうか．",
                [
                    "通常の句点だけでなくピリオドでも区切られるはずです．",
                    "どうでしょうか．",
                ]
            ),
            (
                "デフォルトでは改行記号は端なる文末記号のひとつです。したがって改行は文の区切りと\nみなします。改行記号は除去されません。",
                [
                    "デフォルトでは改行記号は端なる文末記号のひとつです。",
                    "したがって改行は文の区切りと\n",
                    "みなします。",
                    "改行記号は除去されません。",
                ]
            ),
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)

    def test_split_line_with_parentheses(self):
        test_cases = [
            ("これは「テスト文」です。", ["これは「テスト文」です。"]),
            (
                "括弧の中に句点（例えばこんな風に。）がある場合は無視。分割結果は2文です。",
                [
                    "括弧の中に句点（例えばこんな風に。）がある場合は無視。",
                    "分割結果は2文です。",
                ]
            ),
            (
                "会話文「こんにちは。」「ごきげんよう。」",
                ["会話文「こんにちは。」「ごきげんよう。」"]
            ),
            (
                "会話文2文「こんにちは。」「ごきげんよう。」は分割されない。ここで分割。",
                [
                    "会話文2文「こんにちは。」「ごきげんよう。」は分割されない。",
                    "ここで分割。",
                ],
            ),
            (
                "括弧の中に改行がある場合は「文の\n区切り」とみなしません。",
                [
                    "括弧の中に改行がある場合は「文の\n区切り」とみなしません。",
                ]
            ),
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)

    def test_split_max_length(self):
        example = "デフォルトでは1文が1000文字を超えた時点で強制的に文を切り分けます。"
        example += "@" * 2000
        actual = self.splitter.split(example)
        expected = [
            "デフォルトでは1文が1000文字を超えた時点で強制的に文を切り分けます。",
            "@" * 1000,
            "@" * 1000,
        ]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
