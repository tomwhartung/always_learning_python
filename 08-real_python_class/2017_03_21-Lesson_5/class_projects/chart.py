##
#  Code (similar to what) that we want to drop into app.py
#
from collections import defaultdict
def chart():
   all_data = defaultdict(list)
   query = models.Currency.query.all()
   p = figure(
       width=1080,
       height=600,
       x_axis_type="datetime",
   )
   for row in query:
       all_data[row.exchange].append((row.horah, row.price))
   for i, (exchange, points) in enumerate(all_data.items())
           color = bokeh.palettes.Category20[20][i]
           X,Y = zip(*sorted(points))
           p.line(X,Y, line_width=2, alpha=0.7, legend=exchange, color=color)
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   script, div = components(p)
   return render_template(
       'index.html',
       js_resources = js_resources,
       css_resources = css_resources,
       plot_script = script,
       plot_div = div,
   )
