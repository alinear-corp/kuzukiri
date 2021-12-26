use std::collections::{HashMap, HashSet};
use pyo3::prelude::*;
use crate::normalizers::{Normalizer, NormalizerPipeline};
use crate::segmenter::Segmenter;


/// Text Segmentation Class
#[pyclass(name="Segmenter")]
pub struct PySegmenter {
    _segmenter: Segmenter,
}

#[pymethods]
impl PySegmenter {
    /// Create a new Segmenter instance.
    ///
    /// Args:
    ///     terminals (Optional[set[str]]): a set of terminal characters (Default: {'。', '．', '，', '！', '？', '\n'})
    ///     parentheses (Optional[map[str, str]]): pairs of parentheses (Default: {'「': '」', '『': '』', '（': '）', '［': '］', '【': '】'})
    ///     force (Optional[set[str]]): a set of terminal characters, those ignore parentheses (Default: {})
    ///     max_buf_length (Optional[int]): max buffer size (Default: 1000)
    #[new()]
    fn new(
        terminals: Option<HashSet<char>>,
        parentheses: Option<HashMap<char, char>>,
        force: Option<HashSet<char>>,
        max_buf_length: Option<usize>,
    ) -> Self {
        PySegmenter {
            _segmenter: Segmenter::new(
                terminals,
                parentheses,
                force,
                max_buf_length,
            ),
        }
    }

    /// Execute text segmentation
    ///
    /// Args:
    ///     text (str) : target text
    /// Returns:
    ///     List[str] : list of segmented texts
    fn split(&self, text: String) -> Vec<String> {
        self._segmenter.split(text)
    }

    /// Execute text segmentation with normalization
    ///
    /// After splitting, NFKC normalization and trimming are performed.
    ///
    /// Args:
    ///     text (str) : target text
    /// Returns:
    ///     List[str] : list of segmented texts
    fn split_with_norm(&self, text: String) -> Vec<String> {
        let sentences = self._segmenter.split(text);
        let mut normalized: Vec<String> = Vec::with_capacity(sentences.len());
        for sentence in sentences.into_iter() {
            let n = NormalizerPipeline::normalize(sentence);
            if n != "" {
                normalized.push(n);
            }
        }
        normalized
    }
}
