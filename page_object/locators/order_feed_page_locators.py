from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER_FEED_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/feed']")
    ORDER_NUMBER_LOCATOR = (
    By.XPATH, "//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']")
    ORDER_FEED_ORDER_LIST_ITEM_LOCATOR = (By.XPATH,
                                          "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')]")
    ORDER_FEED_COUNTER_LOCATOR = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text.text_type_digits-large")


