from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import json
import time

def StopCode():
    test = 0
    while test == 0:
        test = input("Code Stopped please make it contiune Press(1) ")
        if test == "1":
            test = 1
    
    test = 0



# Set up Selenium WebDriver with the correct ChromeDriver path
driver = webdriver.Chrome(service=Service(r"C:\Users\muath\Desktop\Yeni klasör (2)\chromedriver-win64\chromedriver.exe"))

# Navigate to the orders page (log in first if needed)
driver.get("https://www.yemeksepeti.com/new/orders")
time.sleep(5)  # Allow initial page load

def captchaFounder(driver):
    """
    Checks if a CAPTCHA is present on the current page:
      - Looks for div.px-captcha-header 
      - If the text contains 'Before we continue...',
        it pauses so you can manually solve the CAPTCHA in the browser.
    """
    try:
        captcha_header = driver.find_element(By.CSS_SELECTOR, "div.px-captcha-header")
        if "Before we continue..." in captcha_header.text:
            print("Detected CAPTCHA: 'Before we continue...'")
            input("Solve the CAPTCHA in the browser. Once done, press ENTER to continue...")
    except NoSuchElementException:
        # If the element isn't found, there's no CAPTCHA
        print("No CAPTCHA found, continuing...")


# Wait for order elements to appear login and etc
StopCode()


# Find all order elements
order_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid^="order-item-container-"]')

if not order_elements:
    print("No orders found.")
    driver.quit()
    exit()
else:
    print(f"Found {len(order_elements)} orders on this page.")

# Extract order details
orders_data = []
for elem in order_elements:
    # Extract common attributes
    try:
        data_testid = elem.get_attribute("data-testid")
        order_id = data_testid.replace("order-item-container-", "")
    except Exception:
        order_id = None

    try:
        order_text = elem.text.strip()
    except Exception:
        order_text = None

    # Extract teslim edilme tarihi
    try:
        teslim_tarihi = elem.find_element(By.CSS_SELECTOR, '[data-testid="past-order-subtitle"]').text
    except NoSuchElementException:
        teslim_tarihi = None

    # Extract price information
    try:
        menu_detail = elem.find_element(By.CSS_SELECTOR, '[data-testid="order-item-box-description"]').text
    except NoSuchElementException:
        menu_detail = None

    # Extract restaurant name
    try:
        restaurant_name = elem.find_element(By.CSS_SELECTOR, '[data-testid="order-cart__vendor-name"]').text
    except NoSuchElementException:
        restaurant_name = None

    try:
        price_info = elem.find_element(By.CSS_SELECTOR,'[class="item-price sm:f-title-small-font-size f-title-medium-font-size sm:fw-title-small-font-weight fw-title-medium-font-weight sm:lh-title-small-line-height lh-title-medium-line-height sm:ff-title-small-font-family ff-title-medium-font-family sm:ffs-title-small-font-feature-settings ffs-title-medium-font-feature-settings"]').text   
    except NoSuchElementException:
        price_info = None

    # Save extracted data
    orders_data.append({
        "order_id": order_id,
        "list_page_text": order_text,
        "teslim_tarihi": teslim_tarihi,
        "menu_detail": menu_detail,
        "restaurant_name": restaurant_name,
        "price_info": price_info
    })

# Save data to a JSON file
output_path = "yemeksepeti_orders_listing.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(orders_data, f, ensure_ascii=False, indent=4)

print(f"Saved listing data to '{output_path}'.")
