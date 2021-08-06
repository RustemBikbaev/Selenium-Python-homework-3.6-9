link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_there_is_an_add_to_cart_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket[type='submit']"), "No found button to add to cart"