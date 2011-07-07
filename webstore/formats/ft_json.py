try:
    from json import dumps, loads
except ImportError:
    from simplejson import dumps, loads

from flask import Response, g

def json_request(request):
    json = loads(request.data)
    if not isinstance(json, (list, tuple)):
        yield json
    else:
        for row in json:
            yield row


def _generator(table, callback):
    yield callback + '([' if callback else '['
    iter = table.__iter__()
    has_next, first = True, True
    while has_next:
        try:
            row = iter.next()
        except StopIteration:
            has_next = False
        if has_next:
            if not first: 
                yield ', '
            yield dumps(row)
        first = False
    yield '])' if callback else ']'

def json_table(table, keys):
    callback = str(g.callback) if g.callback else None
    return Response(_generator(table, callback), mimetype='application/json',
                    direct_passthrough=True)

def json_message(message, state='error', url=None, code=200):
    obj = {'message': message, 'state': state}
    if url is not None:
        obj['url'] = url
    response = Response(dumps(obj), status=code, 
                        mimetype='application/json')
    if url is not None:
        response.headers['Location'] = url
    return response



