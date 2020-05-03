Role Name
=========

mysql

Installs a MySQL database, currently mariadb.

An admin account is added, by default this will be 'mysql_admin'.
The admin account password can be changed by setting the variable mysql_admin_password.

Requirements
------------

None.

Role Variables
--------------

mysql_admin_user: An account that is set up to be the MySQL admin.

mysql_admin_password: The password for the MySQL admin account. A default is used, so be sure to change it.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all
      roles:
         - role: mysql

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
