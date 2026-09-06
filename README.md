# MLOps Project - 23L-2558

## Project Overview

This project demonstrates a basic Machine Learning workflow for house price prediction.

The project uses a Random Forest Regression model to predict house prices based on:

* Area
* Number of bedrooms
* House age

Student ID: **23L-2558**

## Project Structure

```text
mlops-project-23L-2558/
│
├── data/
│   └── house_prices.csv
│
├── model/
│   └── house_price_model.pkl
│
├── src/
│   ├── train.py
│   └── train_23L-2558.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

Python 3.x is required.

The required Python packages are listed in `requirements.txt`.

## Installation

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Dataset

Place the dataset in:

```text
data/house_prices.csv
```

The dataset must contain the following columns:

* `area`
* `bedrooms`
* `age`
* `price`

The `data/` directory is ignored by Git and is not uploaded to GitHub.

## Training the Model

Run the training script from the project root directory:

```powershell
python src/train.py
```

The script loads the dataset, splits it into training and testing data, trains a Random Forest Regression model, and saves the trained model.

The trained model is saved as:

```text
model/house_price_model.pkl
```

The `model/` directory is also ignored by Git, so the generated model file is not uploaded to GitHub.

## Student ID

The Student ID **23L-2558** is integrated into the project files and Git workflow as required.

## Git

This project uses Git for version control and includes separate branches for preprocessing and tuning experiments.

Main branch:

```text
main
```

Feature branches:

```text
feature-preprocessing-23L-2558
feature-tuning-23L-2558
```
