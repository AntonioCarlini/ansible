"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_ntp_packages(host):
    assert host.package("ntp").is_installed
    assert host.package("ntpstat").is_installed
