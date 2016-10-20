#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open("yaml_dump_wk1") as f:
	pp("-" * 50)
	pp(" " * 50)
	pp(" " * 20 + "YAML Output")
	pp(" " * 50)
	pp("-" * 50)
	pp(yaml.load(f))

with open("json_dump_wk1") as g:
	pp("-" * 50)
        pp(" " * 50)
        pp(" " * 20 + "JSON Output")
        pp(" " * 50)
        pp("-" * 50)
	pp(json.load(g))
