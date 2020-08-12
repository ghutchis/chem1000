# Modules

One of the strengths of Python is the availabilty of modules which add a variety of features and methods.

There are a few ways to install modules, but two main methods are:

```
pip install -U [module] # install and/or update
```

Or..
```
conda install [module] # if not installed
conda update [module]
```

where `[module]` is the name of the module. In general, the links below are to documentation for modules.

## General Science Modules
* [pint](https://pint.readthedocs.io/en/stable/) - unit conversion
* [numpy](https://numpy.org/doc/stable/) - numeric python - base of almost everything in the Python for science “stack"
* [scipy](https://docs.scipy.org/doc/scipy/reference/) - scientific data analysis tools, including integration, optimization, signal analysis, filtering, etc.
* [pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/) - manipulate data tables / spreadsheets
* [sympy](https://docs.sympy.org/latest/) - symbolic math manipulation

## Plotting / graphs 

(to be honest, this grows endlessly)
* [matplotlib](https://matplotlib.org/users/) - common plotting library
* [seaborn](https://seaborn.pydata.org/introduction.html) (builds on top of matplotlib)
* [plotly](https://plotly.com/python/plotly-express/) - interactive plots
* [bokeh](https://docs.bokeh.org/en/latest/docs/user_guide.html) - interactive plots

## Data Science / Machine Learning
* [statsmodels](https://www.statsmodels.org/stable/user-guide.html) - linear regression, including robust regression
* [scikit-learn](https://scikit-learn.org/stable/preface.html)
* [pytorch](https://pytorch.org/tutorials/) - machine learning toolkit
* [keras](https://keras.io/getting_started/intro_to_keras_for_engineers/) - high level interface for machine learning (e.g. TensorFlow)
* [TensorFlow](https://www.tensorflow.org/learn) - machine learning toolkit
* [GPyTorch](https://gpytorch.ai/) - Gaussian Process Regression / [Bayesian Optimization](https://botorch.org/) / [Adaptive Experimentation](https://ax.dev/)
* [Pyjanitor](https://pyjanitor.readthedocs.io/) - clean up data sets

## Chemistry
* [py3dmol](https://nbviewer.jupyter.org/github/3dmol/3Dmol.js/blob/master/py3Dmol/examples.ipynb) - interactive visualization in Jupyter
* [rampy](https://github.com/charlesll/rampy) - process Raman / IR / XAS spectra including background correction
* [NMRglue](https://www.nmrglue.com/) - NMR data analysis
* [pubchempy](https://pubchempy.readthedocs.io/en/latest/) - access data from PubChem
* [cclib](http://cclib.github.io/) - read useful data from quantum chemistry files
* [openbabel](https://open-babel.readthedocs.io/en/latest/UseTheLibrary/Python.html) - read / write / cheminformatics
* [rdkit](https://www.rdkit.org/docs/GettingStartedInPython.html) - cheminformatics / molecular fingerprints / descriptors
* [openmm](http://docs.openmm.org/latest/userguide/) - molecular dynamics
* [mdanalysis](https://www.mdanalysis.org/docs/) - analysis of MD simulations

## Other
* [Biopython](https://biopython.org/) - computational bio and bioinformatics
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - scrape data from the web
* [scikit-image](https://scikit-image.org/) - image manipulation & analysis (e.g., particle counting, size, etc.)
* [Atomic Simulation Environment](https://wiki.fysik.dtu.dk/ase/) - Tools to run and analyze atomic materials calculations
* [pymatgen](https://pymatgen.org/) - materials science in Python
    - [matgenb](http://matgenb.materialsvirtuallab.org/) - Example notebooks for the Materials Virtual Lab