evo
===

Python evostream client

Sample usage:

    >>> from evo import Evo
    >>> e = Evo("127.0.0.1")
    >>> e.listStreams()
    {u'status': u'SUCCESS', u'data': None, u'description': u'Available streams'}
