# configGenerators

These scripts utilize a mix of Python and Jinja template to create configs for CXR devices. In this repo, there are two generator files:
  1. generateInterfaces.py
  2. generateVRF_GRE_BGPconfig.py

Both scripts have been developed and tested on MacOS. It is assumed that the user will be using MacOS, though transferring to Windows or Linux shouldn't be too difficult. 


In Mac, make sure you have the latest version of Python, PIP, and Jinja installed. 

-----

<b>generateInterfaces.py</b>
In order to execute this file, make sure you have the following:
  1. generateInterfaces.py - the actual python script 
  2. interfaceTemplate.j2 - the jinja template that the script fills out
  3. nsoInput.txt - data taken from NSO which the script will parse and extrapolate interface information. Content MUST be in the format of this file in order for script to work

To run the script, enter in your terminal: 

`python3 generateInterfaces.py interfaceTemplate.j2`

The results will be output to a file called `'output.txt'`


-----

<b>generateVRF_GRE_BGPconfig.py</b>
In order to execute this file, make sure you have the following files in the SAME directory:
  1. generateVRF_GRE_BGPconfig.py - python script that does the work
  2. vrf_gre_bgp_template.j2 - the jinja template that the script fills out
  3. vrf_grp_bgp_vars.txt - the variables that will be read. Content MUST be in the format of this file in order for script to work

To run the script, enter in your terminal: 

`python3 generateVRF_GRE_BGPconfig.py vrf_gre_bgp_template.j2 vrf_gre_bgp_vars.txt`

The results will be output to a file called `vrf_gre_bgp_config.txt`
