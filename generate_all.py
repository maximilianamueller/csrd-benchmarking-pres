
import pandas as pd
import subprocess
import os

df = pd.read_excel("report_data.xlsx")
firm_names = df["name"].dropna().unique()

os.makedirs("pdfs", exist_ok=True)

for name in firm_names:
    safe = name.replace(" ", "_").replace("/", "-")
    print(f"Rendering: {name}")
    subprocess.run([
        "quarto", "render", "csrd_report.qmd",
        "--to", "pdf",
        "--output", f"pdfs/benchmarking_{safe}.pdf",
        "--execute-params", f'firm="{name}"'
    ])
     