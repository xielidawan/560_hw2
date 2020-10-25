# 560_hw2
generate 1000 random number which range from 0 to 100; then, use a function y = 3*x+6 to get the new data set and generate a graph.

# instruction to Create a virtual environment [ In Windows System ]


## step one:
Clone the repository to local. 

Way One: Downloading the App and clone the repository from the App.

Way Two: Getting into the terminal and using code : git clone [git address]

Way Three: Downloading the zip file of that repository


## Step Two:
Installing virtualenv by calling this code in the terminal:

>> pip install virtualenv

Then run the following code, env is the name of the environment or name of the path(you could change it):

>> py -m venv env

After using this code you will have a document called env; then, you could activate it by:

>> .\env\Scripts\activate


## Step Three:
After you called the code above, you enter the virtual envirment. Now, you need to install the all the package we need, using:

>> pip install matplotlib

Then, calling this code to save your dependencies:

>> pip freeze > requirements.txt

It will generate a text file in the repository file. If you only have the standard library it will be empty, after you install some packages those package will showing in this text file.

Now you can run the code by(code.py is an example you could change it):

>> py code.py


## Step Four(Optional for user not push the file to Github):
Quiting the virtual environment, by:

>> deactivate

Because we don't want to upload the environment so we need to write a file called .gitignore to omit the env file:

>> vim .gitignore

You will entering the .gitignore file and could edit it by pressing i button; after that, write the code:

>> env/

Then, press ESC and enter: 

>> :wq!

Now, you done with the .gitignore file editing.


# Binder address:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xielidawan/560_hw2/master?filepath=HW2_task5.ipynb)
