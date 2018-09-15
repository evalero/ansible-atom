Atom
=========

A role to install [Atom ide](https://atom.io)  

Role Variables
--------------
* ` gpg_key ` : url to gpg key
* ` atom_repo `: Depending on OS family, change the atom_repo var to point to correct version.
* ` rpm_validate_key `: Uncomment and set to **no** if the target machine is behind a proxy that breaks SSL


Example Playbook
----------------

```
- hosts: localhost
  roles:
    - atom
```
License
-------
GPLv2

Author Information
------------------

Ernesto Valero (evalero@paradigmadigital.com)
