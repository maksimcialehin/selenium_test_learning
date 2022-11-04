import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('promo_number', [pytest.param(i, marks=pytest.mark.xfail(i == 7,
                                                                                  reason='7 is a wrong number'))
                                          for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_the_same_name()
    page.should_be_the_same_price()
