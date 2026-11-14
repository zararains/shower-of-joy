"""ai-happy-01 entry: "A Shower of Joy".

A laughing baby elephant sprays a sparkling shower of water over three
giggling ducklings. The program copies the bundled image to the output
path the grader sets (MAKEFUN_OUTPUT_DIR, or /output).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
print("wrote", TARGET)
