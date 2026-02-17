import time
import uuid
import json
import pandas as pd
import polars as pl
import fast_uuid

# We'll test these row counts
SIZES = [100_000, 1_000_000, 10_000_000]
RESULTS = []

print(f"Benchmarking fast-uuid against standard methods...")

for count in SIZES:
    print(f"\n--- Testing with {count:,} rows ---")
    
    # 1. Pandas Native
    start = time.time()
    _ = [str(uuid.uuid4()) for _ in range(count)]
    pd_time = time.time() - start
    RESULTS.append({
        "size": count,
        "framework": "Pandas (Native)",
        "time_seconds": pd_time,
        "rows_per_second": count / pd_time
    })
    print(f"Pandas Native: {pd_time:.4f}s")

    # 2. Pandas + fast-uuid
    start = time.time()
    # fast-uuid generates a list of strings
    _ = fast_uuid.generate_uuid_v4(count)
    rust_time = time.time() - start
    RESULTS.append({
        "size": count,
        "framework": "Pandas + fast-uuid",
        "time_seconds": rust_time,
        "rows_per_second": count / rust_time
    })
    print(f"Pandas + fast-uuid: {rust_time:.4f}s")

    # 3. Polars Native (map_elements)
    # We construct a minimal DF to force the map execution
    df_pl = pl.DataFrame({'id': range(count)})
    start = time.time()
    _ = df_pl.with_columns(
        pl.col('id').map_elements(lambda _: str(uuid.uuid4()), return_dtype=pl.Utf8).alias('uuid')
    )
    pl_time = time.time() - start
    RESULTS.append({
        "size": count,
        "framework": "Polars (Native)",
        "time_seconds": pl_time,
        "rows_per_second": count / pl_time
    })
    print(f"Polars Native: {pl_time:.4f}s")

    # 4. Polars + fast-uuid
    # Polars can take the list directly or (even better) we'll support Arrow later
    # For now, list -> Series is the standard way
    start = time.time()
    _ = pl.Series("uuid", fast_uuid.generate_uuid_v4(count))
    pl_fast_time = time.time() - start
    RESULTS.append({
        "size": count,
        "framework": "Polars + fast-uuid",
        "time_seconds": pl_fast_time,
        "rows_per_second": count / pl_fast_time
    })
    print(f"Polars + fast-uuid: {pl_fast_time:.4f}s")

# Save detailed JSON for visualization
with open("benchmark_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2)

print("\nSaved detailed results to benchmark_results.json")
