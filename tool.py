import tkinter as tk
from tkinter import ttk
import psutil

def update_stats():
    # 1. RAM-Daten auslesen
    mem = psutil.virtual_memory()
    ram_total = mem.total / (1024**3)
    ram_avail = mem.available / (1024**3)
    ram_used_pct = mem.percent
    
    # 2. CPU-Daten auslesen (ohne Blockieren/Intervall, um die GUI flüssig zu halten)
    cpu_pct = psutil.cpu_percent()

    # 3. GUI-Labels und Fortschrittsbalken aktualisieren
    lbl_cpu.config(text=f"CPU-Auslastung: {cpu_pct}%")
    progress_cpu["value"] = cpu_pct

    lbl_ram.config(text=f"RAM: {ram_avail:.2f} GB frei von {ram_total:.2f} GB")
    progress_ram["value"] = ram_used_pct

    # 4. Diese Funktion nach 1000 Millisekunden (1 Sekunde) erneut aufrufen
    root.after(1000, update_stats)

# --- GUI Struktur aufbauen ---
root = tk.Tk()
root.title("XFCE System Monitor")
root.geometry("350x200")
root.resizable(False, False)

# Stil für ein modernes XFCE-Aussehen festlegen
style = ttk.Style()
style.theme_use("clam")

# Frame für Abstände (Padding)
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# CPU Sektion
lbl_cpu = ttk.Label(frame, text="CPU-Auslastung: 0%", font=("Helvetica", 11))
lbl_cpu.pack(anchor="w", pady=(0, 5))
progress_cpu = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress_cpu.pack(fill="x", pady=(0, 20))

# RAM Sektion
lbl_ram = ttk.Label(frame, text="RAM-Auslastung: 0%", font=("Helvetica", 11))
lbl_ram.pack(anchor="w", pady=(0, 5))
progress_ram = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress_ram.pack(fill="x", pady=(0, 10))

# Erste Aktualisierung starten
update_stats()

# Hauptschleife der GUI starten
root.mainloop()
