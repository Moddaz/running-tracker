# API Calls

## Important
+ time interval (`startTimeMillis` and `endTimeMillis`) has to be in nano secoconds (mili * 1000)
+ Access for API ``https://www.googleapis.com/auth/fitness.location.read`` has to be granted
<br/> ![apis](https://i.imgur.com/hdd4Bs4.png "apis")

## Examples

### Kilometers
provides kilometers from 29.07 - 01.08.

#### Request
+ HTTP Method: ``POST``
+ Request URI: ``https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate``
````
{
  "aggregateBy": [{
    "dataTypeName": "com.google.step_count.delta",
    "dataSourceId": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta"
  }],
  
  "bucketByTime": { "durationMillis": 86400000}, //interval: day / 24h
  "startTimeMillis": 1564272000000,
  "endTimeMillis": 1564704000000
}
````

#### Response
````
HTTP/1.1 200 OK
Content-length: 2465
X-xss-protection: 1; mode=block
X-content-type-options: nosniff
Transfer-encoding: chunked
Expires: Mon, 01 Jan 1990 00:00:00 GMT
Vary: Origin, X-Origin
Server: GSE
Etag: "mqZ8nz1T_Dl4ssxi55wNSn8e1S8/TzgpLyspm7W0ppjHrCBVzPizEgI"
Pragma: no-cache
Cache-control: no-cache, no-store, max-age=0, must-revalidate
Date: Thu, 01 Aug 2019 21:51:17 GMT
X-frame-options: SAMEORIGIN
Alt-svc: quic=":443"; ma=2592000; v="46,43,39"
Content-type: application/json; charset=UTF-8
-content-encoding: gzip
{
  "bucket": [
    {
      "startTimeMillis": "1564272000000", 
      "endTimeMillis": "1564358400000", 
      "dataset": [
        {
          "dataSourceId": "derived:com.google.distance.delta:com.google.android.gms:aggregated", 
          "point": [
            {
              "startTimeNanos": "1564300767715000000", 
              "originDataSourceId": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta", 
              "endTimeNanos": "1564341491077434517", 
              "value": [
                {
                  "mapVal": [], 
                  "fpVal": 8061.5830417871475
                }
              ], 
              "dataTypeName": "com.google.distance.delta"
            }
          ]
        }
      ]
    }, 
    {
      "startTimeMillis": "1564358400000", 
      "endTimeMillis": "1564444800000", 
      "dataset": [
        {
          "dataSourceId": "derived:com.google.distance.delta:com.google.android.gms:aggregated", 
          "point": [
            {
              "startTimeNanos": "1564397527064056779", 
              "originDataSourceId": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta", 
              "endTimeNanos": "1564435477860856704", 
              "value": [
                {
                  "mapVal": [], 
                  "fpVal": 7847.701479434967
                }
              ], 
              "dataTypeName": "com.google.distance.delta"
            }
          ]
        }
      ]
    }, 
    {
      "startTimeMillis": "1564444800000", 
      "endTimeMillis": "1564531200000", 
      "dataset": [
        {
          "dataSourceId": "derived:com.google.distance.delta:com.google.android.gms:aggregated", 
          "point": [
            {
              "startTimeNanos": "1564461946945000000", 
              "originDataSourceId": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta", 
              "endTimeNanos": "1564513241426000000", 
              "value": [
                {
                  "mapVal": [], 
                  "fpVal": 7186.627092421055
                }
              ], 
              "dataTypeName": "com.google.distance.delta"
            }
          ]
        }
      ]
    }, 
    {
      "startTimeMillis": "1564531200000", 
      "endTimeMillis": "1564617600000", 
      "dataset": [
        {
          "dataSourceId": "derived:com.google.distance.delta:com.google.android.gms:aggregated", 
          "point": [
            {
              "startTimeNanos": "1564556743729259785", 
              "originDataSourceId": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta", 
              "endTimeNanos": "1564615102446819846", 
              "value": [
                {
                  "mapVal": [], 
                  "fpVal": 1428.5482759475708
                }
              ], 
              "dataTypeName": "com.google.distance.delta"
            }
          ]
        }
      ]
    }
  ]
}
````