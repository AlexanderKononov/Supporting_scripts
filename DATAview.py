import numpy as np
import fnmatch, glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 

from scipy.interpolate import interp1d 
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D


from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import sys

####################################################################################
# utility functions
####################################################################################

def get_data(fname, chrs=None):
    '''
    '''
    if chrs is not None:
        chrs = [str(chr) for chr in chrs]
    with open(fname,'r') as fh:
        # determine file format and specify loading function
        if fname.split('.')[-2].startswith(('cna','baf','snv','mean-tcn')):
            data = [l.replace('\n','').split() for l in fh.readlines() if (chrs is None or l.split()[0] in chrs) and l[0] != '#']
            data = np.array(data,dtype=float)
            chromosomes = np.sort(np.unique(data[:,0]))
            data = {chr : data[data[:,0]==chr,1:] for chr in chromosomes}
            return data
        elif fname.split('.')[-2].startswith(('subclone','posterior')):
            data = [l.replace('\n','').split() for l in fh.readlines() if (chrs is None or l.split()[0] in chrs) and l[0] != '#']
            post = np.array(data[2:],dtype=float)
            chromosomes = np.sort(np.unique(post[:,0]))
            post = {chr : post[post[:,0]==chr,1:] for chr in chromosomes}
            return [data[0], data[1], post]
        else:
            print 'unsupported file format'            
            return None

def plot_raw(ax,sample,data,bias_func=None):#tcn
    '''
    '''
    x = data[:,0]
    y = data[:,2*sample+1] / data[:,2*sample+2]
    if bias_func is not None:
        y = y / bias_func(x)
    ax.plot(x, y, '.', color='gray', alpha=0.3)

'''
def plot_gof(ax,sample,data,tcn,bias_func=None):
    x = data[:,0]
    y = data[:,2*sample+1] / data[:,2*sample+2]
    if bias_func is not None:
        y = y / bias_func(x)
    ax.plot( x, y, '.', color='gray', alpha=0.3)
    lines = [Line2D([seg[0],seg[2]],[seg[sample+3],seg[sample+3]],color='red',alpha=0.9,lw=3) for seg in tcn]
    for line in lines:
        ax.add_line(line)
        pass
    ax.yaxis.grid(True)
'''

####################################################################################

arg=sys.argv

raw = {"CNA" : get_data(arg[1]),
       "BAF" : get_data(arg[2]),
       "SNV" : get_data(arg[3])}
labels = ["Read depth", "B-allele frequency", "SNV frequency"]

n_samples = len(raw)
n_chr = len(raw["CNA"])

gs = GridSpec(n_samples, n_chr)
fig = plt.figure(figsize=(20,8))

ax_gof = []

for key in raw:
    i = raw.keys().index(key)
    axes = [fig.add_subplot(gs[i,0])]
    for j in range(1,n_chr):
        axes.append(fig.add_subplot(gs[i,j], sharey=axes[0]))
    ax_gof.append(axes)

for key in raw:
    i = raw.keys().index(key)
    for j,chr in enumerate(raw[key]):
        plot_raw(ax_gof[i][j], 0, raw[key][chr])

        # label and rescale x-axis
        scale = 1e3      
        ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale))   
        ax_gof[i][j].xaxis.set_major_formatter(ticks)
        if i==0:
            ax_gof[i][j].set_title("Chromosome %i"%chr, fontsize=14)
        elif i==(len(raw)-1):
            ax_gof[i][j].set_xlabel("Coordinate (kb)", fontsize=14)
        
        # customize limits of (x,y)-axes
        if key=="BAF":
            ax_gof[i][j].set_ylabel("B-allele frequency", fontsize=12)
            ax_gof[i][j].set_ylim([0, 1])
        elif key=="CNA":
            ax_gof[i][j].set_ylabel("Read depth", fontsize=12)
        elif key=="SNV":
            ax_gof[i][j].set_ylabel("SNV frequency", fontsize=12)
            ax_gof[i][j].set_ylim([0, 1])
            
left = 0.02
bottom = 0.02
right = 1.0 - left
top = 1.0 - bottom
gs.tight_layout(fig,rect=[left,bottom,right,top],h_pad=1,w_pad=1)
plt.savefig('dataFig', fmt='pdf')
plt.show()