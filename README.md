# flask_couchbase

Couchbase Flask Extension


## Configuration

| Parameter                   | Description |
|-----------------------------| ----------------------------- |
| `COUCHBASE_CONNECTION`      | Bucket connection string, like `'couchbases:///my_bucket` or `'couchbases://10.3.4.33/my_secret_bucket?certpath=/var/cbcert.pem'` |
| `COUCHBASE_PASSWORD`        | Bucket password if any |
| `COUCHBASE_CONNECT_OPTIONS` | Extra options for the connection separated by `&`, like `'operation_timeout=4&http_poolsize=0'` |
