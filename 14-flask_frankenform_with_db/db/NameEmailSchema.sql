--
--  Schema for our NameEmail table
--  ------------------------------
--  Reference for datatypes:
--     https://www.sqlite.org/datatype3.html
--  Note the date_* columns are stored as Unix Time in integers, specifically:
--     "INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC"
--
CREATE TABLE NameEmail
   ( id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT,
     email TEXT,
     site TEXT DEFAULT 'groja.com',
     active INTEGER DEFAULT 1,
     date_added INTEGER,
     date_changed INTEGER,
     consulting INTEGER DEFAULT 0,
     newsletter INTEGER DEFAULT 0,
     portrait INTEGER DEFAULT 0
   )

