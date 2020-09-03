# Asynchronous music recommender

This project is a web service that suggests musics based on user's Favorited music. About 30000 song data with artist and their 12 specific properties has been gathered from spotify-api, to employed for machine learning part. The whole web service is build with docker container, Flask is the main web frame work and PostgreSQL is the database. Also, ML tasks are bind with celery, rabbitmq and redis for the purpose of better performance, monitoring and asynchronous.

## Installation

To create and run it

```bash
docker-compose up --build -d
```
To stop all containers:

```bash
docker-compose down -v
```


## Usage

The main api for recommendation

```bash
http://0.0.0.0:8000/recommend/hey you/pink floyd/10
```
this api has GET method and return 10 music similar to Hey You by Pink Floyd.

Also for getting All the searched music for recommendation:
```bash
http://0.0.0.0:8000
```
to see admin panel:
```bash
http://0.0.0.0:8000/admin
```
## Result
Let'shave little fun, I want similart music:
```bash
http://0.0.0.0:8000/recommend/sexual eruption/snoop dogg/4
```
and results are:
```js
{"for":"music: sexual eruption, artist: snoop dogg","ip_address":"192.168.128.1","musics":
[{"1":{"artist":"boys noize","song":"oh! (a-trak remix)","spotify_url":
"https://open.spotify.com/track/5fai3huhzsk4foq7s3g5ll"}},
{"2":{"artist":"paris hilton","song":"nothing in this world","spotify_url":
"https://open.spotify.com/track/4xrgwyaarl21fesc6bvlif"}},
{"3":{"artist":"bonde do rol\u00ea","song":"james bonde","spotify_url":
"https://open.spotify.com/track/1f6goknk0i9m3pq1kancaf"}},
{"4":{"artist":"the valentinos","song":"kafka (bag raiders remix)","spotify_url":
"https://open.spotify.com/track/0oclk8vnbtefvxxcb7tspw"}}],"status":200}
```
which the results are not that bad, but by working more on the similarity function: This could be better.

## Tech
ML: Pandas, Celery, rmq, redis

Web: flask, postgre, nginx, gunicorn

Build: docker, docker-compose

## Medium
### [part1](https://medium.com/@sdamoosavi/music-recommender-web-service-ml-ef6fdd1fc026)
### [part2](https://medium.com/@sdamoosavi/music-recommender-web-service-flask-and-celery-a1274b488ab)
