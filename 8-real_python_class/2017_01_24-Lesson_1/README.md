
# Lesson 1

Some things to note from the first class, on Tues. Jan. 24, 2017.

## Setup Notes:

### Contaminating err Installing nodejs and npm on bette:

For steps used to install python 3.6, and nodejs and npm, see:

* doc/ubuntu/specific_hosts/2016-bette/3-experimenting_with_extras.txt in the jmws_accoutrements repo.

### Accessing the slides:

Running `npm install` gave node command not found errors, so I ran the following commands:

```
 $ which nodejs 
/usr/bin/nodejs
 $ cd /usr/local/bin
 $ ln -s /usr/bin/nodejs node
```

