import re

# REGEX ----------------------------------------------------------------------- 
#
# The supreme regex, courtesy of Diego Perini.
# 
# This attempts to factor in unicode characters as well as ASCII.
# A nice article on the tests run on the regex can be found here:
#
# http://mathiasbynens.be/demo/url-regex
#
# The regex conforms to RFC 3986 (with unicode!) which can be read here:
# http://www.ietf.org/rfc/rfc3986.txt
#
# In which a path is defined as scheme://netloc/path;parameters?query#fragment
# in a varying number of subsections.  For this regex, however, the matching
# URLs will be limited to http(s) and ftp
#
# One fatal flaw in this URL validator, however, is that the parameters at the
# end of the URL are not validated.  This could be an issue if a bunch of
# invalid syntax was entered, for example:
#
#   http://foo.bar.com/#?&?&?&?&=2?
#
# This would likely be invalid on any server, but it is not checked in this
# regex.
__regex = u"^\
(\
    ?P<protocol>(\
        ?P<scheme>https?|ftp\
    )://\
)(\
    ?:\S+(\
        ?::\S*\
    )?@\
)?(\
    ?P<authority>(\
        ?!10(\
                ?:\.\d{1,3}\
        ){3}\
    )(\
        ?!127(\
            ?:\.\d{1,3}\
        ){3}\
    )(\
        ?!169\.254(\
            ?:\.\d{1,3}\
        ){2}\
    )(\
        ?!192\.168(\
            ?:\.\d{1,3}\
        ){2}\
    )(\
        ?!172\.(\
            ?:1[6-9]|2\d|3[0-1]\
        )(\
            ?:\.\d{1,3}\
        ){2}\
    )(\
        ?:[1-9]\d?|1\d\d|2[01]\d|22[0-3]\
    )(\
        ?:\.(\
            ?:1?\d{1,2}|2[0-4]\d|25[0-5]\
        )\
    ){2}(\
        ?:\.(\
            ?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]\
        )\
    )|(\
        ?:(\
            ?:[a-z\u00a1-\uffff0-9]+-?\
        )*[a-z\u00a1-\uffff0-9]+\
    )(\
        ?:\.(\
            ?:[a-z\u00a1-\uffff0-9]+-?\
        )*[a-z\u00a1-\uffff0-9]+\
    )*(\
        ?:\.(\
            ?:[a-z\u00a1-\uffff]{2,}\
        )\
    )\
)(\
    ?P<port>:\d{2,5}\
)?(\
    (\
        ?:(\
            ?P<path>/[^\s#\?&]*\
        )(\
            ?P<fragment>#(\
                ?P<fragment_text>[^\s&\?]*\
            )\
        )?(\
            ?P<params>\??[^&\s]*(\
                ?:[^\s]*\
            )\
        )?\
    )?\
)?$".replace(u" ", u"")  # Remove the formatting spaces.

__regex_c = re.compile(__regex, re.U|re.I)  # ignore case; use unicode.

def is_valid_url(url):
    match = re.match(__regex_c, url)
    return bool(match)
    

def normalize_url(url):
    '''
    Accepts a URL, and if the URL is valid, then a normalized URL is returned
    (normalized according to the brief definition that can be found on RFC3986:

    http://tools.ietf.org/html/rfc3986

    If a URL cannot be normalized because, for example, it is invalid, then None
    will be returned, but we make the assumption that the URL passed is valid
    according to the is_valid_url function.
    '''
    url = url.lower()
    match = re.match(__regex_c, url)
    string = None
    if match is not None:
        string = match.group("protocol") + match.group("authority")
        if match.group("path") is None:
            string += "/"
        else:
            string += match.group("path")
    return string
