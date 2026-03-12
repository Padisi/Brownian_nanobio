# Brownian_nanobio
Minimal example of python project for brownian solver.

## Requirements

- Git: https://github.com/git-guides/install-git
- Conda: https://github.com/conda-forge/miniforge

---

## Clone the Repository
Write in the terminal where you want to place the project folder:
```bash
git clone https://github.com/padisi/Brownian_nanobio.git
cd Brownian_nanobio
```
## Instalation
First, create the conda environment and activate it. The environment is created using the environment.yml file, which contains all the libraries we will use.

You can add new ones there if needed. Make sure to recreate the environment after adding a new dependency.
```bash
conda env create
conda activate brownian
```
Then install the functions we have developed with pip. For this, the pyproject.toml file is required.
```bash
pip install .
```

## Testing
To ensure everything is installed correctly, run the following command in the terminal:
```bash
pytest
```
Some tests are stochastic, so they might fail occasionally on the first run. If this happens, simply rerun pytest.
