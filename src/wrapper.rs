use pyo3::prelude::*;
use crate::splitter::Splitter;


#[pyclass(name="Splitter")]
pub struct PySplitter {
    _splitter: Splitter,
}

#[pymethods]
impl PySplitter {
    #[new]
    fn new() -> Self {
        PySplitter {
            _splitter: Splitter::new(),
        }
    }

    fn split(&self, text: String) -> Vec<String> {
        self._splitter.split(text)
    }
}
