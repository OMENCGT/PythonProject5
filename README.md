# Setup:  
1. clone this repo
2. exec in terminal "python -m venv venv" at project dir
3. exec in terminal "pip install django djangorestframework django-filter"
4. exec in terminal "python manage.py runserver"

then you will be able to make requests to localhost:8000/api/...
# Models:

### BOOK:
| field_name | type                      |
| :--------- | :---                      |
| title      | CharField, max_length=200 |
| author     | Foreign_key Author        |
| isbn       | CharField, max_lentgh=13, unique |
| published_date | DateField             |
| genre      | CharField, max_length=20, choices=GC |
| description | TextField                |
| page_count | IntegerField, default=0   |
| created_at | DateTimeField, auto       |
| updated_at | DateTimeField, auto       |
#### NOTE: auto means you don't need to make this fields 

### AUTHOR:
| field_name | type                       |
| :--------- | :------------------------- |
| name       | CharField, max_length=100  |
| birth_date | CharField, null=1, blank=1 |
| bio        | TextField, blank=1         |
| created_at | same as field in book      |
| updated_at | same as field in book      |

#### NOTE: There is also auto-created field id in both tables.

# End-points:

| №   | Request method | URL            | For what            | Request body | Response status (if ok) | Response content |
| :-: | :------------- | :------------- | :------------------ | :----------- | :---------------------- | :--------------- |
| 1   | GET            | /api/book      | get list of books   | void         | 200                     | list of json     |
| 2   | POST           | /api/book      | add new book        | json according to model Book | 200     | json with added book |
| 3   | PATCH          | /api/book/{id} | edit existing book by id | json with some fields of Book | 200    | json with edited book |
| 4   | DELETE         | /api/book/{id} | delete existing book by id | void  |  202                    | json with deleted book |

**Note: There are same End-points for author, but DELETE chain deleting books with this author**  

