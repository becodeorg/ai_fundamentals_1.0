# Learn to Python

Python is one of the trendiest programmation language for the moment. Easy to learn, Python is often used as an example while learning programmation.

## What is Python ?
Python is a programming language invented by Guido Van Rossum. The first version of Python was released in 1991.

<p align="center">
  <img src="https://cdn.directexpose.com/wp-content/uploads/2018/05/british-comedy-guide-monty-python.jpg" alt="Sublime's custom image"/>

  *(The name of “Python” was chosen to pay homage to the Monthy Pythons)*
</p>

### Python is an interpreted language !
The main difference between a compiled and an interpreted language is as follows : while the compiler translate once for all a source code into an independent executable file (therefore using machine code or assembly code), the interpreter is needed 
at each launch of the interpreted program, to translate.
The interpreter translates a portion of code, executes it and translates then the next portion of code, executes it, and so on. If you have already taken a little look at  programming, you might find that this language has a certain poetry. Programmers often have fun looking for the nicest/most effective way to write a sequence of instructions.

### What does Python do ?
Python is both simple and powerful, it allows you to write very simple scripts but thanks to its many librairies, you can also work on more ambitious projects.

* Web: Today Python combined with the framework Django is a very accurate technological choice for big websites projects.

* System: Python is also frequently used by system admins to create so-called repetitive tasks or simply maintenance tasks. Besides, if you want to create Java applications coded in Python, it is possible thanks to the Jython project.

### Why would you choose Python over other languages ?
Python is a language that’s easy to learn and its code is more readable, and so easier to maintain. It can be up to 5 times more concise than Java language for instance, which boosts the developer productivity et reduce mechanically the amount of bugs.
Python is also used in the science community, for example bioinformatics. Libraries are available for this domain as the biopython module. 

There are also libraries that facilitates the creation of 2D (and 3D) video games. For instance : [pyGame](http://www.pygame.org/news.html)

On the other hand, as Python is an interpreted language, it’s logically slower than a compiled one. Even though great efforts have been made lately, for very big projects, it may be necessary to use Java, C#, etc.

A last thing to know about Python : its environnement is open, meaning it can work with Java, C++, C#, and so on. 


### Who uses Python ?
Google (Guido van Rossum worked for Google from 2005 to 2012), Yahoo, Microsoft and the Nasa claim to use Python, to name a few.

## Installation:
### Please use Anaconda
To make your life easier, you can download Anaconda. This specialized distribution for data scientists and includes more than 1500 python packages that we will need.

[Please follow this link](https://www.anaconda.com/distribution/)

```
On the prompt / terminal:
Move to the directory where you have stored Anaconda3-x.x.x-Linux-x86_64.sh
Type: bash Anaconda3-x.x.x-Linux-x86_64.sh
Validate everything: "Yes"
Restart the computer
``` 
Then 
```
On the prompt/terminal :
conda create --name name_environment python=3
On the prompt / terminal:
Create your environment: conda create --name name_environment python=3
⇒ Type "y"
Activate your environment: source activate environment_name
Disable its environment: source deactivate environment_name
```

### If you want to install everything separately

#### Install Python on Linux or MacOS
If you work in a Linux or MacOS environment, good news: Python is already installed. However, make sure you have a 3.xx version.
````shell
python -v
````

#### Install Python on Windows
You can download a Python installation file at this address: [Download Python](https://www.python.org/download/)

#### Which version to choose ?
Try to use the most recent/stable version. Note that the most used version those days is the 3.XX .

There are [compatibility problems between the version 2 and 3 of Python](https://learntocodewith.me/programming/python/python-2-vs-python-3/). Therefore I advise you to learn Python 3 then to learn the differences between those two versions. So you’ll be able to handle problems related to inevitable migrations.

#### And download Jupyter-Notebook   

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

[Download and install Jupyter-Notebook](https://jupyter.org/)

Open your terminal and type : 
```
jupyter-notebook 
```

### Why Jupyter is data scientists’ computational notebook of choice ?
>Jupyter is a free, open-source, interactive web tool known as a computational notebook, which researchers can use to combine software code, computational output, explanatory text and multimedia resources in a single document. Computational notebooks have been around for decades, but Jupyter in particular has exploded in popularity over the past couple of years. This rapid uptake has been aided by an enthusiastic community of user–developers and a redesigned architecture that allows the notebook to speak dozens of programming languages — a fact reflected in its name, which was inspired, according to co-founder Fernando Pérez, by the programming languages Julia (Ju), Python (Py) and R.


___

## Python editors:

#### Sublime Text

Sublime text has a whole range of plugins that you will soon be hooked! Its basic version is free. A small alert will ask you from time to time if you want to buy a license to support the project but nothing forces you to do it.

Don’t forget to install the packagecontrol which will allow you to install the needed tools for your project.

#### Visual Studio Code

If you’re an Ubuntu user, download the .deb, double-click on the file and click on install. If you’re facing dependencies issues, try executing the following command :

	sudo apt-get install -f

#### Pycharm

[Install PyCharm](https://www.jetbrains.com/pycharm/)

PyCharm is an integrated development environment used to program in Python.

It allows code analysis and contains a graphical debugger. It also allows the management of unit tests, the integration of version management software, and supports web development with Django.

Developed by the Czech company JetBrains, it is a multi-platform software that runs on Windows, Mac OS X and Linux. It is available in professional edition, distributed under proprietary license, and community edition under Apache license. 

<p align="center">
  <a href="./1.basic-python-syntax/basic-python-syntax.ipynb">NEXT >> </a>
</p>

