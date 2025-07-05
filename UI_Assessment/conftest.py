import json
import shutil
import subprocess
import logging
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright, Page

REPORTS_DIR = Path("reports")
ALLURE_RESULTS = REPORTS_DIR / "allure-results"
ALLURE_REPORT = REPORTS_DIR / "allure-report"
TEST_DATA_FILE = Path("resources/test_data.json")


def _clear_dir(path: Path) -> None:
    """Remove all contents of a directory and recreate it."""
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def pytest_sessionstart(session):
    """Prepare report directories before any tests run."""
    _clear_dir(ALLURE_RESULTS)
    _clear_dir(ALLURE_REPORT)


@pytest.fixture(scope="session")
def browser_context():
    """Launch a Chromium browser and yield its context once per session."""
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1080, "height": 950})
        yield context
        browser.close()


@pytest.fixture(scope="session")
def page(browser_context) -> Page:
    """
    Open exactly one tab for the entire session.
    All tests share this `page`, so no new tabs/windows will be created.
    """
    single_page = browser_context.new_page()
    yield single_page
    single_page.close()


@pytest.fixture(scope="session")
def test_data() -> dict:
    """Load test data from JSON once per session."""
    return json.loads(TEST_DATA_FILE.read_text(encoding="utf-8"))


def pytest_sessionfinish(session, exitstatus):
    """Generate and open the Allure report when the session ends."""
    cmd = shutil.which("allure") or shutil.which("allure.bat")
    if not cmd:
        logging.warning("Allure CLI not found on PATH; skipping report generation")
        return

    try:
        subprocess.run(
            [cmd, "generate", str(ALLURE_RESULTS), "-o", str(ALLURE_REPORT), "--clean"],
            check=True
        )
        subprocess.run([cmd, "open", str(ALLURE_REPORT)], check=False)
    except subprocess.CalledProcessError as e:
        logging.error(f"Allure report generation failed: {e}")
