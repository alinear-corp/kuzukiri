import unittest

import kuzukiri


class TestBufLength(unittest.TestCase):
    def setUp(self) -> None:
        self.segmenter = kuzukiri.Segmenter(max_buf_length=7)

    def test_buf_length(self):
        example = "1234567890"
        actual = self.segmenter.split(example)
        expected = [
            "1234567",
            "890",
        ]
        self.assertEqual(actual, expected)

    def test_buf_length_by_wrong_paren(self):
        example = "1（23)4567890"
        actual = self.segmenter.split(example)
        expected = [
            "1（23)45",
            "67890",
        ]
        self.assertEqual(actual, expected)

    def test_buf_length_by_wrong_paren_ignore_terminal(self):
        example = "1（2。3)4567890"
        actual = self.segmenter.split(example)
        expected = [
            "1（2。3)4",
            "567890",
        ]
        self.assertEqual(actual, expected)

    def test_buf_length_by_wrong_paren_clear_stack(self):
        example = "1（2。3)456。7890"
        actual = self.segmenter.split(example)
        expected = [
            "1（2。3)4",
            "56。",
            "7890",
        ]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
