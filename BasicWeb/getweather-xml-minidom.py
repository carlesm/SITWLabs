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
from xml.dom import minidom

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

    def getNodeText(self, node):
        """
        Returns the text "hanging" from a XML node
        """
        nodelist = node.childNodes
        result = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                result.append(node.data)
        return ''.join(result)

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

        doc = minidom.parseString(r.text)

        temp_high = doc.getElementsByTagName("temp_high")[0]
        th_normal = temp_high.getElementsByTagName("normal")[0]
        thnc = self.getNodeText(
            th_normal.getElementsByTagName("C")[0])
        th_record = temp_high.getElementsByTagName("record")[0]
        thrc = self.getNodeText(th_record.getElementsByTagName("C")[0])
        thry = self.getNodeText(
            temp_high.getElementsByTagName("recordyear")[0])

        return_response["high"] = {}
        return_response["high"]["normal"] = thnc
        return_response["high"]["record"] = thrc
        return_response["high"]["year"] = thry

        temp_low = doc.getElementsByTagName("temp_low")[0]
        tl_normal = temp_low.getElementsByTagName("normal")[0]
        tlnc = self.getNodeText(tl_normal.getElementsByTagName("C")[0])
        tl_record = temp_low.getElementsByTagName("record")[0]
        tlrc = self.getNodeText(tl_record.getElementsByTagName("C")[0])
        tlry = self.getNodeText(temp_low.getElementsByTagName("recordyear")[0])
        return_response["low"] = {}
        return_response["low"]["normal"] = tlnc
        return_response["low"]["record"] = tlrc
        return_response["low"]["year"] = tlry

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
