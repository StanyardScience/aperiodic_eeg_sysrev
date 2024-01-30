#GenCode: OLap8p11 
def build_a_box_overlapping_3B(data,colour, stage, studyName,age_min=None, age_max=None):
    # input structure was [EXPONENT, SD, MEAN_AGE, SD_AGE, N_SAMPLE]
    global studyNum
    studyNum += 1
    age = data[2]
    age_sd = data[3] 
    measure_m = data[0]
    measure_sd = data[1]
    n = data[4]
    if stage == 'inf':
        colour = '#4169e1'
    elif stage == 'toddler':
        colour = '#ff1493'
    elif stage == 'child':
        colour = '#228b22'
    elif stage == 'adol':
        colour = '#2E8857'
    elif stage == 'ya':
        colour = '#D35400'
    else:
        print(f'{stage} is not inf/toddler/child/adol/ya...')
    # set marker based on n
    if n < 15:
        markerChoice = 'o'
        colourAlpha=0.2
    elif 15 < n < 30:
        markerChoice = '^'
        colourAlpha=0.4
    elif 30 < n < 50:
        markerChoice = 's'
        colourAlpha=0.6
    elif 50 < n < 100:
        markerChoice = 'p'
        colourAlpha=0.8
    else: 
        markerChoice = 'h'
        colourAlpha=1.0
        
    if 'ECR' in studyName or 'Sleep' in studyName:
        ellipse_line_width = 1.5
        lineStyle = 'dashed'
    else:
        ellipse_line_width = 1
        lineStyle = 'solid'
    # Plot mean ± SD as boxplots
    ax.plot(age, measure_m, color=colour, label=studyName, marker=markerChoice, markersize=12, alpha=colourAlpha)
    if colourAlpha > 0.2:
        ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='w')
    else:
        ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='black')
    if isinstance(measure_sd, float):
        ax.plot([age, age], [measure_m - measure_sd, measure_m + measure_sd],
                        color=colour,alpha=colourAlpha)
    if isinstance(age_sd, float):
        ax.plot([age - age_sd, age + age_sd],[measure_m,measure_m],color=colour, alpha=colourAlpha)
    if isinstance(measure_sd, float) and isinstance(age_sd,float):
        ell = Ellipse(xy=[age,measure_m], width=age_sd*2, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha, linestyle=lineStyle)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and ('Schaworonkow & Voytek' in studyName):
        ell = Ellipse(xy=[age,measure_m], width=0.06, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=0.5, fill=False)
        ax.add_artist(ell)

fig, ax = plt.subplots(1,1,figsize=(10,8))
axMin = 0.70
axMax = 2.35
legendFontSize=7
studyNum = 0

### Infants ###
build_a_box_overlapping_3B(CARTER_LENO_2022_group_infant_AE_EORvids,'#6F8FAF',
           'inf', 'Carter Leno 2022 G EOR Mixed',None,None)

### MANUAL EXTRACT OF GLOBAL APERIODIC ###
build_a_box_overlapping_3B(KARALUNAS_2022_inf_AE_EOR,'#6F8FAF',
           'inf', 'Karalunas 2022 Inf G EOR ',None,None)
