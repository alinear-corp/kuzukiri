use std::collections::{HashMap, HashSet};
use pyo3::prelude::*;
use crate::splitter::Splitter;


#[pyclass(name="Splitter")]
pub struct PySplitter {
    _splitter: Splitter,
}

#[pymethods]
impl PySplitter {
    #[new()]
    fn new(
        terminals: Option<HashSet<char>>,
        parentheses: Option<HashMap<char, char>>
    ) -> Self {
        PySplitter {
            _splitter: Splitter::new(terminals, parentheses),
        }
    }

    fn split(&self, text: String) -> Vec<String> {
        self._splitter.split(text)
    }
}
