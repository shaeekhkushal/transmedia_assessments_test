# UI Automation Framework with Playwright, Pytest & Allure

This project is a UI test automation suite built using **Playwright**, **Pytest**, and **Allure** reporting. It validates end-to-end user interactions such as creating boards, managing lists, and verifying UI changes. Screenshots are embedded in Allure reports for better traceability.

---

## 🚀 Tech Stack

| Tool               | Purpose                           |
|--------------------|------------------------------------|
| `Playwright`       | Browser automation engine          |
| `Pytest`           | Test runner and assertion engine   |
| `Allure`           | Test reporting with screenshots    |

---

## 📁 Project Structure

  UI_Assessment/
  ├── pages/               
  ├── tests/                
  ├── resources/           
  ├── conftest.py           
  ├── pytest.ini            
  ├── utils.py              
  └── requirements.txt      

## Features
- Comprehensive end-to-end UI automation scenarios implemented
- Efficient management of browser sessions and contexts
- Automatic screenshot capture upon test failures
- Seamless integration with Allure for detailed reporting
- Allure reports are automatically generated after test runs
- Allure reports are immediately available via a local server post-execution



## View Allurew report
[Report link](https://shaeekhkushal.github.io/transmedia_ui_assessment_report/)



## API Automation (via Postman)
**Tools & Stack Used**
- **Tool**: Complete API testing flow executed directly in Postman
- **Execution**: All test cases run manually and within Postman’s collection runner
- **Assertions**: Implemented using Postman’s built-in scripting capabilities

# Project Structure
  API_Assessment/
  ├── Transedia-API-assessment.postman_collection.json
  ├── Transmedia-API-env.postman_environment.json




# Setup & Run
**UI Tests**
  pip install -r requirements.txt
  pytest path\to\your\test_file.py

**API Tests**
  newman run Postman_Collection.json \
    -e Postman_Environment.json \

**Requirements**
Python 3.11+
Node.js & Postman
Allure CLI

