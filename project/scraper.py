
from playwright.sync_api import sync_playwright, Playwright, expect


def scrape(iterations):
    game_list = []
    with sync_playwright() as playwright:
        for iteration in range(iterations):
            browser = openBrowser(playwright, headless_value=False, ignore_default_args_value=["--mute-audio"])
            page = getPage(browser, "https://papergames.io/en/battleship")
            try:
                play_robot_button = page.locator('app-juicy-button').get_by_text('Play vs robot')
                play_robot_button.click()
                name_textbox = page.get_by_role('textbox')
                name_textbox.fill('lom')
                name_confirm_button = page.get_by_text('Continue')
                name_confirm_button.click()
                table = page.get_by_role('table').first
                expect(table).to_be_visible()

                cells = set()
                for x in range(10):
                    for y in range(10):
                        class_string = table.locator('.cell-'+str(x)+'-'+str(y)).first.get_attribute('class')
                        if 'undefined' not in class_string:
                            cells.add((x, y))
                game_list.append(cells)
            except Exception as e:
                write_to("errors.log", "Unexpected Error: "+str(e))
            browser.close()
            print(iteration+1)
        playwright.stop()
    write_to("data.csv", game_list)



def openBrowser(playwright: Playwright, headless_value, ignore_default_args_value):
    chromium = playwright.chromium # or "firefox" or "webkit".
    return chromium.launch(headless=headless_value,ignore_default_args=ignore_default_args_value)

def getPage(browser, url):
    page = browser.new_page()
    page.goto(url)
    return page

def write_to(filename, value_set):
    file = open(filename, 'a')
    for value in value_set:
        file.write(str(value)+"\n")
    file.close()



scrape(5)