import os
import time

from playwright.sync_api import sync_playwright, Playwright, expect

last_scrape_time = 0.0
last_scrape_elapsed_time = 0.0
fastest_scrape_time = 100.0

scrapes_to_do = 5000
max_timeout = 5000
do_headless = True

def scrape(iterations):
    errors = 0
    reset_errors()
    starting_time = time.time()
    global last_scrape_time
    last_scrape_time = starting_time
    with sync_playwright() as playwright:
        browser = openBrowser(playwright, timeout=max_timeout, headless_value=do_headless,
                              ignore_default_args_value=["--mute-audio"])
        page = getPage(browser, "https://papergames.io/en/battleship")
        play_robot_button = page.locator('app-juicy-button').get_by_text('Play vs robot')
        play_robot_button.click()
        name_textbox = page.get_by_role('textbox')
        name_textbox.fill('lom')
        name_confirm_button = page.get_by_text('Continue')
        name_confirm_button.click()
        table = page.get_by_role('table').first
        expect(table).to_be_visible()
        page.close()
        for iteration in range(iterations):
            page = getPage(browser, "https://papergames.io/en/battleship")
            try:
                play_robot_button = page.locator('app-juicy-button').get_by_text('Play vs robot')
                play_robot_button.click()
                table = page.get_by_role('table').first
                expect(table).to_be_visible()

                cells = set()
                for x in range(10):
                    for y in range(10):
                        class_string = table.locator('.cell-'+str(x)+'-'+str(y)).first.get_attribute('class')
                        if 'undefined' not in class_string:
                            cells.add((x, y))
                write_to("data.txt", cells)
            except Exception as e:
                write_to("errors.log", "Unexpected Error: "+str(e))
                errors += 1
            page.close()
            try:
                log_progress(iteration+1, iterations, errors,starting_time)
            except Exception as e:
                write_to("errors.log", "Unexpected Error: " + str(e))
        playwright.stop()


def openBrowser(playwright: Playwright, timeout, headless_value, ignore_default_args_value):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=headless_value,ignore_default_args=ignore_default_args_value)
    context = browser.new_context()
    context.set_default_timeout(timeout)
    return context

def getPage(browser, url):
    page = browser.new_page()
    page.goto(url)
    return page

def write_to(filename, value):
    file = open(filename, 'a')
    file.write(str(value)+"\n")
    file.close()

def reset_errors():
    file = open("errors.log", 'w')
    file.write("")
    file.close()

def log_progress(value, max_value, errors,starting_time):
    os.system('cls')
    cur_time = time.time()
    global last_scrape_time
    global last_scrape_elapsed_time
    global fastest_scrape_time
    last_scrape_elapsed_time = cur_time - last_scrape_time
    last_scrape_time = cur_time
    fastest_scrape_time = min(fastest_scrape_time, last_scrape_elapsed_time)
    print("_______Running Scraping________")
    print("Progress: "+str(value)+"/"+str(max_value)+" ("+"{:.0%}".format(value/max_value)+")")
    print("Successful: "+str(value-errors)+" ("+"{:.0%}".format((value-errors)/value)+")")
    print("Errors: "+str(errors)+" ("+"{:.0%}".format(errors/value)+")")
    print("_________________________")
    print("Last Time: "+str(round(last_scrape_elapsed_time,2))+"s")
    print("Total Time: "+str(round(time.time()-starting_time,2))+"s")
    print("Avg Time Per Scrape: "+str(round((time.time()-starting_time)/value,2))+"s")
    print("Avg Time Per Success: "+str(round((time.time()-starting_time)/(value-errors),2))+"s")
    print("Fastest Time: "+str(round(fastest_scrape_time,2))+"s")
    print("_________________________")
    print("Max Timeout: "+str(max_timeout)+"ms")



scrape(scrapes_to_do)