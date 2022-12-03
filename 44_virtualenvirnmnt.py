# virtual environment creation  (creating clone or child of main(base) python interpreter)-duplicate python interpreter

# old versions  called as depricated

# why we use virtual enironment?
# assume i created one website using django version 2.2 when i want to give my website source code to someone after some years
# at that time django version will e updated one and my django version 2.2 will be depricated so it will be problem to use
# my code with old version package so to avoid this we need to create 1 virtual environment(its a clone or child of our main python interpreter)
# in that we can install  same package version  that i used to create my website projects.

# steps to create venv

# create new folder where you are gonna create vertualenv folder
# open terminal in that folder
# sudo pip3 install virtualenv
# virtualenv name(nbn)      (folder will be created)
# . nbn/scripts/activate    (to activate virtualenv ,we can activate by going to the scripts folder and then activate) it will bw created
# set-executionpolicy remotesigned   (if u get error while activating then run this command)
# deactivate          (to exit from the virtulenv)
# . nbn/scripts/activate      (if u want to activate it again - '.' represents at that folder path which you are in )
# pip install package_name      (u can install required packages,pip uninstall package_name for uninstall)
# pip freeze>requirement.txt    (requirement.txt in which we can get to know which version of package is being installed)
# pip install numpy==1.1.5      (by checking requirement.txt file to install to that particular package version)
# pip install -r . \requirement.txt        (to install all the package version in the requirement.txt file)    (req+tab which will autocomplete in terminal)

# virtualenv name            (if you want to create another venv(1st u need to exit(deactivate) if u r in venv interpreter
# virtualenv --system-site-packages name       (if you want to create venv exactly as main(base) python interpreter with all the packages installed in base interpreter)