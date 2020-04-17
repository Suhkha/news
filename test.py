import pytest
from models import News, db

def test_fields_of_news():
	new = News("mexico", 1)
	assert type(new.freq) is int
	assert type(new.key) is str
	return new