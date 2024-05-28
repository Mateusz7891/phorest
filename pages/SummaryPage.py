from playwright.sync_api import expect


class SummaryPage:

    def __init__(self, page):
        self.page = page

    def assert_summary_page(self, giftCard):
        expect(self.page.locator("#confirm-voucher-value")).to_contain_text(giftCard.value)
        expect(self.page.locator("#confirm-payment-amount")).to_contain_text(giftCard.value)
        expect(self.page.locator("#confirm-purchaser-email")).to_contain_text(giftCard.email)
        expect(self.page.locator("#confirm-recipient-email")).to_contain_text(giftCard.recipient_email)
        expect(self.page.get_by_role("banner")).to_contain_text("Summary")

    def clickConfirmDetails(self):
        self.page.get_by_role("button", name="Confirm Details").click()

    def clickEdit(self):
        self.page.get_by_role("button", name="Edit").click()
