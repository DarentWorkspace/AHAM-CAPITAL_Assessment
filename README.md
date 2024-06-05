# AHAM-CAPITAL_Assessment
 Backend Developer Practical : Fund Management System 

## Overview
This project is a Fund Management System implemented using Flask and SQLite. It allows you to create, read, update, and delete (CRUD) investment funds through a RESTful API.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [GET /funds](#get-funds)
  - [POST /funds](#post-funds)
  - [GET /funds/:fund_id](#get-fundsfund_id)
  - [PUT /funds/:fund_id](#put-fundsfund_id)
  - [DELETE /funds/:fund_id](#delete-fundsfund_id)
- [Database Schema](#database-schema)

## Getting Started

### Prerequisites
- Python 3.11.4(base)
- Flask
- SQLite

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DarentWorkspace/AHAM-CAPITAL_Assessment.git

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

3. Install the required packages:
   ```bash
   pip install flask

4. Run the application:
   ```bash
   python app.py
---
## API Endpoints

### GET /funds
Retrieve a list of all funds.
   - In Command Prompt:
   ```curl
   curl http://127.0.0.1:5000/funds
   ```
   - Request:
   ```bash
   GET /funds
   ```
   - Response:
   ```json
   [
     {
      "fund_id": 1,
      "name": "Fund Name",
      "manager_name": "Manager",
      "description": "Description",
      "nav": 100.0,
      "date_of_creation": "2024-06-05",
      "performance": 10.0
     }
   ]
   ```

### POST /funds
Create a new fund.
   - In Command Prompt:
   ```curl
   curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Test Fund\",\"manager_name\":\"Test Manager\",\"description\":\"This is a test fund\",\"nav\":1000,\"date_of_creation\":\"2024-06-05\",\"performance\":100}" http://127.0.0.1:5000/funds
   ```
   - Request:
   ```bash
    POST /funds
    Content-Type: application/json
    {
      "name": "Test Fund",
      "manager_name": "Test Manager",
      "description": "This is a test fund",
      "nav": 1000,
      "date_of_creation": "2024-06-05",
      "performance": 100
    }
   ```
   - Response:
   ```json
    {
      "message": "Fund added successfully"
    }
   ```

### GET /funds/:fund_id
Retrieve details of a specific fund using its ID. 
   - In Command Prompt:
   ```curl
   curl http://127.0.0.1:5000/funds/1
   ```
   - Request:
   ```bash
   GET /funds/1
   ```
   - Response:
   ```json
    {
      "fund_id": 1,
      "name": "Fund Name",
      "manager_name": "Manager",
      "description": "Description",
      "nav": 100.0,
      "date_of_creation": "2024-06-05",
      "performance": 10.0
    }
   ```

### PUT /funds/:fund_id
Update the performance of a fund using its ID.
   - In Command Prompt:
   ```curl
   curl -X PUT -H "Content-Type: application/json" -d "{\"performance\":15}" http://127.0.0.1:5000/funds/1
   ```
   - Request:
   ```bash
    PUT /funds/1
    Content-Type: application/json
    {
      "performance": 15.0
    }
   ```
   - Response:
   ```json
    {
      "message": "Fund performance updated successfully"
    }
   ```

### DELETE /funds/:fund_id
Delete a fund using its ID.
   - In Command Prompt:
   ```curl
   curl -X DELETE http://127.0.0.1:5000/funds/1
   ```
   - Request:
   ```bash
   DELETE /funds/1
   ```
   - Response:
   ```json
    {
      "message": "Fund deleted successfully"
    }
   ```

### Notes: 
  - Make sure your Flask app is running `python app.py` while testing the API.
---
## Database Schema
The database schema consists of a single table `funds` with the following columns:
- fund_id: INTEGER PRIMARY KEY
- name: TEXT NOT NULL
- manager_name: TEXT NOT NULL
- description: TEXT NOT NULL
- nav: REAL NOT NULL
- date_of_creation: TEXT NOT NULL
- performance: REAL NOT NULL

**Table Definition:**
  ```sql
  CREATE TABLE IF NOT EXISTS funds (
    fund_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager_name TEXT NOT NULL,
    description TEXT NOT NULL,
    nav REAL NOT NULL,
    date_of_creation TEXT NOT NULL,
    performance REAL NOT NULL
  );
  ```


