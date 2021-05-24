import subprocess


path = "/home/dinesh/cases/2021/May/123456"

# pathlist = path.split("/")
# pathlist_after_case = pathlist[-3:]
# # print(pathlist_after_case)
# str1 = "\\"
# windows_after_case_path = str1.join(pathlist_after_case)

# windows_case_path = "C\:\\Users\\dmali\\OneDrive - DDN Storage\\Cases"

# win_case_path = windows_case_path +  windows_after_case_path
# print(win_case_path)

output = subprocess.getoutput(f"wslpath -w {path}")
# print(output)
# subprocess.getoutput("`explorer.exe {output}")
subprocess.run (['explorer.exe', output], stdout=subprocess.PIPE)
p1 = subprocess.Popen(["echo", output], stdout=subprocess.PIPE)
subprocess.run(["clip.exe"], stdin=p1.stdout)
# process_name = "sh"
# ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
# output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
# subprocess.run (['clip.exe'], stdin=)

