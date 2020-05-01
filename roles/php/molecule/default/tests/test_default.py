"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_php_packages(host):
    assert host.package("php-intl")
    assert host.package("php-mbstring")
    assert host.package("php-xml")
    assert host.package("php-apcu")
    assert host.package("php-intl")
