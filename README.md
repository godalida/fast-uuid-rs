<div align="center">

# fast-uuid-rs

[![PyPI version](https://img.shields.io/pypi/v/fast-uuid-rs.svg)](https://pypi.org/project/fast-uuid-rs/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fast-uuid-rs.svg)](https://pypi.org/project/fast-uuid-rs/)
[![License](https://img.shields.io/github/license/godalida/fast-uuid-rs?color=white)](https://github.com/godalida/fast-uuid-rs)
[![Downloads](https://pepy.tech/badge/fast-uuid-rs)](https://pepy.tech/project/fast-uuid-rs)

**Blazing fast UUID v4 generation for Python, written in Rust.**

</div>

`fast-uuid-rs` drops in as a high-performance replacement for bulk UUID generation. It leverages Rust's `uuid` crate and `rayon` parallelism to generate millions of UUIDs per second—**up to 50x faster** than Python's standard library.

## 🚀 Benchmarks

**Real-world performance on 10,000,000 rows:**

| Framework | Method | Time (10M rows) | Rows / sec | Speedup |
| :--- | :--- | :--- | :--- | :--- |
| **Pandas** | Standard `uuid.uuid4()` | 37.97s | ~263k | 1x |
| **Pandas** | **fast-uuid** | **1.25s** | **~8.0M** | **30x ⚡** |
| | | | | |
| **Polars** | Standard `.map_elements()` | 39.30s | ~254k | 1x |
| **Polars** | **fast-uuid** | **1.31s** | **~7.7M** | **30x ⚡** |

*> Benchmarks run on GitHub Actions (Ubuntu runner).*

## 📦 Installation

```bash
pip install fast-uuid-rs
```

## ⚡ Usage

Generate a list of UUID strings in parallel.

```python
import fast_uuid

# Generate 1 million UUIDs
uuids = fast_uuid.generate_uuid_v4(1_000_000)

# Returns: ['c3a4d...', 'a1b2c...', ...]
print(f"Generated {len(uuids)} UUIDs instantly.")
```

## 💡 Why is it so fast?

Python's `uuid` module is robust but slow for bulk operations due to:
1. **Object Overhead:** Creating a full `UUID` object for every ID.
2. **The GIL:** Python cannot utilize all CPU cores for generation.
3. **Memory Allocation:** Resizing lists dynamically.

**fast-uuid** solves this by:
- **Releasing the GIL:** All work happens in Rust, allowing true parallelism.
- **Rayon Parallelism:** Utilizes all available CPU cores automatically.
- **Zero-Copy (Internal):** Pre-allocates memory for the exact number of strings needed.

## 🛠️ Development

Requires [Rust](https://rustup.rs/) and `maturin`.

```bash
# Install development dependencies
pip install maturin

# Build and install locally (optimized)
maturin develop --release
```

## 📄 License

MIT
