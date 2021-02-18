"""Role testing files using testinfra."""


def test_nvme_cli(host):
    """Validate nvme bin file."""
    nvme = host.file("/usr/sbin/nvme")
    assert nvme.exists

    """Validate nvme hostid file."""
    hostid = host.file("/etc/nvme/hostid")
    assert hostid.exists
    assert hostid.size > 0
