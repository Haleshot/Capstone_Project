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

## Note

This project has been set up using [PyScaffold] 4.5 and the [dsproject extension] 0.7.2.

[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[PyScaffold]: https://pyscaffold.org/
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
