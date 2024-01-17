# TopQ API Tester

This project is an automated test interaction with GitHub via REST API in order to 
retrieve Issues, create a new Issue, and update an existing Issue.

## Table of Contents:
- Installation
- Usage
- Configuration

## Installation
1. Install Python (recommended version: 3.11).
2. Open a terminal of your choice and to the Project's directory path.
3. Use the following command to install all the required dependencies in this project:
pip install -r requirements.txt


## Usage
To run this automated project in order to test basic GitHub Issues functionality use the following command:
pytest .\tests\test_sequence.py -s


## Configuration
In the config.py file you are able to configure all the necessary parameters in order to execute the API calls and tests.
