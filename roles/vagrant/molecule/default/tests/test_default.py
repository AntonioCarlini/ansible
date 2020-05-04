"""Role testing files using testinfra."""


def test_vagrant_packages(host):
    assert host.package("vagrant")
