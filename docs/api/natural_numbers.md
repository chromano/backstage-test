# Purpose

Provides an endpoint allows requests for calculating the difference between:
     1. the sum of the squares of the first n natural numbers and
     1. the square of the sum of the same first n natural numbers, where n is
guaranteed to be no greater than 100.

Example:

The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.


## Usage

The only required parameter is `n`, which should be provide as part of
the URL via a GET request.

Example:

```bash
curl -X GET http://127.0.0.1:8000/api/v1/calc/natural_numbers/?n=10
```

**Request**:

`GET` `calc/natural_numbers`

Parameters:

Name | Type | Description
---|---|---
n  | int | A number no greater than 100

**Response**:

```json
Content-Type application/json
201 Created

{
"datetime": "2012-04-23T18:25:43.511z",
"value": 2640,
"number": 10,
"occurrences": 1
}
```
