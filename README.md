# Do more trees mean more money?

Analyzing a data set from Dublin city to find if houses are more expensive on streets with tall trees compared to those with shorter trees
---

## Prerequisites

Before setting up the project, ensure you have the following installed:

1. **Python**: Version 3.8 or higher. [Download Python here](https://www.python.org/downloads/)
2. **Package Manager**: `pip` (comes with Python installation).
3. **Virtual Environment Tool**: `venv` or any other Python virtual environment manager.


---

## Setup Instructions

### Local Setup

Follow these steps to set up and run the project locally:

1. Change directory to project folder after unzip it:
    ```bash
    cd money-trees
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add data set files in `data/` folder:

* `dublin-property.csv`
* `dublin-trees.json`

5. Run the application:
    ```bash
    python analyzer.py
    ```

6. Run tests to ensure everything works:
    ```bash
    python -m unittest tests.py
    ```

---

### Production Setup

For deploying this project in a production environment, follow these steps:

1. Set up the production server (e.g., Linux, Docker, or cloud service like AWS, Azure).
2. Install Python 3.8 or higher and `pip` on the server.
3. Change directory to project folder after unzip it:
    ```bash
    cd money-trees
    ```

4. Set up the virtual environment and install dependencies as shown in the **Local Setup** section.

5. Add data set files in `data/` folder:

* `dublin-property.csv`
* `dublin-trees.json`

6. Run the application:
    ```bash
    python analyzer.py
    ```

---

## Dataset Handling Notes

### Original datasets
- `dublin-trees.json` contains a list of street names. Streets are split into two categories: `short` and `tall`, based on the median tree height as recorded by Dublin City Council.
- `dublin-property.csv` contains a subset of the Residential Property Price Register, with a list of property addresses, their street name and sale price in euro. 

### Adding the Dataset
1. Place the dataset in the `data/` directory (create it if it doesn’t exist).
2. Configure `config.py` with these variables:
   * ENCODING: encoding type when reading the files
   * COLUMNS: comma separated columns in the dataset to validate
   * BATCH_SIZE: batch size when processing the file for memory optimization
   * ENV: `local` or `production`

### Example Dataset
```csv
Date of Sale (dd/mm/yyyy),Address,Street Name,Price
1/1/2015,"APT 274, THE PARKLANDS, NORTHWOOD",the park,"€ 79,500.00"
5/1/2015,"61 CHARLEMONT, GRIFFITH AVE, DUBLIN 9",charlemont,"€ 557,000.00"
6/1/2015,"6A Church Street, Finglas, Dublin 11",church street,"€ 160,000.00"
```