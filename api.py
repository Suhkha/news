from flask import Flask, jsonify
import urllib
import requests
from bs4 import BeautifulSoup
import nltk

app = Flask(__name__)
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

list_of_keywords = { "keywords": [ 
  "china", 
  "covid", 
  "mexico", 
  "hospitales" 
]}

keywords = list_of_keywords.get('keywords')

@app.route('/api/get_news', methods=['GET'])
def get_news():
  results = []
  for keyword in keywords:
    URL = "https://google.com/search?q="+keyword
    headers = {"user-agent": USER_AGENT}
    search = requests.get(URL, headers=headers)

    if search.status_code == 200:
      response = BeautifulSoup(search.content, "html.parser")
      for new in response.find_all('div', class_='r'):
        anchors = new.find_all('a')
        if anchors:
          link = anchors[0]['href']
          title = new.find('h3').text
          news = {
            "keyword": keyword,
            "content": title,
            "reference": link,
            "ranking" : freqdist1
          }
          results.append(news)
          
  return jsonify(results)


@app.route('/api/new_keyword', methods=['POST'])
def add_keyword():
  keyword = {'new_keyword' : request.json['keywords']}
  list_of_keywords['keywords'].append(keyword['new_keyword'])
  return jsonify(list_of_keywords)

if __name__ == '__main__':
  app.run(debug=True)