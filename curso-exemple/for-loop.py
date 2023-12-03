import time

start = time.perf_counter()
for i in range(5000):
    continue

elapsed_time = (time.perf_counter() - start) * 1000  # Convertendo para milissegundos

print(f"Took in {elapsed_time:.2f} ms")
