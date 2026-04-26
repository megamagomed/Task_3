import allure


class TestOrderFeed:
    @allure.title("Проверка открытия деталей ингредиента по клику на заказ в ленте")
    def test_click_on_ingredient_show_popup(self, order_feed_page):
        order_feed_page.open_order_feed_page()
        burger_name_in_order = order_feed_page.get_burger_name_in_order()
        order_feed_page.click_to_order()
        burger_name_in_popup = order_feed_page.get_burger_name_in_popup()
        assert burger_name_in_order == burger_name_in_popup

    @allure.title("Проверка отображения заказа из истории в ленте заказов")
    def test_order_from_history_displayed_in_order_feed(
        self, main_page, user_login, personal_account_page, order_feed_page
    ):
        main_page.create_order_and_get_order_number()
        main_page.click_user_profile_button()
        personal_account_page.click_order_history_button()
        history_orders = personal_account_page.get_all_order_numbers_from_history()
        order_feed_page.open_order_feed_page()
        feed_orders = order_feed_page.get_all_order_numbers_from_feed()
        assert all(order in feed_orders for order in history_orders)

    @allure.title("Проверка увеличения счетчика заказов за все время")
    def test_all_time_counter_increased(self, main_page, user_login, order_feed_page):
        order_feed_page.open_order_feed_page()
        before = order_feed_page.get_counter_value("all_time")

        main_page.create_order_and_get_order_number()
        order_feed_page.open_order_feed_page()
        after = order_feed_page.get_counter_value("all_time")

        assert after > before

    @allure.title("Проверка увеличения счетчика заказов за сегодня")
    def test_today_counter_increased(self, main_page, user_login, order_feed_page):
        order_feed_page.open_order_feed_page()
        before = order_feed_page.get_counter_value("today")

        main_page.create_order_and_get_order_number()
        order_feed_page.open_order_feed_page()
        after = order_feed_page.get_counter_value("today")

        assert after > before

    @allure.title('Проверка отображения нового заказа в разделе "В работе"')
    def test_order_appears_in_progress_section(
        self, main_page, user_login, order_feed_page
    ):

        order_number = main_page.create_order_and_get_order_number()

        order_feed_page.open_order_feed_page()
        order_number_with_zero = order_feed_page.add_leading_zero_to_order_number(
            order_number
        )
        order_number_in_progress = order_feed_page.get_order_in_progress()
        assert order_number_with_zero == order_number_in_progress
