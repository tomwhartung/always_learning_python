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
    var get_function_letter_fcn = get_function_letter;
    var css_class = "x-score";  // default value; to override, call css_class()
    var width = 180;            // default value; to override, call width()
    var height = 12;            // default value; to override, call height()
    var tick_format = null;
    /**
     * Function to process each of the SVGGElements in the list
     */
    function score_bars(svgg_elt_list) {
      svgg_elt_list.each(function(data, index) {
        var score_value = get_score_pct_fcn.call(this, data, index);
        var function_letter = get_function_letter_fcn.call(this, data, index);
        var this_svgg_elt = d3.select(this);
        var score_value_arr = []
        score_value_arr = []              // data() fcn expects an array
        score_value_arr.push(score_value);

        // console.log('check check 123 123');
        // console.log('score_bars - width x height: ' + width + ' x ' + height)

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

        score_pct_lines.enter().append("rect")
          .attr("class", set_css_class(function_letter))
          .attr("x", 0)
          .attr("y", height * 2 / 3)
          .attr("width", x_scale)
          .attr("height", height / 3);

        // Compute the tick format.
        var format = tick_format || x_scale.tickFormat(8);

        // Update the tick groups.
        var tick = this_svgg_elt.selectAll("g.tick")
            .data(x_scale.ticks(8), function(data) {
              return this.textContent || format(data);
            });

        //
        // Add the tick marks and the text that appears beneath them
        //
        var tick_enter = tick.enter().append("g")
            .attr("class", "tick")
            .attr("transform", score_bullet_translate(x_scale))
            .style("opacity", 1);
        //
        // Add the actual tick marks
        //
        tick_enter.append("line")
            .attr("y1", height * 1 / 3)
            .attr("y2", height * 4 / 3);
        //
        // Add the label that appears under each tick mark
        //
        tick_enter.append("text")
            .attr("text-anchor", "right")  // anchor it on the right, then
            .attr("dx", "-.5em")           // move it a little to the left
            .attr("dy", "1em")
            .attr("y", height * 7 / 6)
            .text(format);

      });
      d3.timer.flush();
    }

    /**
     * Set (override default) or get current css_class
     */
    score_bars.css_class = function(new_class) {
      if (!arguments.length) {
         return css_class;
      }
      css_class = new_class;
      return score_bars;
    };

    /**
     * Set (override default) or get current width
     */
    score_bars.width = function(new_width) {
      if (!arguments.length) {
         return width;
      }
      width = new_width;
      return score_bars;
    };

    /**
     * Set (override default) or get current height
     */
    score_bars.height = function(new_height) {
      if (!arguments.length) {
         return height;
      }
      height = new_height;
      return score_bars;
    };

    /**
     * Set (override default) or get current tick format
     */
    score_bars.tick_format = function(new_tick_format) {
      if (!arguments.length) {
         return tick_format;
      }
      tick_format = new_tick_format;
      return score_bars;
    };

    return score_bars;
  };
  /*
   * Returns the value for score_pct from the data
   */
  function get_score_pct(data, index) {
    return data.score_pct;
  }
  /*
   * Returns the value for the function_letter from the data
   */
  function get_function_letter(data, index) {
    return data.function_letter;
  }
  /*
   * Return a function that returns a translate string so that the
   * numbers on the axis are not all squished together on the left.
   */
  function score_bullet_translate(x_scale) {
    return function(data) {
      return "translate(" + x_scale(data) + ",0)";
    };
  }
  /**
   * Use the function_letter to set the css class (blue for "N" , etc.)
   */
  function set_css_class (function_letter) {
    /*
     * I am undecided about whether the J & P bars should be grey or should
     * reflect the color of the dominant function (e.g., red for Judging-Feeling)
     * I think the grey bars look better but having the colored bars conveys more information.
     * -> Use this variable to easily toggle whether the bar on the bottom is
     * grey or the same color as the dominant function.
     */
    // var grey_j_p_bars = false;
    var grey_j_p_bars = true;

    if (function_letter == 'N') {
      this.__perceiving_css_class__ = 'n-score'
      css_class = "n-score";
    }
    else if (function_letter == 'S') {
      this.__perceiving_css_class__ = 's-score'
      css_class = "s-score";
    }
    else if (function_letter == 'F') {
      this.__judging_css_class__ = 'f-score'
      css_class = "f-score";
    }
    else if (function_letter == 'T') {
      this.__judging_css_class__ = 't-score'
      css_class = "t-score";
    }
    else if (function_letter == 'P') {
      if (grey_j_p_bars) {
        css_class = "x-score";
      }
      else {
        css_class = this.__perceiving_css_class__;
      }
    }
    else if (function_letter == 'J') {
      if (grey_j_p_bars) {
        css_class = "x-score";
      }
      else {
        css_class = this.__judging_css_class__;
      }
    }
    else {
      css_class = "x-score";
    }
    return css_class;
  }
})();
/**
 * score_bars namespace:
 * ---------------------
 * Keep our utility functions from interfering with other js code
 */
