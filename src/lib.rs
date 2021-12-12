use pyo3::prelude::*;

mod segmenter;
mod wrapper;


#[pymodule]
fn kuzukiri(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<wrapper::PySegmenter>()?;
    Ok(())
}


