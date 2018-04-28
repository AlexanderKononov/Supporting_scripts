import numpy as np
import fnmatch, glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 

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



####################################################################################

arg=sys.argv
arg[1]=arg[1].split('.cna.subclone')[0]

####################################################################################

cnafiles = glob.glob(arg[1]+".cna.subclone-?.txt")

fig, axes = plt.subplots(len(cnafiles), figsize=(20, 5), facecolor='w', edgecolor='k', sharex=True, sharey=True)

for sc,cnafile in enumerate(cnafiles):
    [cn, freq, post] = get_data(cnafile)
    
    ax = axes[sc]
    
    data = post[1][:,3:].T
    x = post[1][:,0]
    y = np.arange(data.shape[0] + 1)
    
    im = ax.pcolor(x, y, data, cmap=plt.cm.BuGn)

    # remove blank columns
    ax.set_xlim( (x.min(), x.max()) )
    ax.set_ylim( (y.min(), y.max()) )
    
    # set ticks
    scale = 1e3   # label and rescale x-axis   
    ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale))   
    ax.xaxis.set_major_formatter(ticks)
    
    ax.set_yticks(np.arange(data.shape[0]) + .5)
    ax.set_yticklabels(y)
    
    # set title and axes labels
    if ax.is_first_row():
        ax.set_title("Subclone-specific total copy number", fontsize=14)
    if ax.is_last_row():
        ax.set_xlabel('Coordinate (kb)', fontsize=12)
    ax.set_ylabel("subclone %i"%int(sc+1), fontsize=10) # label by subclone number
    # set common labels
    fig.text(0.1, 0.5, 'Copy number', fontsize=12, ha='center', va='center', rotation='vertical')

# add colorbar
cax = inset_axes(ax, width='1%', height='100%', loc=3,
                 bbox_to_anchor=(1.025, 0., 1, 1),
                 bbox_transform=ax.transAxes,
                 borderpad=0)
cbar = plt.colorbar(im, cax=cax, format='%.1f')
cbar.ax.set_title('Posterior\n probability', ha='center', fontsize=10)
cbar.ax.tick_params(labelsize=10)
cbar.outline.set_visible(False)

plt.savefig(arg[1]+'CNA.pdf')
plt.show()

####################################################################################

baffiles = glob.glob(arg[1]+".baf.subclone-?.txt")

fig, axes = plt.subplots(len(baffiles), figsize=(20, 5), facecolor='w', edgecolor='k', sharex=True, sharey=True)

for sc,baffile in enumerate(baffiles):
    [baf, freq, post] = get_data(baffile)
    ax = axes[sc]
    
    data = post[1][:,3:].T
    x = post[1][:,0]
    y = np.arange(data.shape[0] + 1)
    
    im = ax.pcolor(x, y, data, cmap=plt.cm.PuBu)
    
    # remove blank columns
    ax.set_xlim( (x.min(), x.max()) )
    ax.set_ylim( (y.min(), y.max()) )
    
    # set ticks
    scale = 1e3   # label and rescale x-axis   
    ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale))   
    ax.xaxis.set_major_formatter(ticks)
    
    ax.set_yticks(np.arange(data.shape[0]) + .5)
    ax.set_yticklabels(y)

    # set title and axes labels
    if ax.is_first_row():
        ax.set_title("Subclone-specific minor copy number", fontsize=14)
    if ax.is_last_row():
        ax.set_xlabel('Coordinate (kb)', fontsize=12)
    ax.set_ylabel("subclone %i"%int(sc+1), fontsize=10) # label by subclone number
    # set common labels
    fig.text(0.1, 0.5, 'Copy number', fontsize=12, ha='center', va='center', rotation='vertical')

# add colorbar
cax = inset_axes(ax, width='1%', height='100%', loc=3,
                 bbox_to_anchor=(1.025, 0., 1, 1),
                 bbox_transform=ax.transAxes,
                 borderpad=0)
cbar = plt.colorbar(im, cax=cax, format='%.1f')
cbar.ax.set_title('Posterior\n probability', ha='center', fontsize=10)
cbar.ax.tick_params(labelsize=10)
cbar.outline.set_visible(False)

plt.savefig(arg[1]+'BAF.pdf')
plt.show()
