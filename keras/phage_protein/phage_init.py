import os
#cwd = os.getcwd()
path = os.path.abspath(__file__)
root_dir = os.path.dirname(path)
fasta_dir = os.path.join(root_dir, 'fasta')
model_dir = os.path.join(root_dir, 'model')
data_dir =  os.path.join(root_dir, 'data')
fasta_dir_2 = os.path.join(root_dir, 'download_seq/all/clustered/')