var score_bars = {
   /**
    * Use the data in "score" to create the SVG score bars chart in the
    * location specified by the "selector" , giving it the specified
    * "margin" and "dimension"s.
    */
   create_chart_svg: function(selector, score, margin, dimension) {
      console.log('create_chart_svg - selector: ' + selector);

      score_bars_data = score_bars.score_to_bars_data(score);
      var score_bars_chart = d3.score_bars()
         .tick_format(function(tick_data) {return tick_data + "%";})
         .width(dimension.width)
         .height(dimension.height);

      var score_bars_svg = d3.select(selector).selectAll("svg")
       .data(score_bars_data)
       .enter().append("svg")
       .attr("class", "bullet")
       .attr("width", dimension.width + margin.left + margin.right)
       .attr("height", dimension.height + margin.top + margin.bottom)
       .append("g")
       .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
       .call(score_bars_chart);

      var function_letter_elt = score_bars_svg.append("g")
        .style("text-anchor", "end")
        .attr("transform", "translate(-6," + dimension.height / 2 + ")");

      function_letter_elt.append("text")
        .attr("class", "function-letter")
        .text(function(data) { return data.function_letter; });

      function_letter_elt.append("text")
        .attr("class", "function-name")
        .attr("dy", "1em")
        .text(function(data) { return data.function_name; });

   },
   /**
    * Translate the "score" object found in the json file to the
    * format we need to draw the score_bars chart.
    * This function uses a fairly brute-force approach, so the code should be
    * easy to understand.
    */
   score_to_bars_data: function (score) {
      //
      // Values stored in the passed-in score object:
      //
      var score_value;
      var e_score_value;
      var i_score_value;
      var n_score_value;
      var s_score_value;
      var f_score_value;
      var t_score_value;
      var j_score_value;
      var p_score_value;
      //
      // Intermediate values derived from values in the passed-in score object:
      //
      var e_or_i_letter;
      var n_or_s_letter;
      var f_or_t_letter;
      var j_or_p_letter;
      var e_or_i_name;
      var n_or_s_name;
      var f_or_t_name;
      var e_i_total;
      var n_s_total;
      var f_t_total;
      var j_p_total;
      var e_or_i_score_pct;
      var n_or_s_score_pct;
      var f_or_t_score_pct;
      var j_or_p_score_pct;
      //
      // Values pushed onto the array that this function returns:
      //
      var e_or_i_entry;
      var n_or_s_entry;
      var f_or_t_entry;
      var j_or_p_entry;
      var score_bars_data = [];

      //
      // Find and save the values in the passed-in score object
      //
      for (var index in score ) {
         pair = score[index];
         for (var x_score_key in pair) {
            score_value = pair[x_score_key];
            if (x_score_key == 'e_score') { e_score_value = parseInt(score_value); }
            else if (x_score_key == 'i_score') { i_score_value = parseInt(score_value); }
            else if (x_score_key == 'n_score') { n_score_value = parseInt(score_value); }
            else if (x_score_key == 's_score') { s_score_value = parseInt(score_value); }
            else if (x_score_key == 'f_score') { f_score_value = parseInt(score_value); }
            else if (x_score_key == 't_score') { t_score_value = parseInt(score_value); }
            else if (x_score_key == 'j_score') { j_score_value = parseInt(score_value); }
            else if (x_score_key == 'p_score') { p_score_value = parseInt(score_value); }
         }
      }
      //
      // All values are required!
      // If any of them are missing, return an array containing a 0 score
      //
      if ( isNaN(e_score_value) || isNaN(i_score_value) ||
           isNaN(n_score_value) || isNaN(s_score_value) ||
           isNaN(f_score_value) || isNaN(t_score_value) ||
           isNaN(j_score_value) || isNaN(p_score_value)   ) {
         var letter_x = "X";
         var incomplete = "(Score Incomplete)";
         e_or_i_entry = {
             "function_letter": letter_x,"function_name": incomplete, "score_pct": 0
         };
         n_or_s_entry = {
             "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
         };
         f_or_t_entry = {
             "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
         };
         j_or_p_entry = {
             "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
         };

         score_bars_data.push(e_or_i_entry);
         score_bars_data.push(n_or_s_entry);
         score_bars_data.push(f_or_t_entry);
         score_bars_data.push(j_or_p_entry);
         return score_bars_data;
      }
      //
      // Determine the letters and names, and calculate the percents needed
      //
      e_i_total = e_score_value + i_score_value;
      n_s_total = n_score_value + s_score_value;
      f_t_total = f_score_value + t_score_value;
      j_p_total = j_score_value + p_score_value;

      if (e_score_value > i_score_value) {
         e_or_i_letter = 'E';
         e_or_i_name = 'Extraversion';
         e_or_i_score_pct = Math.round(100 * e_score_value / e_i_total);
      }
      else {
         e_or_i_letter = 'I';
         e_or_i_name = 'Introversion';
         e_or_i_score_pct = Math.round(100 * i_score_value / e_i_total);
      }

      if (n_score_value > s_score_value) {
         n_or_s_letter = 'N';
         n_or_s_name = 'iNtuition';
         n_or_s_score_pct = Math.round(100 * n_score_value / n_s_total);
      }
      else {
         n_or_s_letter = 'S';
         n_or_s_name = 'Sensing';
         n_or_s_score_pct = Math.round(100 * s_score_value / n_s_total);
      }

      if (f_score_value > t_score_value) {
         f_or_t_letter = 'F';
         f_or_t_name = 'Feeling';
         f_or_t_score_pct = Math.round(100 * f_score_value / f_t_total);
      }
      else {
         f_or_t_letter = 'T';
         f_or_t_name = 'Thinking';
         f_or_t_score_pct = Math.round(100 * t_score_value / f_t_total);
      }

      if (j_score_value > p_score_value) {
         j_or_p_letter = 'J';
         j_or_p_name = 'Judging';
         j_or_p_score_pct = Math.round(100 * j_score_value / j_p_total);
      }
      else {
         j_or_p_letter = 'P';
         j_or_p_name = 'Perceiving';
         j_or_p_score_pct = Math.round(100 * p_score_value / j_p_total);
      }

      //
      // Use these values to construct the score_bars_data array
      //
      e_or_i_entry = {
         "function_letter": e_or_i_letter,
         "function_name": e_or_i_name,
         "score_pct": e_or_i_score_pct
      };
      n_or_s_entry = {
         "function_letter": n_or_s_letter,
         "function_name": n_or_s_name,
         "score_pct": n_or_s_score_pct
      };
      f_or_t_entry = {
         "function_letter": f_or_t_letter,
         "function_name": f_or_t_name,
         "score_pct": f_or_t_score_pct
      };
      j_or_p_entry = {
         "function_letter": j_or_p_letter,
         "function_name": j_or_p_name,
         "score_pct": j_or_p_score_pct
      };

      score_bars_data.push(e_or_i_entry);
      score_bars_data.push(n_or_s_entry);
      score_bars_data.push(f_or_t_entry);
      score_bars_data.push(j_or_p_entry);

      return score_bars_data;
   }
}