build_a_box_overlapping_3B(SCH_VOY_2021_group_AE_40D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (40d)',None, None)
build_a_box_overlapping_3B(SCH_VOY_2021_group_AE_69D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (69d)',None, None)
build_a_box_overlapping_3B(SCH_VOY_2021_group_AE_96D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (96d)',None, None)

#CHILD
build_a_box_overlapping_3B(PEISCH_ARNETT2022_group_gAE_EO,'#00cc99',
            'child','Peisch & Arnett 2022 G EOR',None,None)
build_a_box_overlapping_3B(ROBERTSON2019_group_gAE_EO,'#228b22',
            'child','Robertson 2019 G EOR',None, None)
build_a_box_overlapping_3B(WILKINSON2021_group_gAE_EO,'#008736',
            'child','Wilkinson 2021 G EOR',None, None)
build_a_box_overlapping_3B(HILL2022_group_gAE_EO, '#177245',
            'child','Hill 2022 G EOR', None,None)
build_a_box_overlapping_3B(McSweeney2021_child_group_gEO, '#2E8857',
            'child','McSweeney 2021 G EOR', None,None)

## ADOLESCENTS
build_a_box_overlapping_3B(McSweeney2021_adol_group_gEO, '#CC7722',
            'adol','McSweeney 2021 G EOR', None,None)
build_a_box_overlapping_3B(OSTLUND2021_group_AE_EO, '#C49102',
            'adol','Ostlund 2021 G EOR', None,None)
build_a_box_overlapping_3B(KARALUNAS_2022_adol_AE_EOR, '#C49102',
            'adol','Karalunas 2022 Adol G EOR', None,None)

# ### Young Adult ###
build_a_box_overlapping_3B(PATHANIA_2021_ya_gAE_EOR, '#FBEEE6',
            'ya','Pathania 2021 G EOR', None,None)
build_a_box_overlapping_3B(KE2022_ya_gAE_EO, '#873600',
            'ya','Ke 2022 G EOR', None,None)
build_a_box_overlapping_3B(BARRY_DE_BLASIO_2021_ya_gPN_EO, '#BF360C',
            'ya','Barry & De Blasio 2021 G EOR', None,None)
build_a_box_overlapping_3B(PATHANIA_2022_ya_gAE_ECR, '#FBEEE6',
            'ya','Pathania 2022 G ECR', None,None)

# Create a separate legend for the markers relating to n per study
markers_legend_labels = ['n < 15', 
                         '15 < n < 30', 
                         '30 < n < 50', 
                         '50 < n < 100', 
                         'n > 100']
markers_legend_handles = []
#marker_colours = ['#B71C1C', '#D35400', '#CC7722', '#003300', '#6F8FAF']
marker_colours = ['black','black','black','black','black']# Specify the colors of the markers

for marker, color in zip(['o', '^', 's', 'p', 'h'], marker_colours):
    markers_legend_handles.append(plt.Line2D([], [], marker=marker, markersize=legendFontSize*1.5, linestyle='None', color=color))

markers_legend = fig.legend(markers_legend_handles,
                              markers_legend_labels,
                              fontsize=legendFontSize*1.5,
                              loc='lower center', 
                              title='Markers',
                              bbox_to_anchor=(0.70, -0.12)) #ncol = 5 
markers_legend.get_title().set_fontweight('bold')
for text in markers_legend.get_texts():
    text.set_fontsize(legendFontSize*0.8)

studyList_G_R = ['Carter Leno 2022 G EOR Mixed',
                 'Karalunas 2022 Inf G EOR',
                 'Schaworonkow and Voytek 2021 40d G EOR Mixed',
                 'Schaworonkow and Voytek 2021 69d G EOR Mixed',
                 'Schaworonkow and Voytek 2021 96d G EOR Mixed',  
                 'Peisch & Arnett 2022 G EOR', 
                 'Robertson 2019 G EOR', 
                 'Wilkinson 2021 G EOR', 
                 'Hill 2022 G EOR',  
                 'McSweeney 2021 Child G EOR', 
                 'McSweeney 2021 Adol G EOR',  
                 'Ostlund 2021 G EOR', 
                 'Karalunas 2022 Adol G EOR',
                 'Pathania 2021 G EOR',
                 'Barry and de Blasio G EOR',
                 'Ke 2022 G EOR', 
                 'Pathania 2022 G EOR']
from matplotlib.lines import Line2D
study_legend_labels = [f'{i+1}. {label}' for i, label in enumerate(studyList_G_R)]
study_legend_handles = [Line2D([], [], color='none', marker='', linestyle='', label=label)
                        for label in study_legend_labels]
study_legend = fig.legend(handles=study_legend_handles, fontsize=legendFontSize, loc='lower center',
                           title='Studies', bbox_to_anchor=(0.475, -0.12), ncol=3)
study_legend.get_title().set_fontweight('bold')
fig.subplots_adjust(wspace=1)
fig.set_size_inches(20, 8)
fig.text(0.5,0.9, 'Global EOR AE across early development', ha='center',fontsize=25,weight='bold')
fig.text(0.5, 0.04, 'Age (years)', ha='center',fontsize=18,weight='bold')
fig.text(0.08, 0.5, 'Aperiodic exponent ($\mu$V$^2$ Hz$^{-1}$)', 
         va='center', rotation='vertical',fontsize=18, weight='bold')
plt.axvline(x=2, color='black', linestyle='--', alpha=0.5,zorder=0)
plt.xlim(-2, 33)
plt.xticks(range(0, 35, 5))
ax.axvline(x=2, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=3, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=14, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=19, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=26, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.set_xlim(-1, 33)  # Set the x-axis range for the main plot
age_labels = ['Inf', 'Todd', 'Child', 'Adol', 'YA', 'Ext Adult']
age_positions = [0.8, 2.85, 9, 17, 22.5, 30]
for age_label, age_position in zip(age_labels, age_positions):
    ax.text(age_position, 0.7, age_label, color='grey', fontsize=12, ha='right', va='center', zorder=-1, rotation=0)
plt.tick_params(axis='y', labelsize=16)
plt.tick_params(axis='x', labelsize=16)
plot_the_key('3B')
#plt.savefig('/Users/username/Desktop/someFolder/anotherFolder/continuedPath/name3b' 
#            + '.pdf', bbox_inches='tight') 
