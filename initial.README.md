This playbook prepares a new target so that it can be managed by ansible.

To run this playbook an account, USER, on the remote system needs to be available and its password needs to be known.

Future playbooks will rely on the user setup by this script (ansibleadmin by default).

ansible-playbook initial.yml -u USER --ask-pass --ask-become-pass -i IPADDRESS,

# Note: the trailing comma in that line is NOT an accident!
