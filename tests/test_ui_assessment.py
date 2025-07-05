import pytest
import allure

from utils import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.board_page import BoardPage


@pytest.mark.usefixtures("page", "test_data")
class TestUIAssessment:
    """UI end-to-end flow: dashboard → board → lists."""

    @pytest.mark.dependency(name="navigate_dashboard")
    @allure.description("Test case 1: Navigate to Dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_dashboard(self, page, test_data):
        dashboard = DashboardPage(page)
        base_url = test_data["env"]["base_url"]
        assert dashboard.navigate_to_dashboard(base_url), "Navigation to Dashboard failed"
        take_screenshot(page, "Navigated to Dashboard")

    @pytest.mark.dependency(
        name="create_board",
        depends=["navigate_dashboard"]
    )
    @allure.description("Test case 2: Create New Board")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_board(self, page, test_data):
        board_name = test_data["testing_parameters"]["board_name"]
        dashboard  = DashboardPage(page)
        assert dashboard.create_new_board(board_name), f"Could not create board '{board_name}'"
        take_screenshot(page, "Board Created")

        board_page = BoardPage(page)
        assert board_page.verify_board_created(board_name), f"Board '{board_name}' not found"

    @pytest.mark.dependency(
        name="create_lists",
        depends=["create_board"]
    )
    @allure.description("Test case 3: Create New Lists")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_lists(self, page, test_data):
        lists = test_data["testing_parameters"]["list_name"]
        board_page = BoardPage(page)

        for name in lists:
            assert board_page.create_new_list(name), f"Failed to create list '{name}'"
        take_screenshot(page, "Lists Created")

        assert board_page.verify_list(lists), "Not all lists are visible on the board"

    @pytest.mark.dependency(
        name="delete_list",
        depends=["create_lists"]
    )
    @allure.description("Test case 4: Delete a List")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_list(self, page, test_data):
        lists = test_data["testing_parameters"]["list_name"]
        target = lists[1]
        board_page = BoardPage(page)

        assert board_page.delete_list(target), f"Failed to delete list '{target}'"
        take_screenshot(page, "List Deleted")

        assert board_page.verify_list_deleted(target), f"List '{target}' still present"
