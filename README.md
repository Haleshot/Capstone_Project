[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
<!-- These are examples of badges you might also want to add to your README. Update the URLs accordingly.
[![Built Status](https://api.cirrus-ci.com/github/<USER>/Capstone_project.svg?branch=main)](https://cirrus-ci.com/github/<USER>/Capstone_project)
[![ReadTheDocs](https://readthedocs.org/projects/Capstone_project/badge/?version=latest)](https://Capstone_project.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/Capstone_project/main.svg)](https://coveralls.io/r/<USER>/Capstone_project)
[![PyPI-Server](https://img.shields.io/pypi/v/Capstone_project.svg)](https://pypi.org/project/Capstone_project/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/Capstone_project.svg)](https://anaconda.org/conda-forge/Capstone_project)
[![Monthly Downloads](https://pepy.tech/badge/Capstone_project/month)](https://pepy.tech/project/Capstone_project)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/Capstone_project)
-->


<div align="center">
  <h1>MathMate | Multi-Modal AI for Mathematical Learning</h1>
  <img src="https://github.com/user-attachments/assets/8070b8f6-bbfa-4e00-9ef1-7cddc753eb8d" alt="Project Logo">
  <br>
  <a href="https://github.com/Haleshot/Capstone_Project/issues">
    <img src="https://img.shields.io/github/issues/Haleshot/Capstone_Project" alt="Issues Badge">
  </a>
  <a href="https://github.com/Haleshot/Capstone_Project/pulls">
    <img src="https://img.shields.io/github/issues-pr/Haleshot/Capstone_Project" alt="Pull Requests Badge">
  </a>
</div>

# Capstone project

MathMate | Multi-Modal AI for Mathematical Learning

This capstone project aims to develop a multi-modal AI assistant that integrates computer vision, 
natural language processing, and speech recognition technologies. The system will be accessible 
through a user-friendly chatbot interface, allowing users to interact with it using text, images, or voice 
inputs.

## Installation

In order to set up the necessary environment:

1. review and uncomment what you need in `environment.yml` and create an environment `Capstone_project` with the help of [conda]:
   ```
   conda env create -f environment.yml
   ```
2. activate the new environment with:
   ```
   conda activate Capstone_project
   ```

> **_NOTE:_**  The conda environment will have *Capstone_project* installed in editable mode.
> Some changes, e.g. in `setup.cfg`, might require you to run `pip install -e .` again.


Optional and needed only once after `git clone`:

3. install several [pre-commit] git hooks with:
   ```bash
   pre-commit install
   # You might also want to run `pre-commit autoupdate`
   ```
   and checkout the configuration under `.pre-commit-config.yaml`.
   The `-n, --no-verify` flag of `git commit` can be used to deactivate pre-commit hooks temporarily.

4. install [nbstripout] git hooks to remove the output cells of committed notebooks with:
   ```bash
   nbstripout --install --attributes notebooks/.gitattributes
   ```
   This is useful to avoid large diffs due to plots in your notebooks.
   A simple `nbstripout --uninstall` will revert these changes.


Then take a look into the `scripts` and `notebooks` folders.

## Dependency Management & Reproducibility

1. Always keep your abstract (unpinned) dependencies updated in `environment.yml` and eventually
   in `setup.cfg` if you want to ship and install your package via `pip` later on.
2. Create concrete dependencies as `environment.lock.yml` for the exact reproduction of your
   environment with:
   ```bash
   conda env export -n Capstone_project -f environment.lock.yml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yml` using:
   ```bash
   conda env update -f environment.lock.yml --prune
   ```
4. Hope to create marimo notebooks with uvx commands which will help in isolated environments (dependency-related issues) and smooth running of notebooks.
## Project Organization

```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── Dockerfile              <- Build a docker container with `docker build .`.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yml         <- The conda environment file for reproducibility.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── pyproject.toml          <- Build configuration. Don't change! Use `pip install -e .`
│                              to install for development or to build `tox -e build`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── scripts                 <- Analysis and production scripts which import the
│                              actual PYTHON_PKG, e.g. train_model.
├── setup.cfg               <- Declarative configuration of your project.
├── setup.py                <- [DEPRECATED] Use `python setup.py develop` to install for
│                              development or `python setup.py bdist_wheel` to build.
├── src
│   └── capstone_project    <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `pytest`.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```

<!-- pyscaffold-notes -->

## TODO:

## 1. Model Merging
- [ ] Set up Lightning AI's Efficient Linear Model Merging environment
- [ ] Download and prepare NuminaMath-7B-TIR.q6_k model
- [ ] Download and prepare Qwen2-Math-7B-Instruct-Q6_K.gguf model
- [ ] Research merging methodologies in mergekit repo
- [ ] Select appropriate merging method for math-oriented models
- [ ] Execute model merging process
- [ ] Save and document the merged model

## 2. Model Evaluation
- [ ] Set up llm-autoeval environment
- [ ] Define evaluation metrics focusing on mathematical capabilities
- [ ] Prepare evaluation datasets
- [ ] Run evaluation on the merged model
- [ ] Document baseline performance metrics

## 3. Fine-tuning Preparation
- [ ] Gather and prepare datasets for fine-tuning
- [ ] Set up development environment for various fine-tuning techniques

## 4. ORPOO Fine-tuning
- [ ] Set up ORPOO fine-tuning environment
- [ ] Prepare model and data for ORPOO
- [ ] Execute ORPOO fine-tuning
- [ ] Evaluate model post-ORPOO
- [ ] Document results and improvements

## 5. Axolotl Fine-tuning
- [ ] Set up Axolotl environment
- [ ] Prepare model and data for Axolotl
- [ ] Configure Axolotl parameters
- [ ] Run Axolotl fine-tuning
- [ ] Evaluate model post-Axolotl
- [ ] Document results and improvements


## Relevant diagrams:

Flow diagram:

[![](https://mermaid.ink/img/pako:eNp1U12P2jAQ_CuWnzHHRwpHHioFAnf0EqCAWqmGBzdZiEtiU8fhSoH_XsekvUOoedr17MyOR_EJRzIG7OJNKl-jhCmNlv5KIPN5dKbkD4g0WmhzvkaEfER9Gpr5FC0gNQiXYn0d7lt0QL0xCacPkyLjgoVMJ6TbJ8vx_GbKpzHAPgfYEcYffFMvytpsO4AiX5r1D2QeVIyBZQyrrSGoLRfbCvOv2LUZls3ZHwaBh5YQJYL_LOCMRrR0kTENpRMLV-yRZT_R6Xw2RSMuQBfiTfvJypVc5DPNctBn9HyvRUp2RXm2guPK6vDA0oK9S2hsFYMgRF6hZQmf0Sc6A7WRKmMiAuQJlh5znt_ovdBRoXQC6t7ji1UcmtCOMTuigRSmzO3O_M118B_XxK9kArsnpEafmYhL9xUSWmRiHOhCAfoq1a5CJhaZ0rBINSeZjA1zwPbsO0-55pDfjM2oF8e8tGWm7m5xnflMBzLbK0hA5PwA7-LL17iGMzAZ8dj8p6eStcImkQxW2DVlzNRuhVfiYuaYiXZxFBF2tSqghpUstgl2NyzNTVfsYxODz9lWsezf6Z6Jb1Jmfymmxe4J_8IuceoNp9lttBu9xuNjq-d0a_iI3bZT73U6TqvVaTXabad9qeHflt-sYTD3lCq8Pin7si5_AK0qDUY?type=png)](https://mermaid.live/edit#pako:eNp1U12P2jAQ_CuWnzHHRwpHHioFAnf0EqCAWqmGBzdZiEtiU8fhSoH_XsekvUOoedr17MyOR_EJRzIG7OJNKl-jhCmNlv5KIPN5dKbkD4g0WmhzvkaEfER9Gpr5FC0gNQiXYn0d7lt0QL0xCacPkyLjgoVMJ6TbJ8vx_GbKpzHAPgfYEcYffFMvytpsO4AiX5r1D2QeVIyBZQyrrSGoLRfbCvOv2LUZls3ZHwaBh5YQJYL_LOCMRrR0kTENpRMLV-yRZT_R6Xw2RSMuQBfiTfvJypVc5DPNctBn9HyvRUp2RXm2guPK6vDA0oK9S2hsFYMgRF6hZQmf0Sc6A7WRKmMiAuQJlh5znt_ovdBRoXQC6t7ji1UcmtCOMTuigRSmzO3O_M118B_XxK9kArsnpEafmYhL9xUSWmRiHOhCAfoq1a5CJhaZ0rBINSeZjA1zwPbsO0-55pDfjM2oF8e8tGWm7m5xnflMBzLbK0hA5PwA7-LL17iGMzAZ8dj8p6eStcImkQxW2DVlzNRuhVfiYuaYiXZxFBF2tSqghpUstgl2NyzNTVfsYxODz9lWsezf6Z6Jb1Jmfymmxe4J_8IuceoNp9lttBu9xuNjq-d0a_iI3bZT73U6TqvVaTXabad9qeHflt-sYTD3lCq8Pin7si5_AK0qDUY)


Mindmap:

[![](https://mermaid.ink/img/pako:eNptU8Fu4jAQ_ZWRD6tWIpQAKSQ3KK22EpSKolZacZkmA1jEdtax0dKq_74TaIBu9xBp5s34zfOb-F2kJiORCCV1prBYaABrjLu4mKBb80cwHk8uLyscYMK9OYxoS7kpFGl3gAGGWNKhWtYQwOA-mEyvHjxTY8UW9IbB_H52asiIipJoE6C8GnH8VMWP1mzJBs9hMwpm47p5QnYl9QrmlK61_O3pxDK6HY8HdXonNTmvufXUMJ09Tk_ZLbPvMtzBjdEcluik0Z-qR-j4Iu54h73qsqBULmUK2aFaF3_6VSXpDlOaD6_okzZIz2mDPEeFnWYYtDeHc7dbzP2-WPOwvzDwzlSVGnswvvw6b25MXgLqDB5zdEtj1VGlYm9oI_8VBpWy4xC5WrvKlibKGnuhCizhBwwlD_rku_POW4IXYzdHG3zuZKBMhjmkWOCrzKWTdLbq6c0MWBMoNgwKa15zOukbZJmsLsynl9_Wc2NUYWlNupRbAjq6U57_cc9s6Ak77IVHUfVHfVn_t0Jwvvz_V4ORaAj2UKHM-CG8V90L4dakaCESDjNkK8RCf3Af8qKedjoVibOeGsIav1qLZIl5yZkveGc0kriyqI5ogfqXMao-wqlI3sUfkXSbYRx1O1Er7kdRK-xEDbETSasZddvdKO73-te9qB1H7Y-GeNsTtJpx-zoMe_241-p0ruOw2xDE5ho7Obzi_WP--AsIBS8U?type=png)](https://mermaid.live/edit#pako:eNptU8Fu4jAQ_ZWRD6tWIpQAKSQ3KK22EpSKolZacZkmA1jEdtax0dKq_74TaIBu9xBp5s34zfOb-F2kJiORCCV1prBYaABrjLu4mKBb80cwHk8uLyscYMK9OYxoS7kpFGl3gAGGWNKhWtYQwOA-mEyvHjxTY8UW9IbB_H52asiIipJoE6C8GnH8VMWP1mzJBs9hMwpm47p5QnYl9QrmlK61_O3pxDK6HY8HdXonNTmvufXUMJ09Tk_ZLbPvMtzBjdEcluik0Z-qR-j4Iu54h73qsqBULmUK2aFaF3_6VSXpDlOaD6_okzZIz2mDPEeFnWYYtDeHc7dbzP2-WPOwvzDwzlSVGnswvvw6b25MXgLqDB5zdEtj1VGlYm9oI_8VBpWy4xC5WrvKlibKGnuhCizhBwwlD_rku_POW4IXYzdHG3zuZKBMhjmkWOCrzKWTdLbq6c0MWBMoNgwKa15zOukbZJmsLsynl9_Wc2NUYWlNupRbAjq6U57_cc9s6Ak77IVHUfVHfVn_t0Jwvvz_V4ORaAj2UKHM-CG8V90L4dakaCESDjNkK8RCf3Af8qKedjoVibOeGsIav1qLZIl5yZkveGc0kriyqI5ogfqXMao-wqlI3sUfkXSbYRx1O1Er7kdRK-xEDbETSasZddvdKO73-te9qB1H7Y-GeNsTtJpx-zoMe_241-p0ruOw2xDE5ho7Obzi_WP--AsIBS8U)



## Note

This project has been set up using [PyScaffold] 4.5 and the [dsproject extension] 0.7.2.

[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[PyScaffold]: https://pyscaffold.org/
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
