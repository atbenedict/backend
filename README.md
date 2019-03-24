#Back-End-Architect

## Andrew Benedict

### Live Backend URL: https://dbase.wtf

229,661 US Gun Violence Incidents between Jan 1, 2013 and Mar 31, 2018

### **Register a user**

_method url_: `/api/user/register`

_http method_: **[POST]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

| name       | type   | required | description    |
| ---------- | ------ | -------- | -------------- |
| `username` | String | Yes      | Must be unique |
| `password` | String | Yes      |                |
| `email`    | String | No       | Must be unique |

#### Example

```
  {
    "username": "frodo",
    "password": "pass",
    "email": "f_bag@gmail.com",
  }
```

#### Response

##### 201 (created)

###### Example Response

```
  [
    2
  ]
```

##### 400 (Bad Request)

```
  {
    "errorMessage": "missing ${itemMissing}"
  }
```

### **Login a user**

_method url_: `/api/user/login`

_http method_: **[POST]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

| name       | type   | required | description             |
| ---------- | ------ | -------- | ----------------------- |
| `username` | String | Yes      | must be registered user |
| `password` | String | Yes      |                         |

#### Example

```
  {
    "username": "frodo",
    "password": "pass",
  }
```

#### Response

##### 200 (ok)

> no issues logging in

###### Example response

```
{
    "id": 2,
    "username": "frodo",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNTUyMzQ1ODQxLCJleHAiOjE1ODM5MDM0NDF9.3vQ4kTKKJBHGMbOVTLGSKP7HKNd3fR7aBCwu45T4JCI"
}
```

##### 400 (Bad Request)

```
  {
    errorMessage: 'missing ${itemMissing}'
  }
```

##### 401 (Unauthorized)

```
{
  errorMessage: "passwords don't match"
}
```

### **get a single event**

_method url_: `/api/gundata/:id`

_http method_: **[GET]**

#### Response

##### 200 (ok)

###### Example response

```
{
    "incident_id": 478855,
    "date": "2013-01-01",
    "state": "Ohio",
    "city_or_county": "Lorain",
    "address": "1776 East 28th Street",
    "n_killed": 1,
    "n_injured": 3,
    "incident_url": "http://www.gunviolencearchive.org/incident/478855",
    "gun_stolen": "0::Unknown||1::Unknown",
    "gun_type": "0::Unknown||1::Unknown",
    "incident_characteristics": "Shot - Wounded/Injured||Shot - Dead (murder, accidental, suicide)||Shots Fired - No Injuries||Bar/club incident - in or around establishment",
    "latitude": 41.4455,
    "longitude": -82.1377,
    "n_guns_involved": "2.0",
    "participant_age": "0::25||1::31||2::33||3::34||4::33",
    "participant_age_group": "0::Adult 18+||1::Adult 18+||2::Adult 18+||3::Adult 18+||4::Adult 18+",
    "participant_gender": "0::Male||1::Male||2::Male||3::Male||4::Male",
    "participant_name": "0::Damien Bell||1::Desmen Noble||2::Herman Seagers||3::Ladd Tate Sr||4::Tallis Moore",
    "participant_relationship": "",
    "participant_status": "0::Injured, Unharmed, Arrested||1::Unharmed, Arrested||2::Killed||3::Injured||4::Injured",
    "participant_type": "0::Subject-Suspect||1::Subject-Suspect||2::Victim||3::Victim||4::Victim",
    "participant_info": "{'0': {'age': '25', 'age_group': 'Adult 18+', 'gender': 'Male', 'name': 'Damien Bell', 'status': 'Injured, Unharmed, Arrested', 'type': 'Subject-Suspect'}, '1': {'age': '31', 'age_group': 'Adult 18+', 'gender': 'Male', 'name': 'Desmen Noble', 'status': 'Unharmed, Arrested', 'type': 'Subject-Suspect'}, '2': {'age': '33', 'age_group': 'Adult 18+', 'gender': 'Male', 'name': 'Herman Seagers', 'status': 'Killed', 'type': 'Victim'}, '3': {'age': '34', 'age_group': 'Adult 18+', 'gender': 'Male', 'name': 'Ladd Tate Sr', 'status': 'Injured', 'type': 'Victim'}, '4': {'age': '33', 'age_group': 'Adult 18+', 'gender': 'Male', 'name': 'Tallis Moore', 'status': 'Injured', 'type': 'Victim'}}",
    "year": 2013,
    "month": 1,
    "day_of_month": 1,
    "day_of_week": 1,
    "incident_type": "Suicide"
}
```
