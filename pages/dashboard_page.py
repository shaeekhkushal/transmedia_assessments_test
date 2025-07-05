from playwright.sync_api import Page, expect
import allure


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def _create_board_button(self):
        return self.page.locator("div.create-board")

    def _board_name_input(self):
        return self.page.locator("input.new-board-input")

    def _submit_board_button(self):
        return self.page.locator("button[data-cy='new-board-create']")

    @allure.step("Navigate to dashboard: {url}")
    def navigate_to_dashboard(self, url: str) -> bool:
        response = self.page.goto(url, wait_until="networkidle")
        return bool(response and response.ok)

    @allure.step("Create new board: {board_name}")
    def create_new_board(self, board_name: str) -> bool:

        self._create_board_button().click()
        self._board_name_input().fill(board_name)
        self._submit_board_button().click()

        board_title_input = self.page.locator("input[name='board-title']")
        expect(board_title_input).to_be_visible()

        return True
