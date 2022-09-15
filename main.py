#--------------------------------------------------#
# Created by: Théo Petit
# Date: 15/09/2022
# Version: 2.0
#--------------------------------------------------#
"""
This script can be used too keep track of any vulnerability on a project.
Please see README.md for more informations.

Usage :
    python3 cve-report-generator path/to/your/conf.yml
"""

import sys
import yaml
from src.Printer import Printer


if __name__ == "__main__":

    # Check if there is the right number of arguments.
    try:
        if len(sys.argv) != 2:
            raise IndexError
        path_to_conf = sys.argv[1]

        with open(path_to_conf, 'r') as stream:
            conf = yaml.safe_load(stream)

    except Exception as e:
        e_type = type(e)
        print(__doc__)
        print()
        if e_type is FileNotFoundError:
            Printer.printError(e_type.__name__ + ": The file cannot be found at the specified path.")
        elif e_type is IndexError:
            Printer.printError(e_type.__name__ + ": You need to give the path of your conf as the sole argument.")
        else:
            Printer.printError(e_type.__name__ + ': ' + str(e))
        print()
        exit(1)

    # Print title of script
    Printer.printTitle("cve report generator")

    # Print conf data
    print("Name of the projet: " + Printer.boldText(Printer.blueText(conf["Project Name"])))
    print("CVSS Environment Vector: " + Printer.boldText(Printer.blueText(conf["CVSS Environment Vector"])))
    print("Number of dependencies: " + Printer.boldText(Printer.blueText(str(len(conf["COTS"])))))

    # TODO: study
