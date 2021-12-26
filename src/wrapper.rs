use std::collections::{HashMap, HashSet};
use pyo3::prelude::*;
use crate::normalizers::{Normalizer, NormalizerPipeline};
use crate::segmenter::Segmenter;


#[pyclass(name="Segmenter")]
pub struct PySegmenter {
    _segmenter: Segmenter,
}

#[pymethods]
impl PySegmenter {
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

    fn split(&self, text: String) -> Vec<String> {
        self._segmenter.split(text)
    }

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
