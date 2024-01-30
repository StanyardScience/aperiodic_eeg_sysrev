def plot_the_key(which_figure_am_I):
    # defaults for all keys
    m_sd = 0.1
    age = [28.5, 31.5]
    m = [2.4, 2.2, 2.0, 1.8, 1.6]
    colourAlpha = 1
    ellipse_line_width = 1
    defs_pt = {'linestyle': '-','alpha' : colourAlpha}
    defs_ell = {'width': (age[0]-age[1])/2, 'angle' : 0, 'lw' : ellipse_line_width,
                   'fill' : False, 'alpha' : colourAlpha} 
    # and specific mappings per figure key
    if which_figure_am_I == '2a' or which_figure_am_I =='2A':
        rect = Rectangle((26.8, 1.45), 4.9, 1.2, fill=None, edgecolor='black', linestyle=(0,(3,1,1,1)), linewidth=2)
        ax.add_patch(rect)
        # AE FOOOF-AE IRASA-PaWN Extra-PLE-Converted HE
        col = ['#E69F00', '#2271B2', '#F748F5', '#000000', '#920000']
        descr = ['FOOOF', 'IRASA','PaWN Extra','PLE','Converted HE']
        print(f"Length of col: {len(col)}")
        for i in range(0, 5):
#             print(f"Iteration: {i}, {col[i]}, type = {type(col[i])}")
#             print(f"Iteration: {i}, m[i]: {m[i]}, col[i]: {col[i]}, type(col[i]): {type(col[i])}")
            ax.plot([29.25, 30.75],[m[i],m[i]],color=col[i],**defs_pt)
            ax.plot([30,30],[(m[i]-0.1),(m[i]+0.1)],color=col[i],**defs_pt) # override prior call for brevity
            ell = Ellipse(xy=[30,m[i]], height=m_sd*2, **defs_ell, edgecolor = col[i])
            ax.add_artist(ell)   
            ax.annotate(descr[i], (28.05, m[i]), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=11.5)
            
            ax.annotate('Key', (28.2, 2.55), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=16,weight='bold')
            
    elif which_figure_am_I == '2b' or which_figure_am_I =='2B':
        rect = Rectangle((26.8, 2.05), 4.9, 0.6, fill=None, edgecolor='black', linestyle=(0,(3,1,1,1)), linewidth=2)
        ax.add_patch(rect)
        col = ['#F4631E','#007E7E'] # orange, teal
        descr = ['EOR/Sleep', 'ECR']
        defs_ell = {'width': (age[0]-age[1])/2, 'angle' : 0, 'lw' : ellipse_line_width,
                   'fill' : False, 'alpha' : colourAlpha} 
        ls_opts = ['dashed', 'solid']
        print(f"Length of col: {len(col)}")
        for i in range(0, 2):
#             print(f"Iteration: {i}")
            ax.plot([29.25, 30.75],[m[i],m[i]],color=col[i],alpha=colourAlpha) # override prior call for brevity
            ax.plot([30,30],[(m[i]-0.1),(m[i]+0.1)],color=col[i],**defs_pt) # override prior call for brevity
            ell = Ellipse(xy=[30,m[i]], height=m_sd*2, **defs_ell, linestyle=ls_opts[i], edgecolor = col[i])
            ax.add_artist(ell)   
            ax.annotate(descr[i], (28.05, m[i]), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=11.5)
        ax.annotate('Key', (28.2, 2.55), textcoords="offset points", 
                    xytext=(0,-2.2), ha='center',fontsize=16,weight='bold')
    elif which_figure_am_I == '3a' or which_figure_am_I == '3A':
        rect = Rectangle((26.8, 2), 4.9, 0.65, fill=None, edgecolor='black', linestyle=(0,(3,1,1,1)), linewidth=2)
        ax.add_patch(rect)
        col = ['#AD0000', '#359B73'] # red, green
        descr = ['Global', 'Regional']
        defs_ell = {'width': (age[0]-age[1])/2, 'angle' : 0, 'lw' : ellipse_line_width,
                   'fill' : False, 'alpha' : colourAlpha} 
        ls_opts = ['solid', 'dashed']
        print(f"Length of col: {len(col)}")
        for i in range(0,2):
#             print(f"Iteration: {i}")
            ax.plot([29.25, 30.75],[m[i],m[i]],color=col[i],alpha=colourAlpha) # override prior call for brevity
            ax.plot([30,30],[(m[i]-0.1),(m[i]+0.1)],color=col[i],**defs_pt) # override prior call for brevity
            ell = Ellipse(xy=[30,m[i]], height=m_sd*2, **defs_ell, edgecolor = col[i],linestyle=ls_opts[i])
            ax.add_artist(ell)   
            ax.annotate(descr[i], (28.05, m[i]), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=11.5)
        ax.annotate('Key', (28.2, 2.55), textcoords="offset points", 
                    xytext=(0,-2.2), ha='center',fontsize=16,weight='bold')
    elif which_figure_am_I == '3b' or  which_figure_am_I == '3B':
        print(f'For {which_figure_am_I} there is no key required.')
    elif which_figure_am_I == 'SIIIa' or which_figure_am_I == 'S3a' or which_figure_am_I == 'S3A' or which_figure_am_I =='SIIIA':
        rect = Rectangle((26.8, 1.8), 4.9, .9, fill=None, edgecolor='black', linestyle=(0,(3,1,1,1)), linewidth=2)
        ax.add_patch(rect)
        # AE FOOOF-AE IRASA-PaWN Extra-PLE-Converted HE
        col = ['#E69F00', '#000000', '#920000']
        descr = ['FOOOF', 'PLE','Converted HE']
        print(f"Length of col: {len(col)}")
        for i in range(0, 3):
#             print(f"Iteration: {i}, {col[i]}, type = {type(col[i])}")
#             print(f"Iteration: {i}, m[i]: {m[i]}, col[i]: {col[i]}, type(col[i]): {type(col[i])}")
            ax.plot([29.25, 30.75],[m[i],m[i]],color=col[i],**defs_pt)
            ax.plot([30,30],[(m[i]-0.1),(m[i]+0.1)],color=col[i],**defs_pt) # override prior call for brevity
            ell = Ellipse(xy=[30,m[i]], height=m_sd*2, **defs_ell, edgecolor = col[i])
            ax.add_artist(ell)   
            ax.annotate(descr[i], (28.05, m[i]), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=11.5)
            
            ax.annotate('Key', (28.2, 2.55), textcoords="offset points", 
                        xytext=(0,-2.2), ha='center',fontsize=16,weight='bold')
    else: 
        print(f'Entry: {which_figure_am_I} is not in the preset list of 2a, 2b, 3a, 3b, SIIIA/SIIIa/S3A/S3a. Please verify the input')
