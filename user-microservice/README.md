# USER AND AUTH MICROSERVICE
<hr>

## INSTALLATION

### Clone repository use

```bash
git clone https://github.com/Microservices-BECL-UFPS/user-microservice.git
```

#### Change directory and Activate Environment
```bash
cd user-microservice
```

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

#### Install requirements.txt
```bash
pip install -r requirements.txt
```

## VARIABLES ENVIRONMENTS 

#### Create file '.env' with:
* CLIENTE_ID=ID_CLIENT_GOOGLE_API
* SECRET=SECRET_CLIENT_GOOGLE_API
* SECRET_KEY=DJANGO_SECRET_KEY 

#### Read the file `external_database_import.sql` and execute it in the postgresql database

## LOCAL DATABASE MIGRATIONS
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## RUN CONFIG GROUPS AND PERMISSIONS
```bash
python manage.py config_groups create
```

## RUN SERVER
```bash
python manage.py runserver
```

# ENDPOINTS

## AUTH APP

|ACTION|METHOD|SUFIX|REQUEST_BODY|RESPONSE_BODY|
|------|------|----|------|------|
|SIGN IN/UP|POST|/auth/api/v1/sign_in_up/|[Here](#request-body-sign-in-and-sign-up)|[Here](#response-body-sign-in-and-sign-up)
|REFRESH TOKEN|POST|/auth/api/v1/token/refresh/|[Here](#request-body-refresh-token)|[Here](#response-body-refresh-token)|
|VERIFY TOKEN|POST|/auth/api/v1/token/verify/|[Here](#request-body-verify-token)|[Here](#response-body-verify-token)|

#### SIGN IN/UP Request and Response
##### Request body sign in and sign up:
```json
{
    "token": "google_token_id"
}
```

##### Response body sign in and sign up:
```json
{
    "access": "access_token",
    "refresh": "refresh_token",
}
```
#### Refresh token Request and Response
##### Request body refresh token:
```json
{
    "refresh": "refresh_token"
}
```

##### Response body refresh token:
```json
{
    "access": "access_token",
    "refresh": "refresh_token",
}
```

#### Verify token Request and Response
##### Request body verify token:
```json
{
    "token": "access_token"
}
```

##### Response body verify token:
```json
{}
Status 200 Ok
```

### Note:
The google_token_id is the token that is returned by the google api consumed by frontend.
For test please clone this repository and run with this fast config because our frontend is too slow:

```bash
git clone https://github.com/Sivanesh-S/react-google-authentication.git
```
```bash
cd react-google-authentication
```

### In the following files edit the following variables:
```bash
react-google-authentication/
├── src/
    ├── components/
        ├── Login.js
        ├── LoginHook.js
        ├── Logout.js
        ├── LogoutHook.js
```

```javascript
const clientId = "CLIENT_ID_GOOGLE_API";
```

<strong>to</strong>

```javascript
const clientId = "YOUR_CLIENT_ID_GOOGLE_API";
```

### In the following files edit the following code lines(line 14 in both files):
```bash
react-google-authentication/
├── src/
    ├── components/
        ├── Login.js
        ├── LoginHook.js
```


```javascript
`Logged in successfully welcome ${res.profileObj.name} 😍. \n See console for full profile object.`
```

<strong>to</strong>

```javascript
`Google token id: ${res.tokenId}`
```

### And finally install the libraries and run the project with the following commands:

```bash
npm install
```
```bash
npm start
```
Note: To get the google token you have to log in to the react application and with the previous configuration you will get an "alert" with the google token.

## USER APP

|ACTION|METHOD|SUFIX|REQUEST_BODY|RESPONSE_BODY|DOCUMENTATION|
|------|------|----|------|------|------|
|GET USERS|GET|/user/api/v1/users/|N/A|[Here](#response-body)||
|FIND USER|GET|/user/api/v1/users/{id}/|N/A|[Here](#response-body)||
|UPDATE USER|PUT|/user/api/v1/users/{id}/|[Here](#request-body)|[Here](#response-body)||
|DELETE USER|DELETE|/user/api/v1/users/{id}/|N/A|[Here](#response-body)||
|CREATE USER|POST|/user/api/v1/users/|[Here](#request-body)|[Here](#response-body)||
|PROFILE USER|GET|/user/api/v1/profile/|N/A|[Here](#response-user-profile)|OK|
|------|------|----|------|------|------|
|GET GROUPS|GET|/user/api/v1/groups/|N/A|[Here](#response-body)||
|FIND GROUP|GET|/user/api/v1/groups/{id}/|N/A|[Here](#response-body)||
|UPDATE GROUP|PUT|/user/api/v1/groups/{id}/|[Here](#request-body)|[Here](#response-body)||
|DELETE GROUP|DELETE|/user/api/v1/groups/{id}/|N/A|[Here](#response-body)||
|CREATE GROUP|POST|/user/api/v1/groups/|[Here](#request-body)|[Here](#response-body)||
|UPDATE USER GROUP|PUT|/user/api/v1/update_groups/|[Here](#request-user-update-groups)|[Here](#response-user-update-groups)|OK|
|------|------|----|------|------|------|
|LIST PERMISSIONS|GET|/user/api/v1/permissions/|N/A|[Here](#response-list-permissions)|OK|
|UPDATE USER PERMISSIONS|PUT|/user/api/v1/update_permissions/|[Here](#request-user-update-permissions)|[Here](#response-user-update-permissions)|OK|

#### User Profile
##### Response user profile:
```json
{
    "id": 69,
    "username": "",
    "first_name": "some_first_name",
    "last_name": "some_last_name",
    "email": "some_email@ufps.edu.co",
    "is_active": true,
    "picture": "URL_FIELD",
    "program": {
        "id": 96,
        "name": "some_program_name"
    },
    "groups": [
        {
            "id": 69,
            "name": "some_group_name",
            "permissions": [
                {
                    "id": 96,
                    "name": "some_permission_name",
                    "codename": "some_permission_codename",
                    "content_type": 69
                }
            ]
        }
    ],
    "user_permissions": [
        {
            "id": 96,
            "name": "some_permission_name",
            "codename": "some_permission_codename",
            "content_type": 69
        }
    ]
}
```

#### User Update Groups
##### Request user update groups:
```json
{
    "user_id": 69,
    "groups": [96, 69]
}
```
Note: user_id is the id of the user whose groups are to be updated, and groups is a list of ids corresponding to each group.

##### Response user update groups:
```json
{}
Status 200 Ok
```

#### List Permissions
##### Response list permissions:
```json
[
    {
        "id": 96,
        "name": "some_permission_name",
        "codename": "some_permission_codename",
        "content_type": 69
    }
]
```

#### Update User Permissions
##### Request user update permissions:
```json
{
    "user_id": 69,
    "user_permissions": [96, 69]
}
```
Note: user_id is the id of the user whose permissions are to be updated, and user_permissions is a list of ids corresponding to each permission.

##### Response user update permissions:
```json
{}
Status 200 Ok
```