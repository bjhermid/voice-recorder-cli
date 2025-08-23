from voice_recorder import list_devices, record_wav


# SMOKE TEST JUST MAKE SURE THE FUNC EXIST
def test_list_device():
    devices = list_devices()
    assert isinstance(devices, list)


def test_record_wav():
    assert callable(record_wav)


if __name__ == "__main__":
    test_record_wav()
