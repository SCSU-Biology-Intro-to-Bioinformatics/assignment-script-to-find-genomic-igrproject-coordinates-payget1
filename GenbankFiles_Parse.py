
# coding: utf-8

# In[128]:


from Bio.Seq import Seq
from Bio import SeqIO 
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
from Bio.Alphabet import IUPAC
import sys
import Bio
import pandas as pd 
from Bio.SeqFeature import FeatureLocation
import numpy as np
import re


parser = argparse.ArgumentParser(description='A toy example.')

parser.add_arugment('-gb', '--genbank_file', required=True, dest='genbank', type=str, help='Input .gb file.')

args = parser.parse_args()

genome = SeqIO.read(args.genbank, "genbank")


#Code displays the record of the genbank file
print (record)


# In[131]:


# Reads the genbank file  and extracts data
genome = SeqIO.read('GenbankFile.gb','genbank')


# In[132]:


#list genbank file features
genome.features


# In[133]:


#Strings genome features
feature = str(genome.features)


# In[134]:


#Displays features
feature


# In[135]:


#seperates genome features & makes it readable to userS
gene_features = re.findall(r'SeqFeature\SFeatureLocation\SExactPosition\S\d{1,60}\S\S\sExactPosition\S\d{1,60}\S\S\sstrand=\d{1,60}\S\S\stype\S', features)


# In[136]:


gene_features 


# In[137]:


position_of_gene = str(position_of_gene)


# In[138]:


re.findall(r'\d{1,60}', position_of_gene)
list_of_gene = re.findall(r'\d{1,60}', position_of_gene)


# In[139]:


#Position of genes extracted
list_of_gene


# In[140]:


#start codon extracted
start = list_of_gene[::2]
start


# In[141]:


#stop codon extracted
stop = list_of_gene[1::2]
stop


# In[142]:


#Converts to dataframe
df = pd.DataFrame({'Starts': start})
df['Stops'] = stop
df


# In[143]:


#IGR extracted
names = []
for x in range(1, len(df)+1):
    names.append('IGR_' + str(x))


# In[144]:


#IGR names shown
names


# In[145]:


#add column
df['Names'] = names


# In[146]:


#Displays the names column
df


# In[147]:


#converts dataframe to csv
df.to_csv('IGRproject.csv')

