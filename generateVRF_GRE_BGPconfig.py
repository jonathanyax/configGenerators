import sys
import os
from jinja2 import Environment, FileSystemLoader

#Initialize the jinja2 environment to load templates
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(sys.argv[1])

#Variables from input variables file (file name input by user)
# will be transformed into a dict
varsDict = {}
with open(sys.argv[2]) as varsFile:
  for line in varsFile:
    (key, val) = line.strip().split(": ")
    varsDict[key] = val

#Populate the jinja template with values from varsDict
renderedTemplate = template.render(varsDict)

#Write the output to a file for easy copy and paste
outFile = open("vrf_gre_bgp_config.txt", "wt")
outFile.write(renderedTemplate)
outFile.close()