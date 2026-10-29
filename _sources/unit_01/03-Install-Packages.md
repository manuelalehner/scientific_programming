# Installing Python packages

This section contains instructions on how to install additional packages useful for scientific programming, such as
- IPython for development
- Matplotlib for plotting
- NumPy for scientific computing

## Prerequisites

- You have a working Python installation based on mamba ([Section 01](../unit_01/01-Installation.ipynb)) or conda.
- You understand the differences between the **Windows prompt**, the **miniforge prompt**, and the **Python 
interpreter**.

```{warning} 

If you still have doubts about any of these terms, do not hesitate to revisit the installation instructions in [Section 01](../unit_01/01-Installation.ipynb).
```

## Context: the conda (base) environment

When you open the **miniforge prompt** (a **terminal** in Linux/macOS), you are opening a Windows prompt with new tools available: For one, `python` is installed and can be run. Similarly, `conda` and `mamba` commands are only available from the miniforge prompt, and not from the standard prompt. This is possible thanks to [mamba](https://mamba.readthedocs.io/en/latest/), which is a package management system for Python. It gives you access to a very large number of Python packages *for free* (the only thing you need is an internet connection to connect to the package servers).

```{admonition} More details about Mamba
:class: dropdown, note

You were asked to install miniforge for two main reasons: 
- Miniforge is giving you access to the packages available from [conda-forge](https://conda-forge.org), which is an up-to-date repository for Python packages.
- Miniforge includes a `mamba` installer. `mamba` is a "drop-in" replacement for `conda`, and is significantly faster.
```

You will recognize that you are using conda thanks to the following signs:
- When opening the miniforge prompt or terminal, a `(base)` text appears in front of the current path. For the user Jane, a typical miniforge prompt looks like: `(base) C:\Users\Jane>`.
- When Jane asks her computer where to find Python, conda is indicating the `python.exe` that came with the conda installation.

You can ask for the location of a specific prompt command with the command `where` (`which` in Linux). For Jane, the miniforge prompt gives the following indications about the location of `python`:

```none
(base) C:\Users\Jane> where python 
C:\Users\Jane\mambaforge\python.exe
C:\Users\Jane\AppData\Local\Microsoft\WindowsApps\python.exe

(base) C:\Users\Jane> 
```

The first `python.exe` on the list is the one that will be used if you type `python` in the prompt. This is precisely why conda is useful: **it clearly separates your python installation from all other contents on your computer**.


## Install IPython and JupyterLab in the (base) environment

[IPython](https://ipython.org) and [Jupyter](https://jupyter.org) are fundamental tools of a scientific Python installation. If you have worked with Python before, you are probably familiar with Jupyter Notebooks. To install them, type the following **from the miniforge prompt (terminal on Linux/macOS)**

```none
mamba install ipython jupyterlab
```

This will install IPython and JupyterLab at the same time. To check if it worked, type

```none
ipython
```

This should display something like

```none
Python 3.14.7 | packaged by conda-forge | (main, Sep  2 2026, 21:08:32) [GCC 15.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.17.1 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use `ipython --help-all | less` to view all the IPython configuration options.

In [1]:
```

The only *visual* difference between the `ipython` and `python` interpreters is that `>>>` has been replaced by `In [1]:`. More on this later.

You can now run your script `my_python_script.py` from within the IPython interpreter:

```none
%run my_python_script
```

Exit `ipython` with `exit` or `quit`.

```{exercise}
Open a miniforge prompt/terminal and ask Windows/Linux where to find your current Python installation. Compare yours with Jane's.
What about the location of `ipython`? And of `jupyter-lab`? 
```

## Managing environments

These instructions are useful for later in the class when you will be asked to install more packages and maybe for other classes for which you may have to install packages. 

### Create an environment called "scipro"

`(base)` is the name of the base (default) environment for conda. Installing further packages in `(base)` is fine, but it is not recommended. It is recommended to keep `(base)` as simple as possible, with few or no packages installed, and use named environments for further usages.

First, open the miniforge prompt (terminal) and type the following command

```none
mamba create -n scipro --clone base
```

If asked to confirm, type "yes". 

What did we just do? We created a new conda environment called `scipro` (this is the purpose of the option `-n`) which clones all packages available in `base` with the option `--clone base` (this last part is optional: if you omit it, your new environment will be completely empty and you will have to reinstall IPython in your environment `scipro` to be able to use it).

You can now activate your new environment with `mamba activate scipro`.

```{exercise}
Activate the new environment. What changed in comparison to `(base)`? Now ask the prompt again about where to find the commands `ipython` and `jupyter-lab`. Can you see the difference to `base`? 
```

[Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) are a very simple and elegant way to manage different installations of Python packages. They allow to clearly separate different installations and, more importantly, **conda environments allow us to make mistakes**. 

Since "environments" are nothing else than folders on your computer, they allow setups such as:
- `(base)`: python v3.14, JupyterLab, IPython
- `(scipro)`: same as `(base)` + NumPy, SciPy, Matplotlib, etc.
- `(test)`: python 3.10
- `(complex)`: same as `(base)` + NumPy "beta version" + complicated package
- etc.

You can switch between environments with `mamba activate env_name` and leave the current environment with `mamba deactivate`.

```{important} 

You can see which environment is active by the `(base)` or `(scipro)` indicator in front of the prompt. **In the active environment, ALL mamba commands refer to this specific environment**. 

For example, to list the packages available in `scipro`, you need to activate it first (`mamba activate scipro`) and *then* list the packages with `mamba list`. 

To open IPython and have access to the packages installed in `scipro`, activate the environment first and *then* start `ipython`.
```

When one of your environments becomes "broken" or obsolete, you can simply delete it with  `mamba remove -n ENVNAME --all`. This will delete the corresponding folder and all packages in it. Creating, activating, and deleting environments is super easy, and this is why we recommend their use.

```{admonition} Mamba/conda cheat sheet:
:class: note

- `mamba create -n scipro --clone base` : create an environment called "`scipro`" with the same packages in it as `base`
- `mamba create -n scipro` : same as above, but empty
- `mamba activate scipro` : activate environment `scipro`
- `mamba deactivate` : leave the current environment
- `mamba info --envs` : get a list of all environments
- `mamba list` : list the currently installed packages in a specific environment
- `mamba remove -n scipro --all` : delete the environment `scipro` and all packages in it.
```

Visit the [conda documentation](https://docs.conda.io/projects/conda/en/stable/commands/index.html) for more commands (just replace all "`conda`" commands with "`mamba`").

### Installing additional Python packages in the active environment

In the course of your studies, you will likely need to install many Python packages, for example [Xarray](https://docs.xarray.dev) for gridded data analysis or [MetPy](https://unidata.github.io/MetPy) for meteorology.

Almost always, the install procedure will be:
1. open the miniforge prompt/terminal
2. (optional but recommended) activate the environment where you want to install the package
3. install the package with `mamba install`

For now, install the following Python packages:
- [NumPy](https://numpy.org), the fundamental package for scientific computing with Python
- [SciPy](https://scipy.org), fundamental algorithms for scientific computing in Python
- [Matplotlib](https://matplotlib.org), data visualization with Python

To install these, activate the `scipro` environment (recommended) or use `base`, and type:

```none
mamba install numpy scipy matplotlib
```

Answer "yes" to confirm the installation. Note that `mamba` will install several additional packages. These automatically installed packages are called "**dependencies**": they are required for the other packages to function properly.

To test if the installation worked properly, open an IPython interpreter and type:

```python
In [1]: import numpy as np
In [2]: np.arange(1, 11, 2)
```

The output should be:

```python
Out[2]: array([1, 3, 5, 7, 9])
```

Congratulations! You are ready for the rest of the lecture.


## Learning checklist

<label><input type="checkbox" id="week05_01" class="box"> I understand that a **miniforge prompt** is a Windows prompt with conda and Python commands available</input></label>
<label><input type="checkbox" id="week05_02" class="box"> I understand that miniforge creates a folder (and sub-folders) at the location I indicated during the installation, and this is where all my Python packages are installed.</input></label>   
<label><input type="checkbox" id="week05_03" class="box"> I am able to create new conda environments, activate them, and switch between them.</input></label> 
<label><input type="checkbox" id="week05_04" class="box"> I understand that packages installed with `mamba install ...` are always installed in the environment which is currently active. `(base)` is like any other environment: it is simply the default one. </input></label> 
<label><input type="checkbox" id="week05_05" class="box"> I understand that using environments is beneficial on the long term, because it allows me to experiment with additional packages, without being afraid of breaking anything: **environments are just folders on my computer**!</input></label> 
<label><input type="checkbox" id="week05_06" class="box"> I am able to install new packages using `mamba`. I have installed NumPy, SciPy, and Matplotlib.</input></label>    
