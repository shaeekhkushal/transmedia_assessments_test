from playwright.sync_api import Page, expect
import allure


class BoardPage:
    def __init__(self, page: Page):
        self.page = page

    def _board_name_div(self):
        return (
            self.page
                .locator("input[name='board-title']")
                .locator("xpath=../div[1]")
        )

    def _list_locators(self):
        return {
            "add_modal": self.page.locator('div[data-cy="create-list"]'),
            "input":     self.page.locator('input[data-cy="add-list-input"]'),
            "all":       self.page.locator("input[data-cy='list-name']")
        }

    @allure.step("Verify board is created: {expected_board_name}")
    def verify_board_created(self, expected_board_name: str) -> bool:

        self.page.wait_for_selector("input[name='board-title']")
        actual = self._board_name_div().text_content().strip()
        return actual == expected_board_name

    @allure.step("Create new list: {list_name}")
    def create_new_list(self, list_name: str) -> bool:
        locs = self._list_locators()
        before = locs["all"].count()

        if locs["add_modal"].count() > 0:
            locs["add_modal"].click()

        locs["input"].fill(list_name)
        locs["input"].locator("xpath=../div[1]/button").click()

        expect(locs["all"]).to_have_count(before + 1, timeout=10000)
        return True

    @allure.step("Verify lists include: {expected_items}")
    def verify_list(self, expected_items: list[str]) -> bool:
        names = [el.input_value() for el in self._list_locators()["all"].all()]
        return set(expected_items).issubset(names)

    @allure.step("Delete list: {list_name}")
    def delete_list(self, list_name: str) -> bool:
        for el in self._list_locators()["all"].all():
            if el.input_value() == list_name:
                el.locator("xpath=../button").click()
                el.locator('xpath=../div[1]//div[@data-cy="delete-list"]').click()
                return True
        return False

    @allure.step("Verify list deleted: {list_name}")
    def verify_list_deleted(self, list_name: str) -> bool:
        try:
            # wait for that specific input to detach
            self.page.wait_for_selector(
                f"input[data-cy='list-name'][value='{list_name}']",
                state="detached",
                timeout=10000
            )
            return True
        except:
            return False
