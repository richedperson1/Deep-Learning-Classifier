import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] : %(message)s : ')
PACKAGE_NAME = "DeepClassifier"
listOfFiles = [
    ".github/workflows/.gitkeep",
    f"src/{PACKAGE_NAME}/__init__.py",
    f"src/{PACKAGE_NAME}/components/__init__.py",
    f"src/{PACKAGE_NAME}/utils/__init__.py",
    f"src/{PACKAGE_NAME}/config/__init__.py",
    f"src/{PACKAGE_NAME}/pipeline/__init__.py",
    f"src/{PACKAGE_NAME}/entity/__init__.py",
    f"src/{PACKAGE_NAME}/constants/__init__.py"
    "configs/config.yaml",
    "dvc.yml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for fileName in listOfFiles:
    filePath = Path(fileName)
    fileDir, fileName = os.path.split(filePath)
    print(fileDir, fileName)
    if fileDir:
        os.makedirs(fileDir, exist_ok=True)
        logging.info(
            f"We create the files : {fileDir} and files name : {fileName}")

    if not(os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, "w") as f:
            pass
            logging.info(f"empty file : {fileDir} is created ")
    else:
        logging.info(f"Files : {fileName} already exists")
