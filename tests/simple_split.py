import unittest

import kuzukiri


class MyTestCase(unittest.TestCase):
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
            (
                "通常の句点だけでなくピリオドでも区切られるはずです．どうでしょうか．",
                [
                    "通常の句点だけでなくピリオドでも区切られるはずです．",
                    "どうでしょうか．",
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
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
