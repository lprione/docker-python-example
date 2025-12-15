import argparse
from pathlib import Path

import numpy as np


def compute(n: int = 10) -> np.ndarray:
    """Return squares 0..n-1 (small stand-in for a processing step).

    Keeping this function pure (no I/O) makes it easy to test and to plug into
    larger facility-style pipelines.
    """
    x = np.arange(n)
    return x ** 2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Minimal Dockerized Python processing step (example)."
    )
    parser.add_argument(
        "--n",
        type=int,
        default=10,
        help="Number of values (default: 10).",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="",
        help="Optional output path (writes a small text report).",
    )
    args = parser.parse_args()

    result = compute(args.n)
    print("Result:", result)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(map(str, result.tolist())) + "\n", encoding="utf-8")
        print(f"Wrote report to: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
