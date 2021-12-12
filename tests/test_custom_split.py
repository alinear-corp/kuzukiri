import unittest

import kuzukiri


class TestCustomSplit(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_terminals = {"."}
        self.custom_parens = {"(": ")"}
        self.splitter = kuzukiri.Splitter(
            self.custom_terminals,
            self.custom_parens,
            force=set("\n"),
        )

    def test_split_line_normal_text(self):
        test_cases = [
            ("これはテスト文です。", ["これはテスト文です。"]),
            ("これはテスト文です.", ["これはテスト文です."]),
            (
                "句点を指定した場合、指定した句点以外のみが認識されます。このテストではピリオドのみを指定したため全角の句点は認識されません。",
                [
                    "句点を指定した場合、指定した句点以外のみが認識されます。このテストではピリオドのみを指定したため全角の句点は認識されません。",
                ]
            ),
            (
                "指定した句点で区切ってある場合,そこで分割されます.ここで分割.",
                [
                    "指定した句点で区切ってある場合,そこで分割されます.",
                    "ここで分割.",
                ]
            ),
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)

    def test_split_line_with_parentheses(self):
        test_cases = [
            (
                "括弧を明示的に指定した場合は,指定した括弧のみが認識されます.したがって、(このように.)指定した括弧内に句点があっても無視されます.",
                [
                    "括弧を明示的に指定した場合は,指定した括弧のみが認識されます.",
                    "したがって、(このように.)指定した括弧内に句点があっても無視されます.",
                ]
            ),
            (
                "括弧を明示した場合,未指定の括弧は認識されません.（たとえばこの括弧.）です。",
                [
                    "括弧を明示した場合,未指定の括弧は認識されません.",
                    "（たとえばこの括弧.",
                    "）です。",
                ]
            ),
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)

    def test_force_split(self):
        test_cases = [
            (
                "引数forceを指定した場合は\n指定した文字が現れると強制的に分割します。",
                [
                    "引数forceを指定した場合は\n",
                    "指定した文字が現れると強制的に分割します。",
                ]
            ),
            (
                "forceに指定した文字は（括弧内に\nあっても）分割されます。",
                [
                    "forceに指定した文字は（括弧内に\n",
                    "あっても）分割されます。",
                ]
            ),
        ]
        for example, expected in test_cases:
            actual = self.splitter.split(example)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
