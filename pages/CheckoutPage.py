from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.iframe = self.page.frame_locator('div#stripe-payment-form > div > iframe')


    def assert_checkout_page(self, giftCard):
        expect(self.page.locator("#confirm-voucher-value")).to_contain_text(giftCard.value)
        expect(self.page.locator("#confirm-payment-amount")).to_contain_text(giftCard.value)
        expect(self.page.locator("#confirm-purchaser-email")).to_contain_text(giftCard.email)
        expect(self.page.locator("#confirm-recipient-email")).to_contain_text(giftCard.recipient_email)
        expect(self.page.get_by_role("banner")).to_contain_text("Checkout")

    def fill_credit_card_details(self, creditCard):
        self.iframe.locator('xpath=//input[@name="cardnumber"]').wait_for(state='visible', timeout=10000)
        cardnumber_input = self.iframe.locator('xpath=//input[@name="cardnumber"]')

        cardnumber_input.click()
        cardnumber_input.fill(creditCard.card_number)

        self.iframe.locator('xpath=//input[@name="exp-date"]').wait_for(state='visible', timeout=10000)
        date_input = self.iframe.locator('xpath=//input[@name="exp-date"]')

        date_input.click()
        date_input.fill(creditCard.date)

        self.iframe.locator('xpath=//input[@name="cvc"]').wait_for(state='visible', timeout=10000)
        date_input = self.iframe.locator('xpath=//input[@name="cvc"]')

        date_input.click()
        date_input.fill(creditCard.cvc)

    def click_submit(self):
        self.page.get_by_role("button", name="Submit").click()


