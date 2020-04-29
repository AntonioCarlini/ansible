"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_jp_packages_installed(host):
    assert host.package("ibus-anthy").is_installed
    assert host.package("ruby").is_installed
    assert host.exists("sass")
