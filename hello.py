#!/usr/bin/python
# -*- coding: utf-8 -*-

from cgi import escape,parse_qs
__author__ = "runnerpeople"


def myapp(environ,start_response):
    output = ["<p> WSGI script by George Ivanov </p>",
              "<form method='POST'>",
              "<p><input type='text' name='str'></p>",
              "<p><input type='submit' value='Send!'></p>",
              "</form>"]
    response_headers = [('Content-type','text/html')]
    if environ['REQUEST_METHOD'] == "GET":
        dict_value = parse_qs(environ['QUERY_STRING'])
        output.append("<h3> <p> Get data: </p> </h3>")
        if dict_value:
            output.append("No data received")
        for key,value in dict_value.iteritems():
            if len(value) == 1:
                output.append("%s = %s <br>" % (key, value[0]))
            else:
                output.append("%s = %s <br>" % (key, value))
    else:
        try:
            size = int(environ.get('CONTENT_LENGTH', 0))
        except:
            size = 0
        request=environ['wsgi.input'].read(size)
        dict_value = parse_qs(request)
        output.append("<h3> <p> Post data: </p> </h3>")
        output.append("Value = %s <br>" % (dict_value['str'][0]))
    response_headers.append(('Content-length',str(sum([len(x) for x in output]))))
    start_response('200 OK',response_headers)
    return output


