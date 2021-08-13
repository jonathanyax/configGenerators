import sys
import os
from jinja2 import Environment, FileSystemLoader

#Initialize the jinja2 environment to load templates
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(sys.argv[1])


interfaces = []
with open("nsoInput.txt") as f:
	for line in f:
		if line.startswith('interfaces', 3):
			intInfo = {}
			intNumber = "GigabitEthernet%d" %(int(line[24]) + 1)
			intInfo.update({'name':intNumber})
		if line.startswith('ip_address', 4):
			line = (line.lstrip(' ').strip('\n'))
			updated = line.split()
			intInfo.update({updated[0]:updated[1]})
		if line.startswith('netmask', 4):
			line = (line.lstrip(' ').strip('\n'))
			updated = line.split()
			intInfo.update({updated[0]:updated[1]})
		if line.startswith('gateway', 4):
			line = (line.lstrip(' ').strip('\n'))
			updated = line.split()
			intInfo.update({updated[0]:updated[1]})
			interfaces.append(intInfo)


renderedTemplate = template.render(interfaces=interfaces)
print(renderedTemplate)
 
outFile = open("output.txt", "wt")
outFile.write(renderedTemplate)
outFile.close()