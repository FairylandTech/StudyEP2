import pkg_resources
import subprocess

c_pip_pkg = 0
pip_list = []
for pip_list_index in pkg_resources.working_set:
    pip_list.append(pip_list_index)
for pkg_name_version in pip_list:
    c_pip_pkg += 1
    pkg_name = pkg_name_version.project_name
    # print(f'{c_pip_pkg}: {pkg_name_version}')
    subprocess.call(f'pip install --upgrade {pkg_name}', shell=True)
# print(c_pip_pkg)

    
