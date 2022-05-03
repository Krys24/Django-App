# LINGsCARS
Our chosen website is based on a car dealership called Lingscars. It is based on a small local business located in Newcastle UK. 
The website has an abundant amount of problems. It has an excess amount of information about the vehicles and Ling’s personal achievements, it also is very hard to navigate through the different pages. It is overloaded with colours which can in turn strain the user's vision. The page is also not responsive and can not be minimised for use on smaller devices. This build up of issues would lead to users believing the website is very untrustworthy and would have a negative impact on sales.

## Installation
Firstly open local terminal in desired folder.
Then run this command to clone the repository:
```bash
$ git clone https://github.com/Krys24/SDEV2004.git
```
Now choose directory of the repo and check the origin and upstream remotes are set up correctly.
```bash
cd SDEV2004
git remote -v
```
Now load the file into PyCharm and run the following commands in the terminal.
1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.
2. The second command will run a local server on your machine which means that you only have access/view to this website.
It runs off of your local IP address.

```bash
pip install Django
python manage.py runserver
```
Run this command in PyCharm terminal to generate the translations.
```bash
python manage.py compilemessages
```
## Contributing
Repository for SDEV Assignment by Krystian, Ciaran & David

[Our GitHub Repo.](https://github.com/Krys24/SDEV2004.git)

[Official Django Documentation.](https://docs.djangoproject.com/en/4.0/)

[Official Python Documentation.](https://docs.python.org/3/)
## License
[MIT](https://choosealicense.com/licenses/mit/)