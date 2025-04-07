from bs4 import BeautifulSoup
import requests

# User agent to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def weather(city):
    city = city.replace(" ", "+")  # Replace spaces with "+"
    try:
        res = requests.get(f'https://www.google.com/search?q={city}+weather', headers=headers)
        print("Searching in Google...\n")
        
        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Extract information using the appropriate selectors
        location = soup.select_one('#wob_loc')  # Use select_one to avoid index errors
        time = soup.select_one('#wob_dts')
        info = soup.select_one('#wob_dc')
        temp = soup.select_one('#wob_tm')

        if location and time and info and temp:  # Check if elements exist
            print(location.getText().strip())
            print(time.getText().strip())
            print(info.getText().strip())
            print(temp.getText().strip() + "°C")
        else:
            print("Couldn't fetch weather data. Google might be blocking the request.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for city name
print("Enter the city name:")
city = input()
weather(city)
