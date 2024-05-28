from playwright.sync_api import expect


class PurchaseCompletePage:

    def __init__(self, page):
        self.page = page

    def assertPurchaseCompletePage(self, giftCard):
        expect(self.page.locator("body")).to_contain_text("Your gift card has been sent. We've also sent you a receipt.", timeout=10000)
        expect(self.page.get_by_role("banner")).to_contain_text("Purchase Complete")
        expect(self.page.locator("body")).to_contain_text(giftCard.value)
        expect(self.page.locator("body")).to_contain_text("Payment accepted, thank you!")