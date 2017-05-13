(function() {
//
// score_bullet.js: derived from bullet.js , found in the d3 gallery
//   This one is based on 02-bullet_charts/04-removed_ranges/bullet.js
// References:
//   https://github.com/d3/d3/wiki/Gallery
//   https://bl.ocks.org/mbostock/4061961
//
// Chart design based on the recommendations of Stephen Few. Implementation
// based on the work of Clint Ivy, Jamie Love, and Jason Davies.
// http://projects.instantcognition.com/protovis/bulletchart/
//
d3.score_bullet = function() {
  var orient = "left";
  var reverse = false;
  var duration = 0;
  var markers = get_score_pct;
  var width = 380;
  var height = 30;
  var tickFormat = null;

  // For each small multiple…
  function score_bullet(g) {
    g.each(function(data, i) {
      var marker_value = markers.call(this, data, i).slice().sort(d3.descending);
      var g = d3.select(this);

      console.log( 'marker_value: ' + marker_value );

      // Compute the new x-scale.
      var x_scale = d3.scale.linear()
          .domain([0, 100])
          .range(reverse ? [width, 0] : [0, width]);

      // // Stash the new scale.
      // this.__chart__ = x_scale;

      // Update the marker lines.
      var marker = g.selectAll("line.marker")
          .data(marker_value);

      marker.enter().append("line")
          .attr("class", "marker")
          .attr("x1", x_scale)
          .attr("x2", x_scale)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6);

/* *******************************************
      marker.transition()
          .duration(duration)
          .attr("x1", x_scale)
          .attr("x2", x_scale)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6);
 ******************************************** */

      // Compute the tick format.
      var format = tickFormat || x_scale.tickFormat(8);

      // Update the tick groups.
      var tick = g.selectAll("g.tick")
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
  score_bullet.orient = function(x) {
    if (!arguments.length) return orient;
    orient = x;
    reverse = orient == "right" || orient == "bottom";
    return score_bullet;
  };

  // markers
  score_bullet.markers = function(x) {
    if (!arguments.length) return markers;
    markers = x;
    return score_bullet;
  };

  score_bullet.width = function(x) {
    if (!arguments.length) return width;
    width = x;
    return score_bullet;
  };

  score_bullet.height = function(x) {
    if (!arguments.length) return height;
    height = x;
    return score_bullet;
  };

  score_bullet.tickFormat = function(x) {
    if (!arguments.length) return tickFormat;
    tickFormat = x;
    return score_bullet;
  };

  score_bullet.duration = function(x) {
    if (!arguments.length) return duration;
    duration = x;
    return score_bullet;
  };

  return score_bullet;
};

function get_score_pct(data) {
  console.log('get_score_pct: data.score_pct: ' + data.score_pct);
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
