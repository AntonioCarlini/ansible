"""Role testing files using testinfra."""


def test_programs(host):
    assert host.exists("vmplayer")
    assert host.exists("vmware-collect-host-support-info")
