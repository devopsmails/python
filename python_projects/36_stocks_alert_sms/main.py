import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "L2Y4FINQF8P3S1U6"
NEWS_API_KEY = "32c3f0dfb669425193057fdc87fc5733"

TWILIO_ACCOUNT_SID = "ACf225f87a311e49354524c4f56b8df5c4"
TWILIO_AUTH_TOKEN = "bea638d09ab50b3fc1f63564ab78cc44"

stock_params = {
    "function" : "TIME_SERIES_WEEKLY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}
## Use https://www.alphavantage.co/documentation/#daily


#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Weekly Time Series"]
data_list = [value for (key, value) in data.items()]
last_week = data_list[0]
last_week_closing_price = last_week["4. close"]

# Get the day before yesterday's closing stock price
second_last_week = data_list[1]
second_last_week_closing_price = second_last_week["4. close"]

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(last_week_closing_price) - float(second_last_week_closing_price)
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round(float(difference) / float(last_week_closing_price) * 100)
print(diff_percentage)

if diff_percentage <2:
    news_params = {
        "q" : COMPANY_NAME,
        "apiKey" : NEWS_API_KEY,

    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_article = response.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    last_three_articles = news_article[:3]

#Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Stock: {STOCK_NAME}{up_down}\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in last_three_articles]
    print(formatted_articles)
#Send each article as a separate message via Twilio. 
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17602538114",
            to="+919347589813"
        )


