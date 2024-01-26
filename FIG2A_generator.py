#GenCode: Figure 2A
fig, ax = plt.subplots(1,1,figsize=(10,8))
axMin = 0.70
axMax = 2.35
legendFontSize=7
studyNum = 0

def build_a_box_overlapping_Fig2A(data,colour, stage, studyName,method,age_min=None, age_max=None):
    # input structure was [EXPONENT, SD, MEAN_AGE, SD_AGE, N_SAMPLE]
    global studyNum
    studyNum += 1
    age = data[2]
    age_sd = data[3] 
    measure_m = data[0]
    measure_sd = data[1]
    n = data[4]
    ellipse_line_width = 1
    ###########################
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
    ################################    
    if 'FOOOF' in method:
        colour='#E69F00' #orange
    elif 'IRASA' in method:
        colour='#2271B2' #honolulu blue
    elif 'PaWNextra' in method:
        colour='#F748F5' #pink
    elif 'DFA' in method:
        colour='#920000' # red
    else:
        colour='#000000'
        
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
    if not isinstance(measure_sd, float) and isinstance(age_sd, float) and ('Natarajan 2004 HE G ECR'in studyName):
        ax.plot([17, 23],[measure_m,measure_m],color=colour, alpha=colourAlpha)
        ell = Ellipse(xy=[20,measure_m], width=5, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha)
        ax.add_artist(ell)
    if isinstance(measure_sd, float) and isinstance(age_sd,float):
        ell = Ellipse(xy=[age,measure_m], width=age_sd*2, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and (studyName == 'Fransson 2013 G Sleep'):
        ax.plot([0.75, 0.85],[measure_m,measure_m],color=colour, linestyle='--', alpha=colourAlpha)
        ell = Ellipse(xy=[age,measure_m], width=0.06, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and ('Schaworonkow & Voytek' in studyName):
        ell = Ellipse(xy=[age,measure_m], width=0.06, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=0.5, fill=False)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and ('Linkenkaer Hansen 2001 ROI EOR' or 'Linkenkaer Hansen 2001 ROI ECR' in studyName):
        ax.plot([20, 30],[measure_m,measure_m],color=colour, alpha=colourAlpha)
        ell = Ellipse(xy=[25,measure_m], width=5, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha)
        ax.add_artist(ell)
        
### Infants ###
build_a_box_overlapping_Fig2A(CARTER_LENO_2022_group_infant_AE_EORvids,'#6F8FAF',
           'inf', 'Carter Leno 2022 G EOR Mixed','FOOOF',None,None)
build_a_box_overlapping_Fig2A(FRANSSON_2013_group_SE_SLEEP,'#14cad3',
            'inf','Fransson 2013 G Sleep','PLE',None, None)
### MANUAL EXTRACT OF GLOBAL APERIODIC ###
build_a_box_overlapping_Fig2A(SCH_VOY_2021_group_AE_40D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (40d)','FOOOF',None, None)
build_a_box_overlapping_Fig2A(SCH_VOY_2021_group_AE_69D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (69d)','FOOOF',None, None)
build_a_box_overlapping_Fig2A(SCH_VOY_2021_group_AE_96D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (96d)','FOOOF',None, None)
build_a_box_overlapping_Fig2A(KARALUNAS_2022_inf_AE_EOR, '#C49102',
            'inf','Karalunas 2022 Inf G EOR','FOOOF', None,None) 

#CHILD
build_a_box_overlapping_Fig2A(PEISCH_ARNETT2022_group_gAE_EO,'#00cc99',
            'child','Peisch & Arnett 2022 G EOR','FOOOF',None,None)
build_a_box_overlapping_Fig2A(ROBERTSON2019_group_gAE_EO,'#228b22',
            'child','Robertson 2019 G EOR','FOOOF',None, None)
build_a_box_overlapping_Fig2A(WILKINSON2021_group_gAE_EO,'#008736',
            'child','Wilkinson 2021 G EOR','FOOOF',None, None)
build_a_box_overlapping_Fig2A(HILL2022_group_gAE_EO, '#177245',
            'child','Hill 2022 G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(HILL2022_group_gAE_EC, '#177245',
            'child','Hill 2022 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(TRONDLE2022_group_gAE_EC, '#00703c',
            'child','Trondle 2022 G ECR','FOOOF',None,None)
build_a_box_overlapping_Fig2A(McSweeney2021_child_group_gEO, '#33B864',
            'child','McSweeney 2021 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(McSweeney2021_child_group_gEC, '#33B864',
            'child','McSweeney 2021 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(BRUINING2020_group_gHE,'#000000',
            'child','Bruining 2020 HE G ECR','DFA',None,None)

## ADOLESCENTS
build_a_box_overlapping_Fig2A(McSweeney2021_adol_group_gEO, '#CC7722',
            'adol','McSweeney 2021 G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(McSweeney2021_adol_group_gEC, '#CC7722',
            'adol','McSweeney 2021 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(OSTLUND2021_group_AE_EO, '#C49102',
            'adol','Ostlund 2021 G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(OSTLUND2021_group_AE_EC, '#C49102',
            'adol','Ostlund 2021 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(KARALUNAS_2022_adol_AE_EOR, '#C49102',
            'adol','Karalunas 2022 Adol G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(KARALUNAS_2022_adol_AE_ECR, '#C49102',
            'adol','Karalunas 2022 Adol G ECR','FOOOF', None,None)

# ### Young Adult ###
build_a_box_overlapping_Fig2A(LINKENKAER_HANSEN2001_ya_roiPLE_EO, '#773910',
            'ya','Linkenkaer Hansen 2001 ROI EOR', 'PLE',None,None)
build_a_box_overlapping_Fig2A(MUTHUKUMARASWAMY_LILEY_2018_ya_gIRASA_ECR_lf, '#D35400',
            'ya','M & L 2018 G ECR lf', 'IRASA',None,None)
build_a_box_overlapping_Fig2A(MUTHUKUMARASWAMY_LILEY_2018_ya_gIRASA_ECR_hf, '#DC7633',
            'ya','M & L 2018 G ECR hf', 'IRASA',None,None)
build_a_box_overlapping_Fig2A(PATHANIA_2021_ya_gAE_EOR, '#FBEEE6',
            'ya','Pathania 2021 G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(BARRY_DE_BLASIO_2021_ya_gPN_EO, '#BF360C',
            'ya','Barry & De Blasio 2021 G EOR', 'PaWNextra', None,None)
build_a_box_overlapping_Fig2A(BARRY_DE_BLASIO_2021_ya_gPN_EC, '#BF360C',
            'ya','Barry & De Blasio 2021 G ECR', 'PaWNextra', None,None)
build_a_box_overlapping_Fig2A(KE2022_ya_gAE_EO, '#873600',
            'ya','Ke 2022 G EOR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(IMMINK_2021_ya_gIRASA_ECR, '#E59866',
            'ya','Immink 2021 G ECR', 'IRASA',None,None)
build_a_box_overlapping_Fig2A(PATHANIA_2022_ya_gAE_ECR, '#FF8F00',
            'ya','Pathania 2022 G ECR', 'FOOOF',None,None)
build_a_box_overlapping_Fig2A(CROSS_2022_ya_gIRASA_EOR, '#F6DDCC',
            'ya','Cross 2022 G EOR', 'IRASA',None,None)
build_a_box_overlapping_Fig2A(CROSS_2022_ya_gIRASA_ECR, '#F6DDCC',
            'ya','Cross 2022 G ECR', 'IRASA',None,None)
build_a_box_overlapping_Fig2A(NAKAO2019_group_FCzHE_alpha,'#000000',
                              'ya','Nakao 2019 HE FCz ECR','DFA',None,None)
build_a_box_overlapping_Fig2A(NATARAJAN2004_group_gHE,'#000000',
                              'ya','Natarajan 2004 HE G ECR','DFA',None,None)
build_a_box_overlapping_Fig2A(SLEIMEN_MALKOUN2015_group_gHE,'#000000',
                              'ya','Sleimen Malkoun 2015 HE G ECR','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_EOR_theta,'#000000',
                              'ya','Irmischer 2017 HE EOR Theta','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_ECR_theta,'#000000',
                              'ya','Irmischer 2017 HE ECR Theta','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_EOR_alpha,'#000000',
                              'ya','Irmischer 2017 HE EOR Alpha','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_ECR_alpha,'#000000',
                              'ya','Irmischer 2017 HE ECR Alpha','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_EOR_beta,'#000000',
                              'ya','Irmischer 2017 HE EOR Beta','DFA',None,None)
build_a_box_overlapping_Fig2A(IRMISCHER2017_group_gHE_ECR_beta,'#000000',
                              'ya','Irmischer 2017 HE ECR Beta','DFA',None,None)

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
                              fontsize=legendFontSize*1.8,
                              loc='lower center', 
                              title='Markers',
                              bbox_to_anchor=(0.86, -0.155)) #ncol = 5 
markers_legend.get_title().set_fontweight('bold')
for text in markers_legend.get_texts():
    text.set_fontsize(legendFontSize*1)

studyList_G_R = ['Carter Leno 2022 G EOR Mixed', 
                 'Fransson 2013 PLE G Sleep', 
                 'Schaworonkow & Voytek 2021 40d G EOR Mixed',
                 'Schaworonkow & Voytek 2021 69d G EOR Mixed',
                 'Schaworonkow & Voytek 2021 96d G EOR Mixed',
                 'Karalunas 2022 Inf G EOR',
                 'Peisch & Arnett 2022 G EOR', 
                 'Robertson 2019 G EOR', 
                 'Wilkinson & Nelson 2021 G EOR', 
                 'Hill 2022 G EOR',  
                 'Hill 2022 G ECR',
                 'Trondle 2022 G ECR', 
                 'McSweeney 2021 Child G EOR',
                 'McSweeney 2021 Child G ECR',
                 'Bruining 2020 HE G ECR',
                 'McSweeney 2021 Adol G EOR', 
                 'McSweeney 2021 Adol G ECR', 
                 'Ostlund 2021 Adol G EOR',
                 'Ostlund 2021 Adol G ECR',
                 'Karalunas 2022 G EOR',
                 'Karalunas 2022 G ECR',
                 'Linkenkaer Hansen 2001 ROI EOR',
                 'M & L 2018 G ECR lf', 
                 'M & L 2018 G ECR hf', 
                 'Pathania 2021 G EOR', 
                 'Barry & De Blasio 2021 G EOR',
                 'Barry & De Blasio 2021 G ECR',
                 'Ke 2022 G EOR', 
                 'Immink 2021 G ECR',
                 'Pathania 2022 G ECR',
                 'Cross 2022 G EOR',  
                 'Cross 2022 G ECR',
                 'Nakao 2019 HE FCz ECR',
                 'Natarajan 2004 HE G ECR',
                 'Sleimen Malkoun 2015 HE G ECR',
                 'Irmischer 2017 HE G EOR Theta',
                 'Irmischer 2017 HE G ECR Theta',
                 'Irmischer 2017 HE G EOR Alpha',
                 'Irmischer 2017 HE G ECR Alpha',
                 'Irmischer 2017 HE G EOR Beta',
                 'Irmischer 2017 HE G ECR Beta',
                ]
from matplotlib.lines import Line2D
study_legend_labels = [f'{i+1}. {label}' for i, label in enumerate(studyList_G_R)]
study_legend_handles = [Line2D([], [], color='none', marker='', linestyle='', label=label)
                        for label in study_legend_labels]
study_legend = fig.legend(handles=study_legend_handles, fontsize=legendFontSize, loc='lower center',
                           title='Studies', bbox_to_anchor=(0.473, -0.15), ncol=6)
study_legend.get_title().set_fontweight('bold')
fig.subplots_adjust(wspace=1)
fig.set_size_inches(20, 8)
fig.text(0.4, 0.9, 'Global AE and 1/', fontsize=25, ha='center',weight='bold')
fig.text(0.47, 0.9, '$\it{f}$', fontsize=25, ha='center',style='italic',weight='bold')#.472
fig.text(0.592, 0.9, 'do not differ based on method', fontsize=25, ha='center',weight='bold')
fig.text(0.5, 0.04, 'Age (years)', ha='center',fontsize=18,weight='bold')
fig.text(0.08, 0.5, 'Aperiodic exponent ($\mu$V$^2$ Hz$^{-1}$)', 
         va='center', rotation='vertical',fontsize=18, weight='bold')
ax.axvline(x=2, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=3, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=14, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=19, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.axvline(x=26, color='black', linestyle='--', alpha=0.5,zorder=0)
ax.set_xlim(-1, 33)  # Set the x-axis range for the main plot
age_labels = ['Inf', 'Todd', 'Child', 'Adol', 'YA', 'Ext Adult']
age_positions = [0.8, 2.85, 9, 17, 22.5, 30]
for age_label, age_position in zip(age_labels, age_positions):
    ax.text(age_position, 0.25, age_label, color='grey', fontsize=12, ha='right', va='center', zorder=-1, rotation=0)
plt.tick_params(axis='y', labelsize=16)
plt.tick_params(axis='x', labelsize=16)
plot_the_key('2A')
plt.savefig('/Users/username/Desktop/someFolder/anotherFolder/continuedPath/name2A' 
            + '.pdf', bbox_inches='tight') 
