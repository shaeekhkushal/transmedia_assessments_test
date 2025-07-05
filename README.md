# 🧪 UI Automation Framework with Playwright, Pytest & Allure

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

```bash
qa_ui_automation/
├── pages/                  # Page Object Models
├── resources/              # Test data in JSON
├── tests/                  # Test scripts
├── reports/                # Allure results & report folder
│   ├── allure-results/     # Raw results (excluded from Git)
│   ├── allure-report/      # Generated report (included in Git)
│   └── pytest_report.html  # HTML version of test run
├── conftest.py             # Pytest configurations & fixtures
├── requirements.txt        # Python dependencies
├── pytest.ini              # CLI & logging config
├── utils.py                # Screenshot helper for Allure
└── README.md               # You’re reading it 😄


## 🧪 How to Run Tests

Step 1: Install dependencies
    pip install -r requirements.txt

Step 2: Install Playwright browsers (once)
    playwright install

Step 3: Run the test suite
    pytest your_file_path/yourfile.py


This generates:

- Allure raw results → reports/allure-results/
- HTML report → reports/pytest_report.html
- Screenshot evidence → saved automatically in results

## Generating Allure Report (after test run)
Make sure Allure CLI is installed and on your system PATH.
Then run:
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open reports/allure-report





