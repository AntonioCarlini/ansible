"""Role testing files using testinfra."""


def test_virtualbox_packages(host):
    assert host.package("noise")

def test_virtualbox_packages(host):
    assert host.file("/usr/bin/keepassx").exists
