from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

list_of_keywords = { "keywords": [ "china", "covid", "mexico" ] }

@app.route('/api/keywords', methods=['GET'])
def all_keywords():
  return jsonify(list_of_keywords)

@app.route('/api/new_keyword', methods=['POST'])
def add_keyword():
  keyword = {'new_keyword' : request.json['keywords']}
  list_of_keywords['keywords'].append(keyword['new_keyword'])
  return jsonify(list_of_keywords)

if __name__ == '__main__':
  app.run(debug=True)