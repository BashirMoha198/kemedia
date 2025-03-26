Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def click_button(url, button_xpath):
...     try:
...         driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
...         driver.get(url)
... 
...         # Wait for the button to be clickable
...         button = WebDriverWait(driver, 10).until(
...             EC.element_to_be_clickable((By.XPATH, button_xpath))
...         )
... 
...         button.click()
...         time.sleep(5) #give the page time to respond.
...     except Exception as e:
...         print(f"An error occurred: {e}")
...     finally:
...         if 'driver' in locals(): #check if the driver was initiated.
...             driver.quit()
... 
... # Example usage (replace with actual URL and XPath)
... # This is an example, and not intended for clicking on ads.
... example_url = "https://kemedia.co.ke"
... example_button_xpath = "//*[@id="APjFqb"]"
... 
... #click_button(example_url, example_button_xpath)
... 
... print("Okay.")
SyntaxError: invalid syntax
>>> [DEBUG ON]
>>> [DEBUG OFF]
