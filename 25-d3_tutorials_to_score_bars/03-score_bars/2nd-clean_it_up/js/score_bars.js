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
    var reverse = false;
    var get_score_pct_fcn = get_score_pct;
    var width = 180;   // default value; to override, call width()
    var height = 12;   // default value; to override, call height()
    var tick_format = null;
    /**
     * Function to process each of the SVGGElements in the list
     */
    function score_bars(svgg_elt_list) {
      svgg_elt_list.each(function(data, index) {
        var score_value = get_score_pct_fcn.call(this, data, index);
        var this_svgg_elt = d3.select(this);
        var score_value_arr = []
        score_value_arr = []              // data() fcn expects an array
        score_value_arr.push(score_value);

        console.log('check check check 123 123 123 score_value: ' + score_value);
        console.log('score_bars - width x height: ' + width + ' x ' + height)

        var x_scale = d3.scale.linear()
            .domain([0, 100])
            .range(reverse ? [width, 0] : [0, width]);

        var score_pct_lines = this_svgg_elt.selectAll("line.score-pct")
            .data(score_value_arr);

        score_pct_lines.enter().append("line")
            .attr("class", "score-pct")
            .attr("x1", x_scale)
            .attr("x2", x_scale)
            .attr("y1", height / 6)
            .attr("y2", height * 5 / 6);

        // Compute the tick format.
        var format = tick_format || x_scale.tickFormat(8);

        // Update the tick groups.
        var tick = this_svgg_elt.selectAll("g.tick")
            .data(x_scale.ticks(8), function(data) {
              return this.textContent || format(data);
            });

        // Add the ticks
        var tick_enter = tick.enter().append("g")
            .attr("class", "tick")
            .attr("transform", score_bullet_translate(x_scale))
            .style("opacity", 1);

        tick_enter.append("line")
            .attr("y1", height)
            .attr("y2", height * 7 / 6);

        tick_enter.append("text")
            .attr("text-anchor", "middle")
            .attr("dy", "1em")
            .attr("y", height * 7 / 6)
            .text(format);

      });
      d3.timer.flush();
    }

    /**
     * Set (override default) or get current width
     */
    score_bars.width = function(new_width) {
      if (!arguments.length) return width;
      width = new_width;
      return score_bars;
    };

    /**
     * Set (override default) or get current height
     */
    score_bars.height = function(new_height) {
      if (!arguments.length) return height;
      height = new_height;
      return score_bars;
    };

    /**
     * Set (override default) or get current tick format
     */
    score_bars.tick_format = function(new_tick_format) {
      if (!arguments.length) return tick_format;
      tick_format = new_tick_format;
      return score_bars;
    };

    return score_bars;
  };

  function get_score_pct(data, index) {
    return data.score_pct;
  }

  function score_bullet_translate(x_scale) {
    return function(data) {
      return "translate(" + x_scale(data) + ",0)";
    };
  }
})();
