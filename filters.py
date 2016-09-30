# filters.py
"Custom jinja2 filters"

import jinja2
import flask
from flask import Markup

import plot
blueprint = flask.Blueprint('filters', __name__)


# using the method
@jinja2.contextfilter
def filter2(context, value):
    return "result is "+str(value)

@jinja2.contextfilter
def mpl_figure(context, fig):
    html = '<img src="data:image/png;base64,{}" />'.format(plot.mpl_to_base64(fig))
    return Markup(html) # this makes the html appear correctly, instead of as text

blueprint.add_app_template_filter(filter2)
blueprint.add_app_template_filter(mpl_figure)
