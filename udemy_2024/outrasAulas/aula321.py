import subprocess

# cmd = ['ping', '127.0.0.1', '-c', '4']
# cmd = ['ls', '-lah', '/']
# proc = subprocess.run(cmd, shell=False)

cmd = ['ls -lah /']
proc = subprocess.run(cmd, shell=True)

# print(f'{proc.args=}')
# print(f'{proc.returncode=}')
# print(proc.stdout.decode('utf_8'))
# print(f'{proc.stdout}')
# print(f'{proc.stderr=}')