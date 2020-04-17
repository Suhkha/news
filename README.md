# Project Title
Basic scraping news

## Getting Started

- Activate virtual enviroment
```
source venv/bin/activate
```
- Run project
```
python3 api.py
```

- Run basic test
```
pytest test.py
```

### Prerequisites

- Install dependencies 
```
pip install -r requirements.txt
```

### Installing
- Activate virtual enviroment
```
source venv/bin/activate
```
- Run project
```
python3 api.py
```

- In Postman, import the collection "Scraping Endpoints.postman_collection.json"

- This file contains two endpoints:
First:
```
http://127.0.0.1:5000/api/new_keyword
```
Where you can add the keyword, like this:
```
{"keywords" : "vacuna"}
```

Second: 
```
http://127.0.0.1:5000/api/get_news
```
Where the data is extracted from google results and getting news from different sources

To deactivate virtual enviroment
```
deactivate
```

## Running the tests

- Run basic test
```
pytest test.py
```