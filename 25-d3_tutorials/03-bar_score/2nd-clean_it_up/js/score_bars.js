/**
 * score_bars.js: using score json to create horizontal d3 bars
 * ------------------------------------------------------------
 * Derived from bullet.js , found in the d3 gallery
 * Overview:
 * Starting with code from:
 *   01-aligned_left/16-axes (16: Axes)
 * Adding code and ideas from:
 *   02-bullet_charts/04-removed_ranges
 *   This file is derived from 02-bullet_charts/04-removed_ranges/bullet.js
 *
 * This version is a work in progress!
 * -----------------------------------
 * For more information, see the Goal section of the README.md
 * References:
 *   https://github.com/d3/d3/wiki/Gallery
 *   https://bl.ocks.org/mbostock/4061961
 */
//
// (Following are the original comments from bullet.js in the d3 gallery:)
//   Chart design based on the recommendations of Stephen Few. Implementation
//   based on the work of Clint Ivy, Jamie Love, and Jason Davies.
//     http://projects.instantcognition.com/protovis/bulletchart/
//
(function() {
d3.score_bars = function() {
  var orient = "left";
  var reverse = false;
  var get_score_pct_fcn = get_score_pct;
  var width = 380;
  var height = 30;
  var tickFormat = null;

  // For each small multiple…
  function score_bars(svgg_elt_list) {
    console.log('score_bars - passed-in "svgg_elt_list" = ' + svgg_elt_list)
    svgg_elt_list.each(function(data, index) {
      var score_value = get_score_pct_fcn.call(this, data, index);
      var this_svgg_elt = d3.select(this);
      console.log('score_bars - var "this_svgg_elt" = ' + this_svgg_elt)
		var score_value_arr = []
		score_value_arr = []
		score_value_arr.push(score_value);

      console.log('check check check 123 123 123 bbb ccc 123 456 score_value: ' + score_value);

      // Compute the new x-scale.
      var x_scale = d3.scale.linear()
          .domain([0, 100])
          .range(reverse ? [width, 0] : [0, width]);

      // Update the score-pct lines.
      var score_pct_lines = this_svgg_elt.selectAll("line.score-pct")
          .data(score_value_arr);

      score_pct_lines.enter().append("line")
          .attr("class", "score-pct")
          .attr("x1", x_scale)
          .attr("x2", x_scale)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6);

      // Compute the tick format.
      var format = tickFormat || x_scale.tickFormat(8);

      // Update the tick groups.
      var tick = this_svgg_elt.selectAll("g.tick")
          .data(x_scale.ticks(8), function(data) {
            return this.textContent || format(data);
          });

      // Add the ticks
      var tickEnter = tick.enter().append("g")
          .attr("class", "tick")
          .attr("transform", scoreBulletTranslate(x_scale))
          .style("opacity", 1);

      tickEnter.append("line")
          .attr("y1", height)
          .attr("y2", height * 7 / 6);

      tickEnter.append("text")
          .attr("text-anchor", "middle")
          .attr("dy", "1em")
          .attr("y", height * 7 / 6)
          .text(format);

    });
    d3.timer.flush();
  }

  // left, right, top, bottom
  score_bars.orient = function(x) {
    if (!arguments.length) return orient;
    orient = x;
    reverse = orient == "right" || orient == "bottom";
    return score_bars;
  };

  score_bars.width = function(x) {
    if (!arguments.length) return width;
    width = x;
    return score_bars;
  };

  score_bars.height = function(x) {
    if (!arguments.length) return height;
    height = x;
    return score_bars;
  };

  score_bars.tickFormat = function(x) {
    if (!arguments.length) return tickFormat;
    tickFormat = x;
    return score_bars;
  };

  return score_bars;
};

function get_score_pct(data, index) {
  return data.score_pct;
}

function scoreBulletTranslate(x) {
  return function(data) {
    return "translate(" + x(data) + ",0)";
  };
}

function scoreBulletWidth(x) {
  var x0 = x(0);
  return function(data) {
    return Math.abs(x(data) - x0);
  };
}

})();
