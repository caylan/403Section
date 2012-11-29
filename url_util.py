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
__regex = u"^\
(\
    ?:(\
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
    ?::\d{2,5}\
)?(\
    ?:/[^\s]*\
)?$".replace(u" ", u"")  # Remove the formatting spaces.

__regex_c = re.compile(__regex, re.U|re.I)  # ignore case; use unicode.

def is_valid_url(url):
    match = re.match(__regex_c, url)
    if match is not None:
        print(match.group("authority"))
    return bool(match)
