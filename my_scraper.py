# Import necessary modules
from selenium import webdriver  # To control the browser
from selenium.webdriver.common.by import By  # Enum for element locating strategy
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements to load
from selenium.webdriver.chrome.service import Service  # To control the ChromeDriver service
from bs4 import BeautifulSoup  # To parse HTML content
import time  # For adding delays
import csv  # For writing to CSV files
from tqdm import tqdm  # Progress bar for loops
import random  # Generate random numbers

def human_like_delay(min_time=4, max_time=8):
    """Generate a random sleep duration within a range."""
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def human_like_scroll(browser):
    """Simulate human-like scrolling behavior."""
    # Randomly scroll a certain percentage down the page
    scroll_height = random.uniform(0.2, 0.5)
    browser.execute_script(f"window.scrollTo(0, window.document.body.scrollHeight * {scroll_height});")

def login_to_twitter(browser, username, password):
    """Log in to Twitter using provided credentials."""
    # Open Twitter login page
    browser.get('https://twitter.com/login')

    # Allow some time for the page to load
    time.sleep(3)

    # Input username/email into the appropriate field
    username_input = browser.find_element(By.XPATH, '//input[@autocomplete="username"]')
    username_input.send_keys(username)

    # Click on 'Next' button to proceed
    next_button = browser.find_element(By.XPATH, '//div[@role="button" and .//span[text()="Next"]]')
    next_button.click()

    # Wait a bit for the password field to become available
    time.sleep(3)

    # Input password into the appropriate field
    password_input = browser.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
    password_input.send_keys(password)

    # Click on the 'Log in' button to complete the login
    login_button = browser.find_element(By.XPATH, '//div[@role="button" and .//span[text()="Log in"]]')
    login_button.click()

    # Allow some time for the login to process
    time.sleep(5)

def get_latest_tweets(browser, user, n):
    """Retrieve the latest tweets from a specific user."""
    
    # Open user's Twitter page
    browser.get(f'https://twitter.com/{user}')
    print(f"Fetching latest {n} tweets from @{user}...")

    # This will ensure elements on the page have loaded
    wait = WebDriverWait(browser, 10)
    
    extracted_tweets = []

    # Loop to scroll down the user's page to load more tweets
    for _ in tqdm(range(n // 10), desc="Scrolling to load tweets"):
        # Parse the current tweets visible on the page
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tweet in soup.find_all('article'):
            text_div = tweet.find("div", {"lang": True})  # Look for the tweet text
            time_div = tweet.find("time")  # Look for the timestamp of the tweet

            # Check if both text and timestamp are found
            if text_div and time_div:
                text = text_div.get_text()
                datetime_posted = time_div["datetime"]
                tweet_data = {"text": text, "datetime": datetime_posted}
                if tweet_data not in extracted_tweets:
                    extracted_tweets.append(tweet_data)

        # Stop scrolling if we've extracted enough tweets
        if len(extracted_tweets) >= n:
            break

        # Occasionally refresh the page
        if random.choice([True] + [False]*9):  # 10% chance to refresh
            browser.refresh()
            human_like_delay(0, 2)

        # Simulate a human-like scrolling pattern
        human_like_scroll(browser)
        human_like_delay()

    # Close the browser after extraction is done
    browser.quit()

    # Return the required number of tweets
    return extracted_tweets[:n]

def write_to_csv(tweets, filename="tweets.csv"):
    """Write the list of tweets to a CSV file."""
    print("Writing tweets to CSV...")

    # Open the CSV file for writing
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the headers to the CSV file
        writer.writerow(["No", "Tweet", "Datetime"])

        # Write each tweet to the CSV file
        for idx, tweet_data in enumerate(tweets, 1):
            writer.writerow([idx, tweet_data["text"], tweet_data["datetime"]])

# This code will only execute if the script is run as the main program
if __name__ == "__main__":
    user = 'elonmusk' # Twitter handle of the user you're interested in
    n = 100 # Number of tweets to extract, not really working as expected
    
    # Setup the Chrome driver service
    service = Service(executable_path='./chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')  # Browse in incognito mode
    browser = webdriver.Chrome(service=service, options=options)
    
    # Add your Twitter credentials here
    my_username = 'your.email@domain.com'
    my_password = '****************'
    
    # Log in to Twitter
    login_to_twitter(browser, my_username, my_password)
    
    # Extract the latest tweets
    tweets = get_latest_tweets(browser, user, n)
    
    # Write the tweets to a CSV file
    write_to_csv(tweets)

    # Close the browser
    browser.quit()

    # Notify the user about the successful extraction
    print(f"{len(tweets)} tweets written to 'tweets.csv'")
