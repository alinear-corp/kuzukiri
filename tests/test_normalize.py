import unittest

import kuzukiri


class TestSplitWithNormalization(unittest.TestCase):
    def setUp(self) -> None:
        self.segmenter = kuzukiri.Segmenter()

    def test_split_line_normal_text(self):
        test_cases = [
            (
                " 文章の前後の空白スペースは除去されます。　",
                ["文章の前後の空白スペースは除去されます。"],
            ),
            (
                "ﾕﾆｺｰﾄﾞの正規化がなされているかも注意してください。ＣＭは③ﾁｬﾝﾈﾙで映画予告編、１５００Ｍの旅です。",
                [
                    "ユニコードの正規化がなされているかも注意してください。",
                    "CMは3チャンネルで映画予告編、1500Mの旅です。",
                ]
            ),
            (
                "改行記号\nも除去されます。",
                ["改行記号", "も除去されます。"],
            ),
        ]
        for example, expected in test_cases:
            actual = self.segmenter.split_with_norm(example)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
