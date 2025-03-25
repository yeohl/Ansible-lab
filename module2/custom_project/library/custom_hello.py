#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        message='Hello, {0}'.format(module.params['name'])
    )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()