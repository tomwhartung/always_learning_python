#
#  Schema for our NameEmail table
#  ------------------------------
#  Reference for datatypes:
#     https://www.sqlite.org/datatype3.html
#
CREATE TABLE NameEmail
   ( name TEXT,
     email TEXT,
     site TEXT DEFAULT 'groja.com',
     active INTEGER DEFAULT 1,
     date_added INTEGER,
     date_changed INTEGER,
     consulting INTEGER DEFAULT 0,
     newsletter INTEGER DEFAULT 0,
     portrait INTEGER DEFAULT 0
   )

