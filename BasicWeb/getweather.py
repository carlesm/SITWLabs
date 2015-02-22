#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get weather from weather underground
Created on 11/22/2014

@author: carlesm
'''

import sys

api_key = None  # If assigned won't read argv[1]

location = 'Lleida'
response_format = 'xml'


class WeatherClient(object):

    """Will access wunderground to gather weather information

    Provides access to wunderground API
    (http://www.wunderground.com/weather/api)

    Provides methods:
        almanac
    """

    url_base = 'http://api.wunderground.com/api/'
    url_services = {
        "almanac": "/almanac/q/CA/"
    }

    def __init__(self, apikey):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def almanac(self, location, resp_format = "xml"):
        """
        Accesses wunderground almanac information for the given location
        """
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_services["almanac"]+location+"."+resp_format
        print url


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Must provide api key in code or cmdline arg"

    weatherclient = WeatherClient(api_key)
    weatherclient.almanac("Lleida")
