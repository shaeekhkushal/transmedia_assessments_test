import allure
from playwright.sync_api import Page


@allure.step("Take screenshot: {step_name}")
def take_screenshot(page: Page, step_name: str) -> None:
    """Capture a full-page screenshot and attach it to the Allure report."""
    image_bytes = page.screenshot(full_page=True)
    allure.attach(
        body=image_bytes,
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )
