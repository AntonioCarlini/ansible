Role Name
=========

Prepares the specified target host in order that it may be managed by ansible in the future.

Requirements
------------

* A privileged account and password combination is required on the target. root will be used
* python must be installed in /usr/bin/python
  If it is not, then try 'apt install -y python-minimal'
* ssh server must be installed and running

Actions
-------

* Sets up a user for ansible to use when managing the system. By default this user will be ansible-admin.

Role Variables
--------------

* user_name
* user_shell /bin/bash
* user_local_ssh_key_path: "~/.ssh/id_rsa.pub"
* user_enable_passwordless_sudo: True

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache v2.0

Author Information
------------------

antonio@acarlini.com
