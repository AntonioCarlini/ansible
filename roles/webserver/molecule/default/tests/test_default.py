"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_webserver_packages_installed(host):
    assert host.package("apache2").is_installed
    assert host.package("libapache2-mod-php").is_installed

