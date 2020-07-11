#C:\Users\badar\JaspersoftWorkspace\MyReports

# -*- coding: utf-8 -*-
import os
from pyreportjasper import JasperPy


filepath = 'hello_world_params.jrxml'

def compiling():
    jasper = JasperPy()
    jasper.compile(filepath)

def processing():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    jasper = JasperPy()
    jasper.process(
        filepath, output_file=output, format_list=["pdf", "rtf"])

def listing_parameters():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world_params.jrxml'
    jasper = JasperPy()
    output = jasper.list_parameters(filepath)
    print(output)


