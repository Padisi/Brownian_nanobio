# Brownian_nanobio
Minimal example of python project for brownian solver.

## Requirements

- Git: https://github.com/git-guides/install-git
- Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

---

## Clone the Repository
Write on the terminal where you want to have the folder with the project:
```bash
git clone https://github.com/padisi/Brownian_nanobio.git
cd Brownian_nanobio
```
## Instalation
First create the conda environment and activate it. This is created thanks to the environment.yml file, that contains all the libraries we will use.
You can add news there if you need them, make sure you create the environment again after add a new one.
```bash
conda env create
conda activate brownian
```
Then install the functions we have develop with pip, to make this the pyproject.toml file is needed.
```bash
pip install .
```

## Testing
To ensure you have done everything well write in the terminal:
```bash
pytest
```
To pass the tests.
