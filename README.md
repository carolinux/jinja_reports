Use jinja2 templates for automated scientific report creation (think IPython, but in the context of an actual website). The idea is that there is a need to be able to create and embed plots easily within jinja templates (without creating intermediate picture files). This repo creates two new jinja filters that support the html rendering of matplotlib figure objects and bokeh figure objects.

It's quite hard to populate ipython notebooks with custom data and/or use them as templates, so this is how jinja2 templates can offer an alternative for the user facing endpoint of a scientific report.

Install requirements and then launch the examples like so:
```
pip install -r requirements.txt
python web.py
```

Created by Karolina Alexiou
carolinegr@gmail.com
