#budget app backend api endpoints guide

## All api endpoints

Go to this link /api/account/apilist/ 

to see all available endpoints

## Authentication
For authentication Django rest framework simple jwt is being used. The following are the
various endpoints under authentication

###Registration
api endpoint = /api/account/register/

data required;

* name = full name of user
* username = username of user
* email = email of user
* password = password of user (must be >= 8 chars)
* re_password = repeat user password 


### Login
To login you have to first retrieve user access and refresh tokens
by going to this api endpoint with a post request

api endpoint = /api/token/

data required;

* username 
* password

on passing the above data to the api endpoint if the data is valid for
a registered user you will get back two tokens

* access token
* refresh token

The access and refresh tokens should be stored with either local storage or http only cookie
 the access token expires after 30 mins. To get a new access tokens you have to send the refresh token to the
token verify endpoint below;

api endpoint: /api/token/verify/

The access tokens should be added as Authorization header when making post request to
protected pages (all other available api endpoints are protected and can only be accessed with
requests that contains valid Authorization header access tokens).