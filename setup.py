import setuptools

LONG_DISCRIPTION = "we are going to create new model which will be predict binary classification using deep learning "

__version__ = "0.0.0"

REPO_NAME = "Deep-Learning-Classifier"
AUTHOR_NAME = "rutvik_jaiswal195"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "rutvikjaiswal195@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="feel free to made any changes in project",
    long_description=LONG_DISCRIPTION,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"))
