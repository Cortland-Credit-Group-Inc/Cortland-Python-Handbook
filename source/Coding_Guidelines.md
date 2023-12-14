# Coding Guidelines 

Here are some essential guidelines to adhere to while developing your projects.

## **Use datetime for Date Variables**

- **Rule:** Always utilize the `datetime` module from the `datetime` package for handling date and time values.

- **Example:**

  ```python
  from datetime import datetime
  
  current_date = datetime.now()
  print(current_date.strftime("%Y-%m-%d"))
  ```

## **No Hardcoded Values**

- **Rule:** Define hardcoded values as constants at the beginning of your script, except for values like 0, 1, -1, -2 indicating positions.

- **Example:**

  ```python
  # Correct Approach: Define hardcoded values as constants at the beginning of the script
  MAX_RETRY = 5
  TIMEOUT = 30
  URL = "http://example.com/api/data"
  
  def fetch_data():
      for _ in range(MAX_RETRY):
          response = requests.get(URL, timeout=TIMEOUT)
          if response.status_code == 200:
              return response.json()
      return None
  ```

  In this example, values like `MAX_RETRY`, `TIMEOUT`, and `URL` are defined at the beginning of the script as constants. This makes it easier to change these values in the future without searching through the entire codebase.

## **Select DataFrame Columns by Name**

- **Rule:** Prefer selecting columns in pandas DataFrames by their name rather than by their positional index.

- **Example:**

  ```python
  import pandas as pd
  
  # Sample DataFrame
  data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 34, 29], 'City': ['New York', 'Paris', 'Berlin']}
  df = pd.DataFrame(data)
  
  # Correct Approach: Select columns by name
  names = df['Name']
  ages = df['Age']
  
  # Incorrect Approach: Select columns by index (Avoid this)
  names_by_index = df.iloc[:, 0]
  ages_by_index = df.iloc[:, 1]
  
  ```

  In this example, columns from the DataFrame `df` are accessed by their names (`'Name'` and `'Age''`). This is preferable to selecting columns by their index positions, as it makes the code more readable and less prone to errors if the column order changes in the DataFrame.

## **Avoid Importing Unused Packages**

- **Rule:** Refrain from importing packages or functions that you do not use in your script.

## **Organize Imports**

- **Rule:** List external (third-party) and internal (project-specific) imports separately at the start of your scripts.

## **Structured Program Organization**

- **Structure:** Adopt a clear program structure with dedicated scripts for different functionalities, such as `Helpers.py`, `ReadData.py`, and a central `Main.py`.

- **Example:**

  ```bash
  YourProject/
  │
  ├── Main.py                    # Main script to integrate and run the entire program
  │
  ├── Helpers.py                 # Contains utility functions and classes
  │
  ├── ReadData.py                # Dedicated to data reading and preprocessing tasks
  │
  ├── OtherScript1.py            # Additional script for a specific functionality
  │
  ├── OtherScript2.py            # Another script for a different functionality
  │
  └── ...                        # Additional scripts as needed
  
  ```

  

