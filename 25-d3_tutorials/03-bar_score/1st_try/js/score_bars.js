/**
 * score_bars.js: trying to use score json to create bars as described
 *   in the Goal section of the README.md
 * Starting with code from:
 *   01-aligned_left/16-axes (16: Axes)
 * Adding code and ideas from:
 *   02-bullet_charts/04-removed_ranges
 */
var dataset = [];
// var random_dataset = false;
var random_dataset = true;

if ( random_dataset ) {
  var numDataPoints = 50;
  var xRange = Math.random() * 1000;
  var yRange = Math.random() * 1000;
  for (var i = 0; i < numDataPoints; i++) {
    var newNumber1 = Math.round(Math.random() * xRange);
    var newNumber2 = Math.round(Math.random() * yRange);
    dataset.push([newNumber1, newNumber2]);
  }
}
else {
  dataset = [
    [ 5,     20 ],
    [ 460,  190 ],
    [ 250,  150 ],
    [ 100,  233 ],
    [ 330,  495 ],
    [ 410,  312 ],
    [ 425,  244 ],
    [ 25,   467 ],
    [ 85,   121 ],
    [ 220,   88 ]
  ];
}

