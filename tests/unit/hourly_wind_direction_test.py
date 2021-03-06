from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyWindDirection


class HourlyWindDirectionTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_wind_direction_location')
        self.adapter.register_uri('GET', '/hourly-wind-direction/35/-97',
                                  json=json)
        okc_wd = HourlyWindDirection.location(35, -97)
        self.assertEqual(len(okc_wd.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_wind_direction_asset')
        self.adapter.register_uri('GET', '/hourly-wind-direction/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_wd = HourlyWindDirection.asset('fe68c33d-e718-4449-acae-351072ce7749')
