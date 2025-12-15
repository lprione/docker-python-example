# Docker Python Example

A minimal, **reproducible** pattern for running Python processing steps in a shared research environment.

This repo is intentionally small: it demonstrates how to package a Python script + dependencies + tests so it runs
the same way on any machine. That is exactly what you want in a facility workflow, where “it works on my laptop”
is not an acceptable QA strategy.

## What’s inside

- Python 3.10
- NumPy
- Pytest
- GitHub Actions CI (runs tests on every push/PR)

## Why this matters in a research facility

- **Reproducibility:** the same container runs on laptops, workstations, and servers.
- **Isolation:** dependencies are pinned and do not contaminate other software on shared machines.
- **Handover-friendly:** a colleague can run your processing step with one command, without tribal knowledge.

## Quickstart

### Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python app.py
pytest
```

### Run with Docker

Build:

```bash
docker build -t docker-python-example .
```

Run:

```bash
docker run --rm docker-python-example
```

Run with parameters:

```bash
docker run --rm docker-python-example python app.py --n 20
```

Write a small report to a mounted folder:

```bash
mkdir -p reports
docker run --rm -v "$PWD/reports:/app/reports" docker-python-example \
  python app.py --n 20 --out reports/squares.txt
```

## How this relates to facility data workflows

This containerization pattern is meant to wrap small “pipeline steps” (ingestion, conversion, QC, feature extraction)
so they can be executed consistently by different users and on different machines.

In a facility setting, you’d typically combine this with:
- a metadata-driven ingestion layer (e.g., database/OMERO-facing tools),
- standardized output artifacts (reports, derived data, logs),
- CI to prevent silent breakage.

