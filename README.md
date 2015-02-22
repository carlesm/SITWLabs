# Sistemes i Tecnologies Web - Labs #


This repo keeps some Labs for SITW. Should be checked out step by step
to follow the labs.

### Repo structure ###

* Basic Web
    Basic Web client access (before HTTP REST). No JSON, no XML.

    Before:
        Must have bitnami-django stack
        Must have developer toolbar (firefox or chrome)

    Order:

        clientweb.py
            web client
            urllib2, beautifulsoup4
            Empty client -> web client -> parse -> print

        getweather.py
            wundergroud client
            urllib2
            must get developer key (first argument)
            http://www.wunderground.com/weather/api/
            First draft (still no XML/JSON) using beatifulsoup4




