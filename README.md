evo
===

Python evostream client

Sample usage:

    >>> from evo import Evo
    >>> e = Evo("127.0.0.1")
    >>> e.listStreams()
    {u'status': u'SUCCESS', u'data': None, u'description': u'Available streams'}
    >>> e.createhlsstream(localstreamnames='video300,video400,video500', targetfolder='/tmp/evo', groupname='video', playlisttype='rolling')
    {u'status': u'SUCCESS', u'data': {u'AESKeyCount': 5, u'staleRetentionCount': 10, u'chunkLength': 10, u'encryptStream': False, u'playlistType': u'rolling', u'groupName': u'video', u'bandwidths': [0, 0, 0], u'configIds': [13, 14, 15], u'localStreamNames': [u'video300', u'video400', u'video500'], u'chunkBaseName': u'segment', u'playlistLength': 10, u'createMasterPlaylist': True, u'playlistName': u'playlist.m3u8', u'cleanupDestination': False, u'overwriteDestination': True, u'targetFolder': u'/tmp/evo', u'chunkOnIDR': True, u'keepAlive': True}, u'description': u'HLS stream created'}

