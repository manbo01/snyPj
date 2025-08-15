import random

class DummySensor:
    # set units
    units = {
        "mars_base_internal_temperature": "°C",
        "mars_base_external_temperature": "°C",
        "mars_base_internal_humidity": "%",
        "mars_base_external_illuminance": "W/m²",
        "mars_base_internal_co2": "%",
        "mars_base_internal_oxygen": "%"
    }

    # generate new method / initializing
    def __init__(self): # init : auto call
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }

    # random setting
    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 2)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


if __name__ == "__main__":
    ds = DummySensor()
    ds.set_env()
    result = ds.get_env()
    for key, value in result.items():
        unit = DummySensor.units.get(key, "")
        print(f"{key}: {value} {unit}")