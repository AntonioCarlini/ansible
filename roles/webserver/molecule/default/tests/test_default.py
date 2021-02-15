"""Role testing files using testinfra."""


def test_webserver_packages_installed(host):
    assert (host.package("apache2").is_installed) or (host.package("httpd").is_installed)
    assert (host.package("libapache2-mod-php").is_installed) or (host.package("php").is_installed)
