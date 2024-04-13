import time

class BasePage:

    def __init__(self, browser):
        self.driver = browser
        
    # Generic testing methods

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def write(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.find_element(*locator).click()

    def capture_element_text(self, locator):
        return self.driver.find_element(*locator).text


    # Generic testing methods

    def navigate_to(self, url):
        self.driver.get(url)        

    def assert_element_displayed(self, locator):
        assert self.driver.find_element(*locator).is_displayed(), f"The element {locator} was NOT fount in the web page."

    def assert_element_NOT_displayed(self, locator):
        assert self.driver.find_elements(*locator) < 0, f"The element {locator} WAS found in the web page. Expected behaviour: not found."

    def assert_page_title(self, page_title_locator, expected_text):
        self.assert_element_displayed(page_title_locator)
        captured_text = self.capture_element_text(page_title_locator)
        assert captured_text == expected_text, f"Captured text: {captured_text} did not match expected text {expected_text}"

    def convert_datatable_to_list(self, data_table):
        lines = data_table.split('\n')
        parsed_list = []
        for line in lines:
            # if the data-table has a single value per line, the output is a list.
            # if the data-table has several values per line, the output will be a list of lists.
            items = line.strip().split('|')
            items = [item.strip() for item in items]
            if len(items) == 1 and items[0]:
                parsed_list.append(items[0])
            else:
                parsed_list.append(items)
        return parsed_list