## How to run and serve the application 

Use the package manager pipenv to create the virtual env

Make sure that you are in the root folder (ls command will return - app,tests, Pipfile, Pipfile.lock, README.md, run.py)

```bash
#Creates virtual env
pipenv shell

#Install all required dependencies
pipenv install

#Run the application 
flask run 

#You will see smth like that
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## How to use the application 

### User registration and login API
Firstly you should register the user (I know that you said that API shoudn't have the authorization, but if I will have it it will be bonus points :)))) )<br>
You can make this with /user/create POST endpoint: <br>
Request:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"username":"some_username",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"password": "123"<br>
}<br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"x-access-token": "your_access_token"<br>
}<br>

You can use that access token to autenticate all your API requests with {"Authorization" : "Bearer <your_token>"} header. <br>

Also to login you can use the /user/login POST endpoint: <br>

Request:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"username":"some_username",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"password": "123"<br>
}<br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"x-access-token": "your_access_token"<br>
}<br>
### Product API
To create the product you can use the /product/create POST endpoint: <br>
Request:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name":"some_name",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "some_description"<br>
}<br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": 1,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "some_name,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "some_description",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"offers": []<br>
}<br>

To get the singe product you can use the /product/<product_id>  GET endpoint: <br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": <product_id> ,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "some_name,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "some_description",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"offers": []<br>
}<br>

To update the product you can use the /product/<product_id> PUT  endpoint: <br>
Request:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name":"new_name",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "new_description"<br>
}<br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": <product_id>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "new_name,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "new_description",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"offers": []<br>
}<br>

To delete the product you can use the /product/<product_id> DELETE  endpoint: <br>

Response:<br>

204 Status code <br>

To get all offers for certain product you can use the /product/get_all_offers/<product_id> GET  endpoint: <br>

Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"offers": []<br>
}<br>

## How to run tests

Make sure that you are in the root directory, and run 

```bash
pytest
```