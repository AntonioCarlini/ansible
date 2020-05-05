"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_ansible_target_prepared(host):
    assert host.user("ansibleadmin").exists
    with host.sudo():
      assert host.file("/etc/sudoers.d/ansibleadmin").exists
      assert host.file("/etc/sudoers").contains("#includedir /etc/sudoers.d")

