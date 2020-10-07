import pytest
from src.ConnectorMT5Profiler import Connection


class Test_ReloadProfiles_True_Url():
    @pytest.fixture(scope='class')
    def setup(self):
        return Connection().ReloadProfile_true_url()

    def test_true_reload_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_true_reload_status_code(self, setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_true_reload_description(self, setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_true_reload_description_value(self, setup):
        print("Service Response : ", setup)
        assert setup["description"] == "Done"

class Test_ReloadProfiles_False_Url():
    @pytest.fixture(scope='class')
    def setup(self):
        return Connection().ReloadProfile_false_url()

    def test_false_reload_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_false_reload_status_code(self, setup):
        print("Service Response : ", setup)
        assert setup["status"] == 3

    def test_false_reload_description(self, setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_false_reload_description_value(self, setup):
        print("Service Response : ", setup)
        assert setup["description"] == "invalid uri"