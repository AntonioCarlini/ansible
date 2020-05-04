"""Role testing files using testinfra."""


def test_virtualbox_packages(host):
    assert host.package("noise")
