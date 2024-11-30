from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти" на главной странице
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")

    # Кнопка "Личный кабинет" на главной странице
    PROFILE_BUTTON_MAIN = (By.XPATH, "//a[@href='/account']//p[text()='Личный Кабинет']")

    # Кнопка "Конструктор" на главной странице
    CONSTRUCTOR_BUTTON_LOCATOR = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX")

    # Блок конструктора на главной странице
    CONSTRUCTOR_LOCATOR = (By.CSS_SELECTOR, ".BurgerIngredients_ingredients__menuContainer__Xu3Mo")

    # Кнопка "Лента заказов" на главной странице
    ORDER_FEED_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/feed']")

    # Локатор для ингредиента в списке
    INGREDIENT_ITEM_LOCATOR = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6")

    # Локатор модального окна с деталями ингредиента
    MODAL_WINDOW_LOCATOR = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]")

    # Кнопка закрытия модального окна
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close_modified__3V5XS")

    # Локатор корзины
    BASKET_LOCATOR = (By.CSS_SELECTOR, ".BurgerConstructor_basket__listItem__aWMu1")

    # Локатор цены в корзине
    BASKET_PRICE_LOCATOR = (By.CSS_SELECTOR, ".constructor-element__price")

    # Кнопка "Оформить заказ"
    BUTTON_PLACE_ORDER = (
    By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Оформить заказ')]")

    ORDER_NUMBER_LOCATOR_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")

    MODAL_CLOSE_BUTTON_LOCATOR = (By.XPATH,
                                  "//button[contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]")



