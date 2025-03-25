#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='')
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    path = module.params['path']
    content = module.params['content']
    result = dict(changed = False)
    
    if module.check_mode:
        module.exit_json(**result)
    
    try:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
            result['msg'] = f"{path} 파일이 생성되었습니다."
        else:
            result['msg'] = f"{path} 파일이 이미 존재합니다."

    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)

def main():
    run_module()
    
if __name__ == '__main__':
    main()