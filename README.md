# Payload generator

Simply creates a random JSON, logs it and POSTs it to a configurable endpoint.

## Environment variables

- `POST_ENDPOINT`: where you want the data posted to. Defaults to `'http://127.0.0.1:8080'`

## Why is this repo here?

I needed something stupid to generate some sort of random payload as JSON and post it somewhere
(in kafka and fluentd actually, to compare the performance of their HTTP input plugins).

So I've just created a basic docker image so that I could deploy it to various docker swarms and scale them.

But to my surprise it's been downloaded a lot in a few days,
so I though I would just give more clarity and instructions if people want to use it too...
