# codeunion-back
Test task 

### Seed

#### For development:
``` $ docker-compose up --b```

### Run tests:
In separate tab

``` $ docker-compose exec django bash ``` - get into django container

``` $ $test ``` - run all tests

``` $ $flake8 ``` - run lint

### Run CLI command:

``` $ docker-compose exec django bash ``` - get into django container

``` $ python manage.py update_or_view_currency_rate --update --currency_id <currency_id> --value <new_value> ```

For example

``` $ python manage.py update_or_view_currency_rate --update --currency_id 1 --value 1.1 ```

### Postman collection and env:

[codeunion.postman_collection.json](https://github.com/Alisher2299/codeunion-back/files/13259217/codeunion.postman_collection.json)

[local codeunion.postman_environment.json](https://github.com/Alisher2299/codeunion-back/files/13259220/local.codeunion.postman_environment.json)
