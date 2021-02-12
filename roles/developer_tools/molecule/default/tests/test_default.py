"""Role testing files using testinfra."""


def test_developer_packages(host):
    assert host.package("emacs").is_installed
    assert host.package("git").is_installed
    assert host.package("python3").is_installed
    assert host.package("code").is_installed
