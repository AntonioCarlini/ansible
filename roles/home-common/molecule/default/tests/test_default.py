"""Role testing files using testinfra."""

import re

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_home_common_packages_installed(host):
    assert host.package("munin-node").is_installed
    assert host.package("nano").is_installed
    assert host.package("openssh-server").is_installed

def test_home_common_sudo_ok(host):
    assert host.file("/etc/ssh/sshd_config").contains('PermitRootLogin no')

def test_home_common_timezone_ok(host):
    timezone_op = host.check_output("timedatectl")
    assert re.search(r"Europe/London", timezone_op ) is not None

def test_home_common_locale_ok(host):
    all_generated_locales = host.check_output("locale -a")
    assert re.search(r"en_GB.utf8", all_generated_locales) is not None
