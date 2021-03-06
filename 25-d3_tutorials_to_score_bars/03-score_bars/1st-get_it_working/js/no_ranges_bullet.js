(function() {
//
// no_ranges_bullet.js: derived from bullet.js , found in the d3 gallery
//   This one is based on 02-bullet_charts/04-removed_ranges/bullet.js
// References:
//   https://github.com/d3/d3/wiki/Gallery
//   https://bl.ocks.org/mbostock/4061961
//
// Chart design based on the recommendations of Stephen Few. Implementation
// based on the work of Clint Ivy, Jamie Love, and Jason Davies.
// http://projects.instantcognition.com/protovis/bulletchart/
//
d3.no_ranges_bullet = function() {
  var orient = "left", // TODO top & bottom
      reverse = false,
      duration = 0,
      markers = noRangesBulletMarkers,
      width = 380,
      height = 30,
      tickFormat = null;

  // For each small multiple…
  function no_ranges_bullet(g) {
    g.each(function(data, i) {
      var markerz = markers.call(this, data, i).slice().sort(d3.descending),
          g = d3.select(this);

      // Compute the new x-scale.
      var x1 = d3.scale.linear()
          .domain([0, 100])
          .range(reverse ? [width, 0] : [0, width]);

      // Retrieve the old x-scale, if this is an update.
      var x0 = this.__chart__ || d3.scale.linear()
          .domain([0, Infinity])
          .range(x1.range());

      // Stash the new scale.
      this.__chart__ = x1;

      // Derive width-scales from the x-scales.
      var w0 = noRangesBulletWidth(x0),
          w1 = noRangesBulletWidth(x1);

      // Update the marker lines.
      var marker = g.selectAll("line.marker")
          .data(markerz);

      marker.enter().append("line")
          .attr("class", "marker")
          .attr("x1", x0)
          .attr("x2", x0)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6)
        .transition()
          .duration(duration)
          .attr("x1", x1)
          .attr("x2", x1);

      marker.transition()
          .duration(duration)
          .attr("x1", x1)
          .attr("x2", x1)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6);

      // Compute the tick format.
      var format = tickFormat || x1.tickFormat(8);

      // Update the tick groups.
      var tick = g.selectAll("g.tick")
          .data(x1.ticks(8), function(data) {
            return this.textContent || format(data);
          });

      // Initialize the ticks with the old scale, x0.
      var tickEnter = tick.enter().append("g")
          .attr("class", "tick")
          .attr("transform", noRangesBulletTranslate(x0))
          .style("opacity", 1e-6);

      tickEnter.append("line")
          .attr("y1", height)
          .attr("y2", height * 7 / 6);

      tickEnter.append("text")
          .attr("text-anchor", "middle")
          .attr("dy", "1em")
          .attr("y", height * 7 / 6)
          .text(format);

      // Transition the entering ticks to the new scale, x1.
      tickEnter.transition()
          .duration(duration)
          .attr("transform", noRangesBulletTranslate(x1))
          .style("opacity", 1);
    });
    d3.timer.flush();
  }

  // left, right, top, bottom
  no_ranges_bullet.orient = function(x) {
    if (!arguments.length) return orient;
    orient = x;
    reverse = orient == "right" || orient == "bottom";
    return no_ranges_bullet;
  };

  // markers (previous, goal)
  no_ranges_bullet.markers = function(x) {
    if (!arguments.length) return markers;
    markers = x;
    return no_ranges_bullet;
  };

  no_ranges_bullet.width = function(x) {
    if (!arguments.length) return width;
    width = x;
    return no_ranges_bullet;
  };

  no_ranges_bullet.height = function(x) {
    if (!arguments.length) return height;
    height = x;
    return no_ranges_bullet;
  };

  no_ranges_bullet.tickFormat = function(x) {
    if (!arguments.length) return tickFormat;
    tickFormat = x;
    return no_ranges_bullet;
  };

  no_ranges_bullet.duration = function(x) {
    if (!arguments.length) return duration;
    duration = x;
    return no_ranges_bullet;
  };

  return no_ranges_bullet;
};

function noRangesBulletMarkers(data) {
  return data.markers;
}

function noRangesBulletTranslate(x) {
  return function(data) {
    return "translate(" + x(data) + ",0)";
  };
}

function noRangesBulletWidth(x) {
  var x0 = x(0);
  return function(data) {
    return Math.abs(x(data) - x0);
  };
}

})();
