import json

from scripts.base import QcatApiMixin


class QcatDataGeojson(QcatApiMixin):
    """
    Store QCAT API data as Geojson.
    """

    def read_data(self) -> list:
        """Read a local Geojson file"""
        output_file = self.get_output_file_path()
        try:
            with open(output_file,encoding='utf-8') as geojson_file:
                file_data = geojson_file.read()
        except FileNotFoundError:
            self.log('No existing attribute file found.')
            return []

        try:
            json_data = json.loads(file_data)
        except json.decoder.JSONDecodeError:
            print('Existing attribute file "{output_file}" is not a valid '
                  'geojson file. It is ignored.'.format(
                output_file=output_file))
            return []

        features_by_code = {}
        for feature in json_data.get('features', []):
            properties = feature.pop('properties', {})
            if features_by_code.get(properties['code']):
                # Existing
                feat = features_by_code[properties['code']]
                feature_collection = json.loads(feat['geometry'])
                feature_collection['features'].append(feature)
            else:
                feature_collection = {
                    'type': 'FeatureCollection',
                    'features': [feature],
                }
            properties['geometry'] = json.dumps(feature_collection)
            features_by_code[properties['code']] = properties

        features = list(features_by_code.values())

        self.log('Found existing attribute file "{output_file}" with '
                 '{len_features} entries.'.format(
            output_file=output_file, len_features=len(features)))

        return features

    def write_data(self, data: list) -> None:
        no_geometry_count = 0
        features = []
        for data_json in data:
            geom = data_json.pop('geometry')
            if not geom:
                no_geometry_count += 1
                continue

            for feature in json.loads(geom).get('features', []):
                feature['properties'] = data_json
                features.append(feature)

        feature_collection = {
            'type': 'FeatureCollection',
            'features': features,
        }

        self.log('Skipped {no_geometry_count} questionnaires because they do '
                 'not have a geometry, writing {len_features} features (one '
                 'questionnaire can have multiple features)'.format(
            no_geometry_count=no_geometry_count, len_features=len(features)))

        output_file = self.get_output_file_path()
        with open(output_file, 'w',encoding='utf-8') as geojson_file:
            json.dump(feature_collection, geojson_file)

        print('Output file "{output_file}" written.'.format(
            output_file=output_file))
