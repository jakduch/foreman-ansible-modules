import sys

from plugins.module_utils import foreman_helper

sys.modules['ansible_collections.theforeman.foreman.plugins.module_utils.foreman_helper'] = foreman_helper

from plugins.modules.registration_command import _format_packages


def test_packages_list_is_converted_to_space_delimited_string():
    assert _format_packages(['foreman_scap_client_bash', 'katello-host-tools-tracer']) == (
        'foreman_scap_client_bash katello-host-tools-tracer'
    )


def test_packages_string_is_preserved():
    packages = 'foreman_scap_client_bash katello-host-tools-tracer'

    assert _format_packages(packages) == packages
