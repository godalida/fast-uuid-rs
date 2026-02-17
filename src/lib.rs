use pyo3::prelude::*;
use rayon::prelude::*;
use uuid::Uuid;

/// Generates `n` UUID v4 strings in parallel.
#[pyfunction]
fn generate_uuid_v4(n: usize) -> Vec<String> {
    // Rayon handles parallel iterator creation and collection efficiently.
    // We use a parallel range (0..n) and map each index to a new UUID string.
    (0..n)
        .into_par_iter()
        .map(|_| Uuid::new_v4().to_string())
        .collect()
}

/// A Python module implemented in Rust.
#[pymodule]
fn fast_uuid(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_uuid_v4, m)?)?;
    Ok(())
}
