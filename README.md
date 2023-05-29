# Flask-API
###  API that provides a basic authentication


The first endpoint receives a username and password. When these parameters are correct it returns a JWT token; otherwise it should return a 403 HTTP error message.

```
curl -d "username=admin&password=secret" http://localhost:8000/login
{
  "data": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```
<br />

For the second endpoint you must use the generated token to access a restricted area:
```
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" localhost:8000/protected
{
  "data": "You are under protected data"
}
```
<br />



###  A container was create in other to deploy the API
