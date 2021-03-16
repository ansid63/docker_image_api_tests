import requests
from TestData import GraphQLQuery
import json


class TestGraphQLQuery:
    def test_receive_country_by_id(self):
        response_country = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                         data=GraphQLQuery.DATA_COUNTRY)
        json_response_country_by_id = response_country.json()
        assert json_response_country_by_id['data']['country']['name'] == "Russia"

    def test_receive_language_name_by_code(self):
        response_language = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                          data=GraphQLQuery.DATA_LANGUAGE)
        json_response_language_by_code = response_language.json()
        assert json_response_language_by_code['data']['language']['name'] == "Slovak"

    def test_receive_continent_name_by_code(self):
        response_continent = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                           data=GraphQLQuery.DATA_CONTINENT)
        json_response_continent_by_code = response_continent.json()
        assert json_response_continent_by_code['data']['continent']['name'] == "Antarctica"

    def test_receive_language_through_filter(self):
        response_language = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                          data=json.dumps(GraphQLQuery.DATA_FILTER_LANGUAGE))
        json_response_language_by_filter = response_language.json()
        assert json_response_language_by_filter['data']['languages'][0]['name'] == "Indonesian"

    def test_receive_country_through_filter(self):
        response_country = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                         data=json.dumps(GraphQLQuery.DATA_FILTER_COUNTRY))
        json_response_country_by_filter = response_country.json()
        assert json_response_country_by_filter['data']['countries'][0]['emoji'] == "🇮🇩"

    def test_receive_country_through_filter_in_continents(self):
        response_continents = requests.post(GraphQLQuery.API_URL, headers=GraphQLQuery.HEADERS,
                                            data=json.dumps(GraphQLQuery.FILTER_CONTINENTS))
        json_response_continents_by_filter = response_continents.json()
        assert json_response_continents_by_filter['data']['continents'][0]['countries'][13]['name'] == "New Zealand"
