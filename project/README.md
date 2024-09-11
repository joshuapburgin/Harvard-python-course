# CRM - Customer Relationship Management

#### Video Demo:  https://www.loom.com/share/2b9467f947de4567a574e1d272226d0d?sid=a4ff8ba2-f43e-4d87-a6a4-8d7218befe27

#### Description:
TODO

## Overview

Welcome to the CRM (Customer Relationship Management) system repository. This project is designed to provide a comprehensive solution for managing company and employee data. Utilizing MongoDB for data storage and Python for data processing, the CRM system offers functionalities for data aggregation, querying, and interaction with external APIs such as OpenAI to enhance data extraction and processing capabilities.


## Features

- **Company and Employee Data Management:** Efficiently read and process company and employee data from CSV files, storing them in MongoDB for structured data management.
- **Data Aggregation:** Merge employee data into respective company documents within MongoDB, enabling comprehensive company profiles.
- **Custom Query Capabilities:** Execute complex queries to find companies based on specific criteria such as industry and the number of employees.
- **OpenAI Integration:** Leverage OpenAI's API to extract and process specific information from text inputs, enhancing the system's intelligence.

## Installation

To get started with the CRM system, follow these steps:

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/joshuapburgin/CRM.git
    cd CRM
    ```

2. **Create a Virtual Environment and Activate It:**

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**

    Install all required Python packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory and add your OpenAI API key. This is crucial for the OpenAI integration to function properly:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Set Up MongoDB:**

    Ensure you have MongoDB installed and running locally. MongoDB can be downloaded from [here](https://www.mongodb.com/try/download/community). Follow the installation instructions for your operating system.

## Usage

1. **Prepare Data Files:**

    Ensure you have the following CSV files in the root directory:
    - `company_data.txt`
    - `employee_data.txt`

2. **Run the Main Script:**

    Execute the main script to process and store data:

    ```sh
    python project.py
    ```

3. **Run Unit Tests:**

    To verify the functionality of the system, run the unit tests using pytest:

    ```sh
    pytest test_project.py
    ```

## Project Structure

The project consists of several key files, each playing a crucial role in the overall functionality:

- **`company_data.txt`**: This file contains the raw data for various companies, including their ID, name, website, and industry. It serves as the primary input for company information.

- **`employee_data.txt`**: This file holds the raw data for employees, including their ID, company ID, name, email, LinkedIn profile, and job title. It is used as the input for employee information.

- **`project.py`**: The main script that orchestrates the entire process. It reads the company and employee data, processes it, and stores it in MongoDB. It also includes functions for merging employee data into their respective company documents and querying the database based on user preferences.

- **`requirements.txt`**: This file lists all the Python dependencies required for the project. It ensures that the environment can be set up consistently across different systems.

- **`test_project.py`**: Contains unit tests for various functions in the project. These tests ensure that the code behaves as expected and helps in maintaining code quality.

## Key Functions

### `reading_company_file()`
This function reads company data from `company_data.txt` and creates `Company` objects. Each line in the file is processed to instantiate a `Company` object with attributes like `companyID`, `name`, `website`, and `industry`. These objects are then returned in a list for further processing.

### `reading_employee_file()`
Similar to `reading_company_file()`, this function reads employee data from `employee_data.txt` and creates `Employee` objects. The employee attributes include `employeeID`, `companyID`, `name`, `email`, `linkedin`, and `job_title`. The function returns a list of these objects.

### `employee_using_mongoDB(many_employees)`
This function takes a list of `Employee` objects and inserts them into the MongoDB database. It ensures that any existing data is removed before inserting new data to maintain a clean state.

### `company_using_mongoDB(many_companies)`
This function performs a similar role for company data. It takes a list of `Company` objects and inserts them into the MongoDB database, removing any existing data beforehand.

### `merge_databases_mongoDB()`
This function merges employee data into their respective company documents within MongoDB. It uses an aggregation pipeline to perform a `$lookup` operation, which joins the `employees` collection with the `companies` collection based on the `companyID` field. The result is a comprehensive view of each company, including a list of its employees.

### `input_openai(sentence)`
This function utilizes OpenAI's API to extract specific information from a sentence. It processes user input to dynamically capture preferences like the number of employees and the desired industry. This enhances the system's ability to query the database based on user-defined criteria.

### `targeted_company(number_of_employees, industry)`
This function queries the MongoDB database to find companies that match the specified number of employees and industry. It uses an aggregation pipeline to filter and retrieve relevant companies, returning detailed information about these companies, including their employees.

## Design Choices

### Data Storage
Choosing MongoDB for data storage was a deliberate decision. MongoDB's flexibility in handling unstructured data and its powerful aggregation framework made it an ideal choice for this project. The ability to perform complex queries and data transformations directly within the database significantly simplifies the data processing logic in the application.

### API Integration
Integrating OpenAI's API adds a layer of intelligence to the system, allowing it to process natural language inputs. This makes the system more user-friendly and capable of handling dynamic queries based on user preferences.

### Code Structure
The project is structured to separate concerns clearly. Data reading, processing, and storage are handled in dedicated functions, making the code modular and easier to maintain. Unit tests are provided to ensure that each function performs as expected, contributing to the overall robustness of the system.

## Conclusion

This CRM system offers a robust solution for managing and querying company and employee data. By leveraging MongoDB and OpenAI, it combines powerful data storage capabilities with advanced data extraction and processing features. The project's modular design and comprehensive documentation ensure that it is both scalable and maintainable. We welcome contributions from the community to further enhance this system.

Thank you for exploring this CRM project. We hope it meets your needs and provides a solid foundation for managing customer relationships effectively. For any inquiries or contributions, please feel free to reach out.
