from playwright.sync_api import expect


class Footer:

    def __init__(self, page):
        self.page = page

    def assertFooter(self):
        expect(self.page.locator("#footer")).to_contain_text("Arden Courts")
        expect(self.page.locator("#footer")).to_contain_text(
            "100 Juniper Street 3rd Floor, Philadelphia, 19107, United States")
        expect(self.page.locator("#footer")).to_contain_text("demousa@phorest.com")
        expect(self.page.locator("#footer")).to_contain_text("Powered by Phorest")
        expect(self.page.locator("#footer")).to_contain_text("Terms &amp; Conditions")
        expect(self.page.locator("#footer")).to_contain_text("Cancellation Policy")
        expect(self.page.locator("#footer")).to_contain_text("Privacy Policy")
