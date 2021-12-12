use pyo3::prelude::*;

mod splitter;
mod wrapper;


#[pymodule]
fn kuzukiri(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<wrapper::PySplitter>()?;
    Ok(())
}


