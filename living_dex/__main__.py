
import os
import sys
import getopt
import logging
from .parser import parse


def usage():
    """Help documentation."""
    print(
        f"\nusage: routes_finder [-v] [-h] [--verbose] [--help] "
        f"[--input=<Input-File>] [--output=<Output-File>]\n"
        f"\nOptions:\n"
        f"\t-v, --verbose\t\tVerbose\n"
        f"\t-h, --help\t\tHelp\n"
        f"\t--input\t\t\tFilename\n"
        f"\t--output\t\tFilename\n"
        f"\t--locations\t\tCSV File\n"
        f"\t--trips\t\t\tCSV File\n"
        f"\t--results\t\tInteger\n"
        f"\nArguments:\n"
        f"\tInput-File: Text file containing the origin & destination input (Default: data/dex.json).\n"
        f"\tOutput-File: Filename and path where to output the results (Default: data/output.txt).\n"
    )


def main():
    """Find all routes between two nodes in a unidirectional graph."""
    # Check the user CLI input matches correct syntax
    try:
        # Specify the valid CLI options/arguments
        opts, _ = getopt.getopt(
            sys.argv[1:],
            "hv",
            [
                "help",
                "verbose",
                "input=",
                "output=",
            ],
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # Define input arguments and initialize default values.
    input_file = "data/dex.json"
    output_file = "data/output.txt"

    # Loop through all the User CLI options/arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
        elif opt == "--input":
            input_file = arg

            if not os.path.exists(input_file):
                sys.exit("Could not find input file")
        elif opt == "--output":
            output_file = arg

    parse(input_file, output_file)


if __name__ == "__main__":
    main()