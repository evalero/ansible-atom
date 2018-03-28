import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_atom_installed(host):
    if (str(host.system_info.distribution) == 'debian' or
            str(host.system_info.distribution) == 'ubuntu'):
        f = host.file('/usr/bin/atom')
    else:
        f = host.file('/bin/atom')
    assert f.exists
