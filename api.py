from flask import Flask, jsonify, request
from config import config
from models import db
from models import News
import urllib
import requests
from bs4 import BeautifulSoup
import nltk
from nltk import FreqDist


def create_app(enviroment):
  app = Flask(__name__)
  app.config.from_object(enviroment)
  with app.app_context():
    db.init_app(app)
    db.create_all()
  return app

enviroment = config['development']
app = create_app(enviroment)

# user-agent
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}

list_of_keywords = { "keywords": [ "china", "covid", "mexico", "hospitales" ]}
keywords = list_of_keywords.get('keywords')

@app.route('/api/get_news', methods=['GET'])
def get_news():
  # Initialize the list
  results = []

  # Iterate each keyword of the list
  for keyword in keywords:

    # Asign to the URL the keyword to search
    URL = "https://google.com/search?q="+keyword
    search = requests.get(URL, headers=HEADERS)
  
    # If the search has a 200 status we parse the content found
    if search.status_code == 200:
      response = BeautifulSoup(search.content, "html.parser")

      # In the response we find the common class rc and their anchors
      for new in response.find_all('div', class_='rc', limit=3):
        anchors = new.find_all('a')

        if anchors:

          # Get the content of anchor: href
          link = anchors[0]['href']

          # Get the text of the results, like title and excerpt of the post/article according to specific tags and class
          title = new.find('h3').text
          excerpt = new.find('span', class_='st').text
          news = {
            "keyword" : keyword,
            "title" : title,
            "reference" : link,
            "excerpt" : excerpt
          }

          # Join content of the excerpt and title, and pass to lowercase to ensure a better count of frequency words
          full_text = news['excerpt'].lower() + news['title'].lower()
          text = full_text.split(" ")
          FreqDistBody = FreqDist(text)
          frequency = FreqDistBody[keyword]

          # Adding a new key value pair to news
          news.update( {'frequency' : frequency} )
  
          results.append(news)

          # Store in database the results of the search
          new = News.create(news['title'], news['excerpt'],news['reference'],  news['keyword'], news['frequency'])
          
  return jsonify(sorted(results, key=lambda k:k['frequency'], reverse=True))


@app.route('/api/new_keyword', methods=['POST'])
def add_keyword():
  # Get new keyword and add to the original list of keywords
  keyword = {'new_keyword' : request.json['keywords']}
  list_of_keywords['keywords'].append(keyword['new_keyword'])

  return jsonify(list_of_keywords)

if __name__ == '__main__':
  app.run(debug=True)