[codeunion.postman_collection.json](https://github.com/Alisher2299/codeunion-back/files/13259190/codeunion.postman_collection.json)# codeunion-back
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

[Uploading codeunion.postm{
	"info": {
		"_postman_id": "7bf1701f-66e9-4699-a2bd-dab8d89dc350",
		"name": "codeunion",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "16303083"
	},
	"item": [
		{
			"name": "Login",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"var res = pm.response.json();",
							"pm.environment.set('access_token', res.access);",
							"pm.environment.set('refresh_token', res.refresh);"
						],
						"type": "text/javascript"
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"email\": \"admin@mail.com\",\n    \"password\": \"admin\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "{{host}}/v0/api/users/login/",
					"host": [
						"{{host}}"
					],
					"path": [
						"v0",
						"api",
						"users",
						"login",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Signup",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"var res = pm.response.json();",
							"pm.environment.set('access_token', res.access);",
							"pm.environment.set('refresh_token', res.refresh);"
						],
						"type": "text/javascript"
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"email\": \"alisher.zhanayev.99@gmail.com\",\n    \"password\": \"adminadmin1\",\n    \"confirm_password\": \"adminadmin1\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "{{host}}/v0/api/users/signup/",
					"host": [
						"{{host}}"
					],
					"path": [
						"v0",
						"api",
						"users",
						"signup",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Get currency by id",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "Get currencies list",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "{{access_token}}",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "{{host}}/v0/api/currencies?page=5&per_page=7",
					"host": [
						"{{host}}"
					],
					"path": [
						"v0",
						"api",
						"currencies"
					],
					"query": [
						{
							"key": "page",
							"value": "5"
						},
						{
							"key": "per_page",
							"value": "7"
						}
					]
				}
			},
			"response": []
		}
	]
}an_collection.json…]()
