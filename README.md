# py4dm20

Python implementation of computer assignments for course 4dm20.

## Installation instructions

1. Install Python 3.10 in a conda environment (python 3.11 is not supported by mosek as of 2023-03)
    - `conda create -n 4dm20 python=3.10`
    - `conda activate 4dm20`

2. Install the required packages: `pip install -r requirements.txt`
3. Install MOSEK
    - `conda install -c mosek mosek`
4. Install CVXPY
    - `conda install -c conda-forge cvxpy`
