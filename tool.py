import psutil

# RAM-Auslastung abfragen
mem = psutil.virtual_memory()
print(f"Gesamter RAM: {mem.total / (1024**3):.2f} GB")
print(f"Verfügbarer RAM: {mem.available / (1024**3):.2f} GB")
