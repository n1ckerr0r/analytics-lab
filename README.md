# Analytics Lab

A collection of my learning and practical data analytics projects in `Jupyter Notebook`.

## Projects

- `marketing-campaign/` - marketing campaign analysis and hypothesis testing
- `netflix/` - exploratory analysis of the Netflix catalog

## Requirements

This environment has `python3`, but the system `pip` and a full `jupyter notebook` are not set up for the project. The easiest way to run the notebooks here is via `uv` and a local virtual environment.

## Quick start

```bash
cd /home/n1ckerr0r/maindir/projects/analytics-lab
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
jupyter notebook
```

After that, the Jupyter interface opens in the browser, where you can open:

- `marketing-campaign/marketing-campaign.ipynb`
- `netflix/netflix.ipynb`

Alternative: if you already have `JupyterLab` installed, you can launch it with:

```bash
jupyter lab
```
