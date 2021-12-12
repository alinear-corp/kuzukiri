use std::collections::{HashMap, HashSet};
use pyo3::prelude::*;
use crate::splitter::Segmenter;


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
}
