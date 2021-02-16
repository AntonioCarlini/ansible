"""Role testing files using testinfra."""

# Debian-based systems store libreoffice7.1 in /usr/local/bin
# RedHat-based systems store libreoffice7.1 in /usr/bin
def test_libreoffice_file_installed(host):
    assert (host.file("/usr/local/bin/libreoffice7.1").exists) or (host.file("/usr/bin/libreoffice7.1").exists)
