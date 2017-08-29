from scripts.base import ArgParser
from scripts.data_csv import QcatDataCsv


if __name__ == '__main__':

    desc = 'Extract data from the QCAT API and save it as a CSV file. A ' \
           'configuration file is required.'

    args = ArgParser(description=desc).parse()

    QcatDataCsv(args).handle()
