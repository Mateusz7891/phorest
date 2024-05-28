from playwright.sync_api import Playwright, sync_playwright

from builders.CreditCardBuilder import CreditCardBuilder
from builders.GiftCardBuilder import GiftCardBuilder
from enums.URL import URL
from pages.BuyGiftCardPage import BuyGiftCardPage
from pages.CheckoutPage import CheckoutPage
from pages.Footer import Footer
from pages.PuchaseCompletePage import PurchaseCompletePage
from pages.SummaryPage import SummaryPage


def send_to_me_test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto(URL.LANDING_PAGE.value)

    gift_card = GiftCardBuilder().with_send_to_me_data().build()

    footer = Footer(page)

    buy_gift_page = BuyGiftCardPage(page)
    buy_gift_page.fill_gift_page_send_to_me(gift_card)
    buy_gift_page.assert_gift_page(gift_card)
    footer.assertFooter()

    summary_page = SummaryPage(page)
    summary_page.assert_summary_page(gift_card)
    summary_page.clickConfirmDetails()
    footer.assertFooter()

    checkout_page = CheckoutPage(page)
    checkout_page.assert_checkout_page(gift_card)
    footer.assertFooter()

    credit_card = CreditCardBuilder().with_test_data().build()

    checkout_page.fill_credit_card_details(credit_card)
    footer.assertFooter()
    checkout_page.click_submit()

    purchase_complete_page = PurchaseCompletePage(page)
    purchase_complete_page.assertPurchaseCompletePage(gift_card)
    footer.assertFooter()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    send_to_me_test(playwright)