from playwright.sync_api import expect


class BuyGiftCardPage:

    def __init__(self, page):
        self.page = page

    def fill_gift_page_send_to_me(self, giftCard):
        self.page.get_by_label(giftCard.value).check()
        self.page.get_by_text("Your Email Address").click()
        expect(self.page.locator("body")).to_contain_text(giftCard.value)
        self.page.get_by_placeholder("the receipt will be sent here").click()
        self.page.get_by_placeholder("the receipt will be sent here").fill(giftCard.email)
        self.page.get_by_placeholder("first name").click()
        self.page.get_by_placeholder("first name").fill(giftCard.first_name)
        self.page.get_by_placeholder("last name").click()
        self.page.get_by_placeholder("last name").fill(giftCard.last_name)
        self.page.get_by_role("button", name="Checkout").click()

    def fill_gift_page_send_to_someone_else(self, giftCard):
        self.page.get_by_label(giftCard.value).check()
        self.page.get_by_role("link", name="Send to someone else").click()
        self.page.get_by_text("Your Email Address").click()
        expect(self.page.locator("body")).to_contain_text(giftCard.value)
        self.page.get_by_placeholder("the receipt will be sent here").fill(giftCard.email)
        self.page.get_by_placeholder("first name").fill(giftCard.first_name)
        self.page.get_by_placeholder("last name").fill(giftCard.last_name)
        self.page.get_by_placeholder("gift card will be sent here").fill(giftCard.recipient_email)
        self.page.get_by_placeholder("type your message here eg. Hi").fill(giftCard.recipient_message)
        self.page.get_by_role("button", name="Checkout").click()

    def fill_gift_page_send_to_me_other(self, giftCard):
        self.page.get_by_label("Other").check()
        self.page.get_by_role("spinbutton").fill(giftCard.value)
        self.page.get_by_text("Your Email Address").click()
        expect(self.page.locator("body")).to_contain_text(giftCard.value)
        self.page.get_by_placeholder("the receipt will be sent here").click()
        self.page.get_by_placeholder("the receipt will be sent here").fill(giftCard.email)
        self.page.get_by_placeholder("first name").click()
        self.page.get_by_placeholder("first name").fill(giftCard.first_name)
        self.page.get_by_placeholder("last name").click()
        self.page.get_by_placeholder("last name").fill(giftCard.last_name)
        self.page.get_by_role("button", name="Checkout").click()

    def fill_gift_page_send_to_someone_else_other(self, giftCard):
        self.page.get_by_label("Other").check()
        self.page.get_by_role("spinbutton").fill(giftCard.value)
        self.page.get_by_text("Your Email Address").click()
        expect(self.page.locator("body")).to_contain_text(giftCard.value)
        self.page.get_by_placeholder("the receipt will be sent here").fill(giftCard.email)
        self.page.click("//a[contains(text(), 'Send to someone else')]")
        self.page.get_by_placeholder("first name").fill(giftCard.first_name)
        self.page.get_by_placeholder("last name").fill(giftCard.last_name)
        self.page.get_by_placeholder("gift card will be sent here").fill(giftCard.recipient_email)
        self.page.get_by_placeholder("type your message here eg. Hi").fill(giftCard.recipient_message)
        self.page.get_by_role("button", name="Checkout").click()

    def assert_gift_page(self, giftCard):
        expect(self.page.locator("body")).to_contain_text(giftCard.value)


