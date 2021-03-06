#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_actiongroupconfig
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of ActionGroupConfig Avi RESTful Object
description:
    - This module is used to configure ActionGroupConfig object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    action_script_config_ref:
        description:
            - Reference of the action script configuration to be used.
            - It is a reference to an object of type alertscriptconfig.
    autoscale_trigger_notification:
        description:
            - Trigger notification to autoscale manager.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
    description:
        description:
            - User defined description for the object.
    email_config_ref:
        description:
            - Select the email notification configuration to use when sending alerts via email.
            - It is a reference to an object of type alertemailconfig.
    external_only:
        description:
            - Generate alert only to external destinations.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        required: true
    level:
        description:
            - When an alert is generated, mark its priority via the alert level.
            - Enum options - ALERT_LOW, ALERT_MEDIUM, ALERT_HIGH.
            - Default value when not specified in API or module is interpreted by Avi Controller as ALERT_LOW.
        required: true
    name:
        description:
            - Name of the object.
        required: true
    snmp_trap_profile_ref:
        description:
            - Select the snmp trap notification to use when sending alerts via snmp trap.
            - It is a reference to an object of type snmptrapprofile.
    syslog_config_ref:
        description:
            - Select the syslog notification configuration to use when sending alerts via syslog.
            - It is a reference to an object of type alertsyslogconfig.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create ActionGroupConfig object
  avi_actiongroupconfig:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_actiongroupconfig
"""

RETURN = '''
obj:
    description: ActionGroupConfig (api/actiongroupconfig) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible.module_utils.network.avi.avi import (
        avi_common_argument_spec, HAS_AVI, avi_ansible_api)
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        action_script_config_ref=dict(type='str',),
        autoscale_trigger_notification=dict(type='bool',),
        description=dict(type='str',),
        email_config_ref=dict(type='str',),
        external_only=dict(type='bool', required=True),
        level=dict(type='str', required=True),
        name=dict(type='str', required=True),
        snmp_trap_profile_ref=dict(type='str',),
        syslog_config_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'actiongroupconfig',
                           set([]))

if __name__ == '__main__':
    main()
