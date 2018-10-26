import json
import datetime



def wsgi_application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    url = "".join([environ["HTTP_HOST"], environ["RAW_URI"]])
    test = json.dumps({"time": str(datetime.datetime.now().time()),
                       "url": url})
    test1 = test.encode('utf-8')
    return [test1]
