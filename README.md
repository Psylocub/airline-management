# Airlines management project

## Local setup

**Create python environment & install dependencies**

```
$ make setup
```

**Activate python environment**

```
$ source .venv/bin/activate
```

**Setup .ENV file**
```
$ Rename .ENV.EXAPMLE to .ENV and fill all data
```

**Run database container**

```
$ make up_db
```

**Add migrations to database**

```
$ make init_db
```

**Create user**
```
./src/manage.py createsuperuser
```

**Run application**

```
$ make run
```

## API documentation

* Swagger web UI: [api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
* Swagger JSON: [api/schema/swagger.json](http://127.0.0.1:8000/api/schema/swagger.json) 
* Redoc: [api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/) 
* Flights & in-flight time: [api/v1/flights/?sorted](http://127.0.0.1:8000/api/v1/flights/?sorted)