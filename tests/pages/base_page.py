from selenium.webdriver.common.by import By

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
            items = [item.strip() for item in items if item.strip()] # if item.strip() evaluates to false if ''. so it effectively skips empty list item
            if len(items) == 1 and items[0]:
                parsed_list.append(items[0])
            else:
                parsed_list.append(items)
        return parsed_list
    
    def assert_list_of_locators(self, locators, attr_table):
        for row in attr_table:
            for element_name in row:
                locator = locators.get(element_name)
                if locator:
                    assert self.assert_element_displayed(locator), f"Element '{locator}' is not visible"


    def form_filler_multiple_fields_friendly_matcher(self, locators: dict, attr_table: str):
        # receives a {"friend name": "locator_name"} and the parsed [["friendly name1", "friendly name2"]["input value1", "input value"]]
        # returns matched {"locator_name": "value"}
        # eg: 
        # locators = {"First Name": "field_first_name_locator", "Last Name": "field_last_name_locator", "Zip/Postal Code": "field_postal_code_locator"}
        # converted attr_table [['First Name', 'Last Name', 'Zip/Postal Code'], ['Antonio', 'Santos', '4567-123']]
        # data_dict = {'field_first_name_locator': 'Antonio', 'field_last_name_locator': 'Santos', 'field_postal_code_locator': '4567-123'}
        # however, 
        # the data_dict must be returned to the child class so the field_first_name_locator gets replaced by
        # a child class attribute values, such as (CheckoutPage) self.field_first_name_locator (By.XPATH, "//input[@id='first-name']")

        print("-------------------- initial_attr_table")
        print(attr_table)

        attr_table = self.convert_datatable_to_list(attr_table)
        data_dict = {}
        for i in range(len(attr_table[0])):
            attribute_name = attr_table[0][i]
            locator_key = locators.get(attribute_name)
            if locator_key:
                data_dict[locator_key] = attr_table[1][i]
        return data_dict
