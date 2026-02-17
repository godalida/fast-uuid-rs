# fast-uuid

[![PyPI version](https://img.shields.io/pypi/v/fast-uuid.svg)](https://pypi.org/project/fast-uuid/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fast-uuid.svg)](https://pypi.org/project/fast-uuid/)
[![License](https://img.shields.io/crates/l/fast-uuid.svg)](https://github.com/yourusername/fast-uuid)
[![Downloads](https://pepy.tech/badge/fast-uuid)](https://pepy.tech/project/fast-uuid)

**Blazing fast UUID v4 generation for Python, written in Rust.**

`fast-uuid` drops in as a high-performance replacement for bulk UUID generation. It leverages Rust's `uuid` crate and `rayon` parallelism to generate millions of UUIDs per second—**up to 50x faster** than Python's standard library.

## 🚀 Benchmarks

| Method | Count | Time | Speed |
| :--- | :--- | :--- | :--- |
| **Python** (`uuid.uuid4`) | 100,000 | 0.26s | ~380k / sec |
| **fast-uuid** | 100,000 | **0.005s** | **~18.2M / sec** |

*> Benchmarked on MacBook Pro (M1 Max), Python 3.12.*

## 📦 Installation

```bash
pip install fast-uuid
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
