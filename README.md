
## Kickstarter-Project-Success-Prediction

## Overview

Welcome to the Kickstarter Project Repository, a comprehensive resource for predicting the success of Kickstarter projects through the application of various machine learning techniques. This repository cantains machine learning model that has been trained to analyze and forecast the outcomes of Kickstarter campaigns. Alongside the model, you'll find meticulously crafted code for data cleaning, preprocessing, and training, ensuring that the predictive capabilities are built upon high-quality, refined datasets.



---

## Relevant columns of the data set

* **backers_count**: Amount of people pledging money to the project                                     
* **category** -> 'slug': Name of the projects' specific parent- & sub-category (part of json string)
* **country**: Country of the projects creator 
* **creator** -> 'id': id of the creator -> to be used as categorical variable (part of json string)
* **fx_rate**: currency exchange rate
* **goal**: Information on the amount of money needed to succeed in the local currency of the project
* **launched_at**: Start date? of the project
* **deadline**: End date of the project
* **spotlight**: Project highlighted on the website -> excluded since unclear if this only happens after a project has been funded
* **staff_pick**: Marked by a staff member of kickstarter (more attention drawn towards project) -> excluded since unclear if this only happens after a project has been funded
* **state**: (successful/failed/canceled/live/suspended) -> exclude 'live' and combine 'canceled', 'suspended' with 'failed'
* **static_usd_rate**: Exchange rate to transform goal in every column from current currency to USD

## Repository Structure

- **model**: Contains saved files of the model.
- **src**: Includes scripts for different purposes:
- **hyperparameters.py**: Defines hyperparameters used in the model.
- **data_loader.py**: Includes scripts for loading the data.
- **train.py**: Script for training the models.
- **predict.py**: Script for outcome of the models.
- **notebook**: Experimental notebooks used for analysis and development.
- **feature_engineering**.py: Script for the feature engineering.

## Getting Started

1. Clone this repository.
2. Set up a Python environment and install the necessary dependencies listed in requirements.txt.
3. Utilize the provided scripts in the src directory for model training, data preprocessing, etc.

## Set up your Environment

### **`macOS`** type the following commands : 

- For installing the virtual environment you can either use the [Makefile](Makefile) and run `make setup` or install it manually with the following commands:

     ```BASH
    make setup
    ```
    After that active your environment by following commands:
    ```BASH
    source .venv/bin/activate
    ```
Or ....
- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:
    ```Bash
    python.exe -m pip install --upgrade pip
    ```


   
## Usage

In order to train the model and store test data in the data folder and the model in models run:

**`Note`**: Make sure your environment is activated.

```bash
python example_files/train.py  
```

In order to test that predict works on a test set you created run:

```bash
python example_files/predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```





