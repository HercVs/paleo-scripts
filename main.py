import sys
from qap import qap_build
from util import *

if __name__ == "__main__":
    data_input_filepath = sys.argv[1]
    data_output_filepath = sys.argv[2]

    data_raw = load_from_csv(data_input_filepath)
    data_percent = to_percentages(data_raw)
    qap_build(data_percent).savefig(data_output_filepath)