Project for CSE 403 quiz section.

Group members:
- Caylan Lee
- Yoong Woo Kim
- Andrew Davies
- Ivan Darmansyah
- Peter Weisbeck
- Brian Oliphant
- Kyle Boone 


Other Group's GitHub
* https://github.com/hunlan/cse403sortingoption


URL Validator
-------------

The URL sorter works fine with sorting strings, but the algorithms have no way of telling whether the strings being sorted are valid URLs. Our URL validator should help address that issue. The choices made for URL validation and normalization were for the sake of time reduction (finding code that's already been written to address our needs) and tailoring it to our own use.

* Files/Functions *
The validation utilities can be found in the url_util.py file, with the
validator function being is_valid_url, and the normalizer function being
normalize_url.

The main command-line tool is located in url_validator.py, and runs much of the
same functionality as urlsort did in the previous assignments.  However, in this
implementation, the heap sort function is used as the default sorting algorithm
due to the speed (when compared to the other functions).  The program has the
option of reading in an input file, and writing out to an output file.  The
encoding of all URLs read in from the file is defaulted to utf-8 without
alternatives as of yet.  When writing out to stdout or piping the output of the
validator, the program may be forced to print escped unicode characters for
optimum performance (an issue that comes up often when using python2.7).

Currently there is no option to suppress the debug output (showing which URLs
are valid, unique, etc as read in from the file) simply due to laziness.

## Validator 

*Decription*

So far, the validator uses a modified regex originally created by Diego Perini,
featured in the article (about the perfect url validator regex)[http://mathiasbynens.be/demo/url-regex].  This validator works with unicode, and will validate a large portion of URLs (though the exact number of valid urls is not yet clear, though every valid URL tested has functioned thus far).

The URL is split according to (RFC 3986)[http://www.ietf.org/rfc/rfc3986.txt],
and is, basically, separated into the following parts:

* protocol
* authority
* port
* path
* fragment
* params

More info on all of these (except for params) can be found in the link.  The
params consist of the parameters given to a page via a GET request in the form

        '?param1=foo&param2=bar'

Overall the regex for the validator is also used with the normalizer, due to the
fact that, with the python regex, we are able to extract the important sections
of the URL for normalization.

*Hangups* 

A problem with the validator is that, due to the large number of parameters, it
is very hard to read.  Apart from handling most cases rather gracefully, one
place that likely needs inspection is the area toward the end of the code that
tries to deal with parameters being sent to a specific URL.  There is no
standard checking of parameters, and they are all globbed together as the area
that follows the first '?' symbol or '&' symbol (after the authority section and path).  This was not dealt with on account of the difficulty, and the fact that a large number of URLs were all parsed properly. 

## Normalizer

The normalizer uses the same regex as described in the validator section above.
The normalizer canonicalizes URLs in the following manner:  A URL is first
assumed to be valid (else the outcome of the function is not defined).  The URL
is first compressed into an all-lowercase version of the protocol and the
authority.  For example:

        http://foo.bar.com

Would be the initial state of the URL.  After this, the path is then, case
preserved, appended to the end of the URL.  If there is no path, a simple '/'
character will be added.  The path case is preserved on account of the fact that
paths on Unix systems are case sensitive, whereas domain names and protocols are
not.

After this has occurred, the remaining sections: the fragment, and the params,
are simply chopped off.  The params were left off despite the fact that they
would change the page simply because the implementation of validating parameters
was deemed too difficult for the current portion of the assignment after having
already found and implemented such a robust URL validation regex.

## Comparator

The URL comparator was left with the simple Python string comparisons on account
of the fact that, quite frankly, no one on the team could come up with a way to
sort URLs that wouldn't be confusing in the end when compared to plain old
alphabetizing.  So, sorting has remained largely the same via comparisons.
