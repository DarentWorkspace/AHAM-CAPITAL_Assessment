# Test Documentation

This document contains test cases for the fund management system.

## Test Cases
---
### TC001: Verify Retrieving List of Funds

**Test Case Title:** Verify Retrieving List of Funds

**Description:**
This test case will verify the functionality of retrieving a list of all funds through the API endpoint.

**Preconditions:**
- The application is installed and running.
- The database contains at least one fund entry.

**Test Steps:**
1. Send a GET request to the `/funds` endpoint.
2. Verify the response status code.
3. Verify the response contains a list of funds.
4. Verify the correctness of the response data format.

**Expected Results:**
- The response status code should be 200 (OK).
- The response should contain a list of funds.
- The response data format should be JSON.

**Actual Results:**
- The response status code is 200 (OK).
- The response contains a list of funds.
- The response data format is JSON.

**Test Data:** None

**Postconditions:**
- The application state remains unchanged.
---
### TC002: Verify Adding a New Fund

**Test Case Title:** Verify Adding a New Fund

**Description:**
This test case will verify the functionality of adding a new fund through the API endpoint.

**Preconditions:**
- The application is installed and running.

**Test Steps:**
1. Send a POST request to the `/funds` endpoint with valid fund data.
2. Verify the response status code.
3. Verify the new fund is added to the database.

**Expected Results:**
- The response status code should be 200 (OK) or 201 (Created).
- The new fund should be added to the database.

**Actual Results:**
- The response status code is 200 (OK) or 201 (Created).
- The new fund is added to the database.

**Test Data:**
- Fund data (name, manager_name, description, nav, date_of_creation, performance)

**Postconditions:**
- The database contains the newly added fund.
---
### TC003: Verify Retrieving Details of a Specific Fund

**Test Case Title:** Verify Retrieving Details of a Specific Fund

**Description:**
This test case will verify the functionality of retrieving details of a specific fund using its ID through the API endpoint.

**Preconditions:**
- The application is installed and running.
- The database contains at least one fund entry.

**Test Steps:**
1. Send a GET request to the `/funds/{fund_id}` endpoint with a valid fund ID.
2. Verify the response status code.
3. Verify the response contains details of the specified fund.
4. Verify the correctness of the response data format.

**Expected Results:**
- The response status code should be 200 (OK).
- The response should contain details of the specified fund.
- The response data format should be JSON.

**Actual Results:**
- The response status code is 200 (OK).
- The response contains details of the specified fund.
- The response data format is JSON.

**Test Data:** Valid fund ID

**Postconditions:**
- The application state remains unchanged.
---
### TC004: Verify Updating Performance of a Fund

**Test Case Title:** Verify Updating Performance of a Fund

**Description:**
This test case will verify the functionality of updating the performance of a fund using its ID through the API endpoint.

**Preconditions:**
- The application is installed and running.
- The database contains at least one fund entry.

**Test Steps:**
1. Send a PUT request to the `/funds/{fund_id}` endpoint with a valid fund ID and updated performance data.
2. Verify the response status code.
3. Verify the performance of the specified fund is updated in the database.

**Expected Results:**
- The response status code should be 200 (OK) or 204 (No Content).
- The performance of the specified fund should be updated in the database.

**Actual Results:**
- The response status code is 200 (OK) or 204 (No Content).
- The performance of the specified fund is updated in the database.

**Test Data:**
- Valid fund ID
- Updated performance data

**Postconditions:**
- The database contains the updated performance of the fund.
---
### TC005: Verify Deleting a Fund

**Test Case Title:** Verify Deleting a Fund

**Description:**
This test case will verify the functionality of deleting a fund using its ID through the API endpoint.

**Preconditions:**
- The application is installed and running.
- The database contains at least one fund entry.

**Test Steps:**
1. Send a DELETE request to the `/funds/{fund_id}` endpoint with a valid fund ID.
2. Verify the response status code.
3. Verify the specified fund is deleted from the database.

**Expected Results:**
- The response status code should be 200 (OK) or 204 (No Content).
- The specified fund should be deleted from the database.

**Actual Results:**
- The response status code is 200 (OK) or 204 (No Content).
- The specified fund is deleted from the database.

**Test Data:** Valid fund ID

**Postconditions:**
- The database no longer contains the deleted fund.
---
### TC006: Verify Error Handling for Invalid Input

**Test Case Title:** Verify Error Handling for Invalid Input

**Description:**
This test case will verify the error handling mechanism for invalid input data in API requests.

**Preconditions:**
- The application is installed and running.

**Test Steps:**
1. Send a request to the API endpoint with invalid input data.
2. Verify the response status code.
3. Verify the error message in the response.

**Expected Results:**
- The response status code should be 400 (Bad Request).
- The response should contain a clear and informative error message for the invalid input.

**Actual Results:**
- The response status code is 400 (Bad Request).
- The response contains a clear and informative error message for the invalid input.

**Test Data:** Invalid input data

**Postconditions:**
- The application state remains unchanged.
---
### TC007: Verify Error Handling for Missing Resources

**Test Case Title:** Verify Error Handling for Missing Resources

**Description:**
This test case will verify the error handling mechanism for missing resources in API requests.

**Preconditions:**
- The application is installed and running.

**Test Steps:**
1. Send a request to the API endpoint with a valid endpoint URL but with a missing resource.
2. Verify the response status code.
3. Verify the error message in the response.

**Expected Results:**
- The response status code should be 404 (Not Found).
- The response should contain a clear and informative error message for the missing resource.

**Actual Results:**
- The response status code is 404 (Not Found).
- The response contains a clear and informative error message for the missing resource.

**Test Data:** Valid endpoint URL with missing resource

**Postconditions:**
- The application state remains unchanged.
---
