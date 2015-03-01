#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get weather from weather underground
Created on 11/22/2014

Using XML as format, minidom

@author: carlesm
'''

import sys
import requests
import xmltodict

api_key = None  # If assigned won't read argv[1]



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
        self.api_key = apikey


    def almanac(self, location):
        """
        Accesses wunderground almanac information for the given location
        """
        resp_format = "xml"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_services[
                "almanac"] + location + "." + resp_format
        r = requests.get(url)

        return_response = {}

        xml = xmltodict.parse(r.text)

        return_response["high"] = {}
        return_response["high"]["normal"] = \
            xml['response']['almanac']['temp_high']['normal']['C']
        return_response["high"]["record"] = \
            xml['response']['almanac']['temp_high']['record']['C']

        return_response["high"]["year"] = \
            xml['response']['almanac']['temp_high']['recordyear']

        return_response["low"] = {}
        return_response["low"]["normal"] = \
            xml['response']['almanac']['temp_low']['normal']['C']
        return_response["low"]["record"] = \
            xml['response']['almanac']['temp_low']['record']['C']
        return_response["low"]["year"] = \
            xml['response']['almanac']['temp_low']['recordyear']

        return return_response


def print_almanac(almanac):
    """
    Prints an almanac received as a dict
    """
    print "High Temperatures:"
    print "Average on this date", almanac["high"]["normal"]
    print "Record on this date %s (%s) " % \
        (almanac["high"]["record"],
            almanac["high"]["year"])
    print "Low Temperatures:"
    print "Average on this date", almanac["low"]["normal"]
    print "Record on this date %s (%s) " % \
        (almanac["low"]["record"],
            almanac["low"]["year"])


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Must provide api key in code or cmdline arg"

    weatherclient = WeatherClient(api_key)
    print_almanac(weatherclient.almanac("San_Francisco"))
