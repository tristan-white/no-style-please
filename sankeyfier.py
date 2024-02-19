#!/usr/bin/python3
'''
This script is for simplifying the process of creating sankey
graphs with plotlyjs. It parses a csv file in the following 
format:

SOURCE,TARGET,VALUE,NOTE

Plotlyjs takes json as input but instead of using names for
SOURCE and TARGET it uses indices from a the variable "label"
which contains names of sources and targets - thus this 
script simplifies creating a list of indices by enabling the
user to simply supply a csv with verbose names. The NOTE
field will be ignored by this script.
'''
import json
import sys

import plotly.graph_objects as go

sources = []
targets = []
values = []
with open(sys.argv[1], "r") as f:
	rows = f.readlines()
	# First pass of list gets list of unique sources
	labels = set()
	for r in rows:
		labels.add(r.split(",")[0])
		labels.add(r.split(",")[1])
	indices = {l:i for i,l in enumerate(labels)}
	print(indices)
	for r in rows:
		sources.append(indices[r.split(",")[0]])
		targets.append(indices[r.split(",")[1]])
		values.append(r.split(",")[2])

trace = dict(
	trace = "sankey",
	orientation = "h",
	node = dict(
		pad = 15,
		thickness = 30,
		line = dict(
			color = "black",
			width = 0.5
		),
		label = list(labels),
		color = "blue",
	),
	link = dict(
		source = sources,
		target = targets,
		value = values
	)
)
data = [trace]
layout = dict(
	title = "Title",
	font = dict(
		size = 10,
	)
)

final = {"data": data, "layout": layout}

# print(json.dumps(final, indent=10))

fig = go.Figure(
	data=[go.Sankey(node=trace["node"], link=trace["link"])]
)
fig.update_layout(title_text="title", font_size=10)
fig.show()
