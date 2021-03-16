class GraphQLQuery:
    API_URL = "https://countries.trevorblades.com/"
    HEADERS_REDIRECT = {
        'Content-Type': 'application/json',
        'Origin': 'https://lucasconstantino.github.io',
        'Referer': 'https://lucasconstantino.github.io/graphiql-online/'
    }

    HEADERS = {
        'Content-Type': 'application/json',
    }

    DATA_COUNTRY = "{\"query\": \"query {country(code: \\\"RU\\\") {name}}\"}"
    DATA_LANGUAGE = "{\"query\": \"query {language(code: \\\"sk\\\") {name native}}\"}"
    DATA_CONTINENT = "{\"query\": \"query {continent(code: \\\"AN\\\") {name countries {name capital currency} } }\"}"
    DATA_FILTER_LANGUAGE = {"query": "{languages(filter: {code: {eq: \"id\"}}) {code name native}}"}
    DATA_FILTER_COUNTRY = {"query": "{countries(filter: {code: {in: \"ID\"}}) {code name native emoji}}"}
    FILTER_CONTINENTS = {"query": "{continents(filter: {code: {in: \"OC\"}}) {code name countries {name capital}}}"}


class GraphQLMutation:
    API_URL = "http://localhost:4000/"
    HEADERS = {'Content-Type': 'application/json'}
    DATA_CREATE_USER = "{\"query\":\"mutation {createUser(id: 4, name: \\\"Robert\\\", email: \\\"robert@gmail.com\\\", age: 21) {id name email age}}\"}"
    DATA_DELETE_USER = "{\"query\":\"mutation {deleteUser(id: 4) {id name email age}}\"}"
    DATA_UPDATE_USER = "{\"query\":\"mutation {updateUser(id: 4, name: \\\"Gregor\\\", email: \\\"gregor@gmail.com\\\", age: 27) {id name email age}}\"}"
