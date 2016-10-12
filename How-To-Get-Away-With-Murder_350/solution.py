import datetime

micro = 13115115452298564

date_string = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=micro)
print date_string

# We are given a sqlite3 file, which contains download history from Google Chrome.
# $ sqlite3
# > .open History
# > select * from downloads;

# We see a date string, but by running `pragma table_info(downloads);`, we see that it's just the modification date of the downloaded file
# We want the 4th column, which represents the visit time.

# This is conveniently documented online:
# http://forensicswiki.org/wiki/Google_Chrome#History

# Anyways, this code converts from microseconds to a nice datestring but to comply with the flag format, we turn from
# 2016-08-08 07:37:32.298564
# to
# 2016-08-08 07:37:32 UTC
