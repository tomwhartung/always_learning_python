# 25-d3_tutorials

Explore the possibility of using D3.js to draw the score scales on seeourminds.com .

## Goal:

This is the goal of this project:

### Input data:

See the values for the `score` in the json files in the `00-test_json` directory.

### Output graph:

We want a horizontal bar graph containing four bars that repreents the `score` as follows:

* 1st bar: E/I
  * Label: E or I, whichever score is higher
  * Color: dark grey or black (depending on aesthetics)
  * Length: matches score
* 2nd bar: N/S
  * Label: N or S, whichever score is higher
  * Color: blue if N score is higher, else yellow
  * Length: matches score
* 3rd bar: F/T
  * Label: F or T, whichever score is higher
  * Color: red if F score is higher, else green
  * Length: matches score
* 4th bar: J/P
  * Label: J or P, whichever score is higher
  * Color, if J score is higher: red or green (depending on F and T scores)
  * Color: else (if P score is higher): blue or yellow (depending on N and S scores)
  * Length: matches score

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




