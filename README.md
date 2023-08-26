# Twitter Scraper

This script allows you to automate the process of logging into Twitter and scraping the latest tweets from a specific user. The script mimics human-like behaviors, such as randomized delays and scroll patterns, to reduce the risk of being flagged as a bot.

## Prerequisites

1. **Python 3:** You should have Python 3 installed on your system.
2. **Google Chrome:** This script uses the Chrome WebDriver, so you should have Google Chrome installed.
3. **ChromeDriver:** Download the appropriate version of ChromeDriver based on your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the root directory of this repository or any location in your system's PATH.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vucinatim/twitter-scraper.git
   cd twitter-scraper
   ```

2. **Set up a Virtual Environment (optional, but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Libraries:**

   ```bash
   pip install -r requirements.txt
   ```

   Note: You should create a `requirements.txt` in the root directory with the following content:

   ```
   selenium==3.141.0
   beautifulsoup4==4.9.3
   tqdm==4.56.0
   ```

## Usage

1. Update your Twitter credentials in the script:

   ```python
   my_username = 'your.email@domain.com'
   my_password = '****************'
   ```

2. Run the script:

   ```bash
   python twitter_scraper.py
   ```

3. After execution, you'll find a `tweets.csv` file in the root directory containing the extracted tweets.

## Contribution

Feel free to fork this repository, and make modifications. If you have any suggestions or improvements, pull requests are always welcome!

## Disclaimer

This script is for educational purposes only. Always respect the terms of service of the website you are scraping.
