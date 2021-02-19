"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_collaboration_packages_installed(host):
    assert host.package("skypeforlinux").is_installed
    assert host.package("slack-desktop").is_installed
    assert host.package("teams").is_installed
    assert host.package("zoom").is_installed
