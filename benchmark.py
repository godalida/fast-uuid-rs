import time
import uuid
import pandas as pd
import polars as pl
import fast_uuid

COUNT = 1_000_000

print(f"Benchmarking UUID column creation for {COUNT:,} rows...\n")

# --- PANDAS ---
print("--- Pandas DataFrame ---")

# 1. Pandas Native (List Comprehension)
start = time.time()
df_pd = pd.DataFrame({'id': range(COUNT)})
df_pd['uuid'] = [str(uuid.uuid4()) for _ in range(COUNT)]
pd_time = time.time() - start
print(f"Pandas (Standard):  {pd_time:.4f} s")

# 2. Pandas + fast-uuid
start = time.time()
df_pd_fast = pd.DataFrame({'id': range(COUNT)})
df_pd_fast['uuid'] = fast_uuid.generate_uuid_v4(COUNT)
pd_fast_time = time.time() - start
print(f"Pandas (fast-uuid): {pd_fast_time:.4f} s")

print(f"Speedup: {pd_time / pd_fast_time:.1f}x\n")


# --- POLARS ---
print("--- Polars DataFrame ---")

# 3. Polars Native (map_elements is slow)
start = time.time()
df_pl = pl.DataFrame({'id': range(COUNT)})
df_pl = df_pl.with_columns(
    pl.col('id').map_elements(lambda _: str(uuid.uuid4()), return_dtype=pl.Utf8).alias('uuid')
)
pl_time = time.time() - start
print(f"Polars (Standard):  {pl_time:.4f} s")

# 4. Polars + fast-uuid
start = time.time()
df_pl_fast = pl.DataFrame({'id': range(COUNT)})
df_pl_fast = df_pl_fast.with_columns(
    pl.Series("uuid", fast_uuid.generate_uuid_v4(COUNT))
)
pl_fast_time = time.time() - start
print(f"Polars (fast-uuid): {pl_fast_time:.4f} s")

print(f"Speedup: {pl_time / pl_fast_time:.1f}x")
