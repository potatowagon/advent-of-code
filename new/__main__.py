import shutil
import os

print("Please enter qn name:")
qn_name = input()

this_dir = os.path.dirname(__file__)
sample_runner_path = os.path.join(this_dir, "sample.py")
qn_runner_path = os.path.join(os.getcwd(), f"test_{qn_name}.py")
qn_input_path = os.path.join(os.getcwd(), f"{qn_name}.txt")
print(this_dir, os.getcwd(), qn_name)
#shutil.copy(sample_runner_path, qn_runner_path)

# create input file
with open(qn_input_path, 'w') as fp:
    pass

# Create qn runner
fin = open(sample_runner_path, "rt")
fout = open(qn_runner_path, "wt")
for line in fin:
	fout.write(line.replace('REPLACEME', qn_name))
fin.close()
fout.close()
