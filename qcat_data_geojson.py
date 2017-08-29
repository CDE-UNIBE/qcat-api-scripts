from scripts.base import ArgParser
from scripts.data_geojson import QcatDataGeojson


if __name__ == '__main__':

    desc = 'Extract data from the QCAT API and save it as a Geojson file. A ' \
           'configuration file is required.'

    args = ArgParser(description=desc).parse()

    QcatDataGeojson(args).handle()
