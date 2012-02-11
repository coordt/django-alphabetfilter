"""
Django-AlphaFilter provides an admin widget for alphabetical filtering that 
works like date_hierarchy and an template tag for use elsewhere.
"""

__version_info__ = {
    'major': 0,
    'minor': 5,
    'micro': 4,
    'releaselevel': 'final',
    'serial': 0
}

def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
