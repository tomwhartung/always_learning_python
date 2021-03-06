# 25-d3_tutorials_to_score_bars

Explore the possibility of using D3.js to draw the score scales on seeourminds.com .

## Goal:

This section describes the goal of this project.

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

## Results

See the final section named **Conclusion** at the very end of this file.

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

#### Process:

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

* Got rid of a lot of code we don't need.
* Not sure how we might adapt what we have here to our purposes

#### Process:

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

#### 2.3 Delete as much code as we can

Got rid of a lot of code we don't need:

```
mkdir 03-before_removing_ranges
cp 02-fix_errors/* 03-before_removing_ranges
vi 03-before_removing_ranges/index.html   # etc....
mkdir 04-removed_ranges
cp 03-before_removing_ranges/* 04-removed_ranges
```

### 03-score_bars

#### Process:

1. Start with latest version of code from `01-aligned_left` (`16-axes`)
2. Update to use score data somehow
3. Add ideas and code from latest version of `02-bullet_charts` (`04-removed_ranges`)
4. Update to display horizontal score bars somehow

##### 3.1 Starting point

```
mkdir -p 03-score_bars/1st-get_it_working
cp -r 01-aligned_left/16-axes/*  03-score_bars/1st-get_it_working/
.......
```

##### 3.2 Updating the code

This proved to be very challenging.
Someday I would like to offer the author of the code a critique, bwahaha.

Finding a way to get the code to do what I want it to required taking baby steps.

##### 3.3 Cleaning up the code

After getting it to work, we need to delete everyt hing unrelated to our score_bars.
No worries, we are leaving the final "big" versions in the `1st-get_it_working` sub-project.

```
cd 03-score_bars
mkdir 2nd-clean_it_up
cp -r 1st-get_it_working/* 2nd-clean_it_up
.......
```

##### 3.4 Final touches (3 graphs)

We want to create another sub-project that includes code to
convert the score json to the array we need for the score_bars.

```
cd 03-score_bars
mkdir 3rd-final_touches-3_graphs
cp -r 2nd-clean_it_up/* 3rd-final_touches-3_graphs
.......
```

##### 3.5 Single graph all data

Reduce to the minimal amount of code we can add to the single image and
result pages to get a graph for quiz results and full-sized images.

```
cd 03-score_bars
mkdir 4th-one_graph_all_data
cp -r 3rd-final_touches-3_graphs/* 4th-one_graph_all_data
.......
```

There may be other last-minute changes (e.g., css and positioning) to
make before porting this into the seeourminds.com code, we shall see.
But we won't be making those changes here.

The idea is to get this code as close as possible to what we can drop into
the pages mentioned above.

##### 3.6 Small graph experiment

Test the feasibility of having a small graph for display with smaller images,
such as on the gallery landing page and in the gallery pages.

```
cd 03-score_bars
mkdir 5th-small_graph_exp
cp -r 3rd-final_touches-3_graphs/* 5th-small_graph_exp
cp 4th-one_graph_all_data/js/score_bars.js  5th-small_graph_exp/js
.......
```

**Consider making the four-letter-type on these images a link that will
display this small graph when someone clicks on it.**

##### 3.7 Final combination

Combine the last three sub-projects into a single new sub-project and

* Ensure all work with the same version of score_bars.js and score_bars.css
* See if they will work with version 4 of d3
* Ultimately drop this code into the site (seeourminds.com)

```
cd 03-score_bars
mkdir 6th-final_combination
cp -r 3rd-final_touches-3_graphs/* 6th-final_combination
cp 4th-one_graph_all_data/index.html 6th-final_combination/index-4th-big.html
cp 4th-one_graph_all_data/js/score_bars.js 6th-final_combination/js
cp 5th-small_graph_exp/index.html 6th-final_combination/index-5th-small.html
.......
```

#### D3 Version 4 Testing

Using the `6th-final_combination` files, see if we can use Version 4 of D3.

##### First: Prevent Confusion!

Copy and rename files as appropriate, so that we can test Version 4 of D3
without getting confused!

```
cd 03-score_bars
cd 6th-final_combination
cp ...
mv ...
cd js
cp score_bars.js score_bars-v4.js
```

Results:

```
ls -1
3rd-final_touches-3_graphs-v3.html
3rd-final_touches-3_graphs-v4.html
4th-one_graph_all_data-v3.html
4th-one_graph_all_data-v4.html
5th-small_graph_exp-v3.html
5th-small_graph_exp-v4.html
vi 3rd-final_touches-3_graphs-v3.html   # update headings to prevent confusion!
vi 3rd-final_touches-3_graphs-v4.html   # update to use js/score_bars-v4.js
vi 4th-one_graph_all_data-v3.html       # update headings to prevent confusion!
vi 4th-one_graph_all_data-v4.html       # update to use js/score_bars-v4.js
vi 5th-small_graph_exp-v3.html          # update headings to prevent confusion!
vi 5th-small_graph_exp-v4.html          # update to use js/score_bars-v4.js
```

And in the javascript directory:

```
ls -1 js/*
js/score_bars.js
js/score_bars-v4.js

js/d3:
d3-3.5.17.js
d3.v3.js
d3.v4.js
d3.v4.min.js
```

##### Second: Test Using Version 4 of D3

Test in browser and update `score_bars-v4.js` as needed.

```
cd 03-score_bars
cd 6th-final_combination
cd js
vi score_bars-v4.js
```

Whoo-hoo - it turns out we need only a couple of minor modifications!  Yay!!

### 04-final_d3v4

Grab only essential code needed to draw the bars using Version 4 of D3.

```
mkdir 04-final_d3v4
cp 03-score_bars/6th-final_combination/index.html  04-final_d3v4
cp 03-score_bars/6th-final_combination/4th-one_graph_all_data-v4.html  04-final_d3v4
cp 03-score_bars/6th-final_combination/5th-small_graph_exp-v4.html  04-final_d3v4
cp 03-score_bars/6th-final_combination/run.sh 04-final_d3v4
mkdir 04-final_d3v4/css
cp 03-score_bars/6th-final_combination/css/sanity.css 04-final_d3v4/css/        # one little bit of cruft for sanity's sake!
cp 03-score_bars/6th-final_combination/css/score_bars.css 04-final_d3v4/css/
mkdir 04-final_d3v4/js
cp 03-score_bars/6th-final_combination/js/score_bars-v4.js 04-final_d3v4/js/
cd  04-final_d3v4/js/
mv score_bars-v4.js score_bars.js
cd -
mkdir 04-final_d3v4/js/d3
cp 03-score_bars/6th-final_combination/js/d3/d3.v4.* 04-final_d3v4/js/d3
lf
vi index.html
vi 4th-one_graph_all_data-v4.html
vi 5th-small_graph_exp-v4.html
```

And I think we are finally ready to drop this in to the site code!!

## Conclusion

* Use the code from `04-final_d3v4` on the site (**except** `css/sanity.css`).
* If there are ever any issues, try falling back on version 3 of D3.
* That code is in the `*-v3.*` files in `03-score_bars/6th-final_combination`.

