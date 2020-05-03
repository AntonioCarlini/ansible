"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_programs(host):
    assert host.exists("vmplayer")
    assert host.exists("vmware-collect-host-support-info")
