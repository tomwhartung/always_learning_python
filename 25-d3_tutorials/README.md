# 25-d3_tutorials

Explore the possibility of using D3.js to draw the score scales on seeourminds.com .

## References:

This looks like a good place to start:

- http://alignedleft.com/tutorials/d3/fundamentals

This is the sort of graph we want:

- https://bl.ocks.org/mbostock/4061961

I found a link to that page on the d3 gallery page:

- https://github.com/d3/d3/wiki/Gallery

## Tutorials and Results

### 01-aligned_left

#### Result:

This is a great tutorial!
It's a little friendly/chatty, but the organization, flow, and
chunking of information into bite-sized pieces are all excellent.

#### Process

##### 1.1 d3 setup

Following http://alignedleft.com/tutorials/d3/fundamentals :

Downloaded d3-3.5.17.js from:

- http://d3js.org/d3.v3.js

##### 1.2 http-server setup

Installed http-server so we can run a test server:

- https://github.com/d3/d3/wiki

As root:
```
npm install -g http-server
```

To run it:

As tomh:
```
http-server
```

To access it:

- https://github.com/d3/d3/wiki

##### 1.3 Running the steps

See the sequenced subdirectories for code developed while running through the steps.

### 02-bullet_charts

Reference:

- https://bl.ocks.org/mbostock/4061961

This is **not** a tutorial, but an example from the gallery:

- https://github.com/d3/d3/wiki/Gallery

#### Result:

#### Process

#### 2.1 Try to run the code, as-is

```
mkdir -p 02-bullet_charts/01-copy_and_pasted_code
```

Code does not work as-is!  Getting a 404 on bullet.js !

#### 2.2 Try to fix the "as-is" code

```
cd 02-bullet_charts/
mkdir 02-fix_errors
cp 01-copy_and_pasted_code/* 02-fix_errors
vi 02-fix_errors/index.html
```

Oops my bad: the file name needs to be `bullet.js` not `bullets.js` .

#### 2.3 Get creative!

See if we can get this idea, and the code that goes with it, to work for
our seeourminds.com scores.

```
mkdir 03-get_creative
cp 02-fix_errors/* 03-get_creative
vi 03-get_creative/index.html   # etc....
```




