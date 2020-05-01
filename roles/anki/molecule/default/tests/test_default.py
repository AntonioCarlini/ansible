"""Role testing files using testinfra."""


def test_anki_packages_installed(host):
    assert host.file("/usr/local/bin/anki").exists
