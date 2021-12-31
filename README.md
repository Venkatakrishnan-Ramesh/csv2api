### Documentation

CSV2API is the simplest backend you can integrate with your application, so easy that, now you can save the time and money needed by a backend developer.

**Accepted Parameters:**
- **url**: The URL pointing to the raw CSV file (shareable link of CSV file is not accepted). **REQUIRED**
- **query**: pass your query here and get specific data. **OPTIONAL**

**Keep in mind:**
- query parameters are case sensitive
- String should be of the form `'string'` and `string` is not considered as a string.
- Supports boolean and need not be under a string, `'True'` is wrong, `True` is correct. Booleans are case sensitive, `False` is a bool, `false` is a string
