
# coding: utf-8

# In[3]:


import os
import sys
import git
import shutil
import argparse


# In[5]:


get_ipython().run_line_magic('pinfo', 'metavar')


# In[ ]:


parser = argparse.ArgumentParser()
parser.add_argument('dir_name', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')


# In[ ]:


#To clone Git Repo

# dir_name = "temp"
# remote_url = "https://github.com/kmbond/loki_1.git/"

# if os.path.isdir(dir_name):
#     shutil.rmtree(dir_name)
    
# os.mkdir(dir_name)
# print("In process")

# repo = git.Repo.init(dir_name)
# origin = repo.create_remote('origin',remote_url)
# print("Added remote")
# print("Fetching")
# origin.fetch()
# print ("Fetching complete")
# origin.pull(origin.refs[0].remote_head)
# print ("---Done---")

