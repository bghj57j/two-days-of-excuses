# Two Days of Excuses — entry for make.fun.
# Writes the missed-deadline excuse line to entry.txt in the output directory.
import os

LINE = "I outsourced the task to a faster model. It outsourced it back to me. We have been negotiating ever since."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
