print('FIGURE 4A')
fig, ax = plt.subplots(1,1,figsize=(10,8))
axMin = 0.70
axMax = 2.35
legendFontSize=7
studyNum = 0
def build_a_box_overlapping_Fig4A(data,colour, stage, studyName,age_min=None, age_max=None):
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
        
    if 'G EOR' in studyName or 'G ECR' in studyName or 'G Sleep' in studyName:
        ellipse_line_width = 1
        lineStyle = 'solid'
        colour = '#AD0000'
        if colourAlpha > 0.2:
            ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='w')
        else:
            ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='black')
    else:
        ellipse_line_width = 1
        lineStyle = 'dashed'
        colour = '#359B73' #green
        if colourAlpha > 0.2:
            ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='w')
        else:
            ax.annotate(studyNum, (age, measure_m), textcoords="offset points", xytext=(0,-2.2), ha='center',fontsize=8, color='black')
        #print('green')
    # Plot mean ± SD as boxplots
    ax.plot(age, measure_m, color=colour, label=studyName, marker=markerChoice, markersize=12, alpha=colourAlpha)
    if isinstance(measure_sd, float):
        ax.plot([age, age], [measure_m - measure_sd, measure_m + measure_sd],
                        color=colour,alpha=colourAlpha)
    if isinstance(age_sd, float):
        ax.plot([age - age_sd, age + age_sd],[measure_m,measure_m],color=colour, alpha=colourAlpha)
    if isinstance(measure_sd, float) and isinstance(age_sd,float):
        ell = Ellipse(xy=[age,measure_m], width=age_sd*2, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha, linestyle=lineStyle)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and (studyName == 'Fransson 2013 G Sleep'):
        ax.plot([0.75, 0.85],[measure_m,measure_m],color=colour, linestyle='--', alpha=colourAlpha)
        ell = Ellipse(xy=[age,measure_m], width=0.06, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha)
        ax.add_artist(ell)
    elif isinstance(measure_sd, float) and not isinstance(age_sd, float) and ('Linkenkaer Hansen 2001 ROI EOR' or 'Linkenkaer Hansen 2001 ROI ECR' in studyName):
        ax.plot([20, 30],[measure_m,measure_m],color=colour, linestyle='--', alpha=colourAlpha)
        ell = Ellipse(xy=[25,measure_m], width=5, height=measure_sd*2, angle=0,
              edgecolor=colour, lw=ellipse_line_width, fill=False,alpha=colourAlpha, linestyle=lineStyle)
        ax.add_artist(ell)
### Infants ###
build_a_box_overlapping_Fig4A(CARTER_LENO_2022_group_infant_AE_EORvids,'#6F8FAF',
           'inf', 'Carter Leno 2022 G EOR Mixed',None,None)
# build_a_box_overlapping_Fig4A(FRANSSON_2013_group_SE_SLEEP,'#14cad3',
#             'inf','Fransson 2013 G Sleep',None, None)
### MANUAL EXTRACT OF GLOBAL APERIODIC ###
build_a_box_overlapping_Fig3B(SCH_VOY_2021_group_AE_40D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (40d) G EOR',None, None)
build_a_box_overlapping_Fig3B(SCH_VOY_2021_group_AE_69D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (69d) G EOR',None, None)
build_a_box_overlapping_Fig3B(SCH_VOY_2021_group_AE_96D,'#14cad3',
            'inf','Schaworonkow & Voytek 2021 Mixed (96d) G EOR',None, None)
build_a_box_overlapping_Fig4A(KARALUNAS_2022_inf_AE_EOR, '#FFFFFF',
            'inf', 'Karalunas 2022 Inf G EOR', None, None)
#CHILD
build_a_box_overlapping_Fig4A(CELLIER2021_group_child_fAE_EO, '#00a550',
            'child','Cellier 2021 F EOR',None,None)
build_a_box_overlapping_Fig4A(CELLIER2021_group_child_pAE_EO, '#55a500',
            'child','Cellier 2021 P EOR',None,None)
build_a_box_overlapping_Fig4A(PEISCH_ARNETT2022_group_gAE_EO,'#00cc99',
            'child','Peisch & Arnett 2022 G EOR',None,None)
build_a_box_overlapping_Fig4A(ROBERTSON2019_group_gAE_EO,'#228b22',
            'child','Robertson 2019 G EOR',None, None)
build_a_box_overlapping_Fig4A(WILKINSON2021_group_gAE_EO,'#008736',
            'child','Wilkinson 2021 G EOR',None, None)
build_a_box_overlapping_Fig4A(WILKINSON2021_group_fAE_EO,'#00e95d',
            'child','Wilkinson 2021 F EOR',None, None)
build_a_box_overlapping_Fig4A(WILKINSON2021_group_cAE_EO,'#25ff7c',
            'child','Wilkinson 2021 C EOR',None, None)
build_a_box_overlapping_Fig4A(WILKINSON2021_group_pAE_EO,'#87ffb7',
            'child','Wilkinson 2021 P EOR',None, None)
build_a_box_overlapping_Fig4A(WILKINSON2021_group_tAE_EO,'#aeffcf',
            'child','Wilkinson 2021 T EOR',None, None)
build_a_box_overlapping_Fig4A(HILL2022_group_gAE_EO, '#177245',
            'child','Hill 2022 G EOR', None,None)
build_a_box_overlapping_Fig4A(HILL2022_group_aAE_EO, '#139251',
             'child','Hill 2022 A EOR', None,None)
build_a_box_overlapping_Fig4A(HILL2022_group_cAE_EO,'#069f50',
             'child','Hill 2022 C EOR',None, None)
build_a_box_overlapping_Fig4A(HILL2022_group_pAE_EO,'#557665',
             'child','Hill 2022 P EOR',None, None)
build_a_box_overlapping_Fig4A(TRONDLE2022_group_gAE_EC, '#00703c',
            'child','Trondle 2022 G ECR',None,None)
build_a_box_overlapping_Fig4A(McSweeney2021_child_group_gEO, '#2E8857',
            'child','McSweeney 2021 Child G EOR', None,None)
## ADOLESCENTS
build_a_box_overlapping_Fig4A(McSweeney2021_adol_group_gEO, '#CC7722',
            'adol','McSweeney 2021 Adol G EOR', None,None)
build_a_box_overlapping_Fig4A(OSTLUND2021_group_AE_EO, '#C49102',
            'adol','Ostlund 2021 G EOR', None,None)
build_a_box_overlapping_Fig4A(KARALUNAS_2022_adol_AE_EOR, '#FFFFFF',
            'adol', 'Karalunas 2022 Adol G EOR', None, None)
build_a_box_overlapping_Fig4A(CELLIER2021_group_adol_fAE_EO, '#a5a400',
            'adol','Cellier 2021 F EOR', None,None)
build_a_box_overlapping_Fig4A(CELLIER2021_group_adol_pAE_EO, '#bfbd00',
            'adol','Cellier 2021 P EOR', None,None)

# ### Young Adult ###
build_a_box_overlapping_Fig4A(DONOGHUE2020_group_CZ_EO, '#fd6500',
           'ya','Donoghue 2020 Cz EOR', None, None)
build_a_box_overlapping_Fig4A(KE2022_ya_gAE_EO, '#873600',
            'ya','Ke 2022 G EOR', None,None)
build_a_box_overlapping_Fig4A(KE2022_ya_cAE_EO, '#6e2c00',
            'ya','Ke 2022 C EOR', None,None)
build_a_box_overlapping_Fig4A(KE2022_ya_fAE_EO, '#3b1700',
            'ya','Ke 2022 F EOR', None,None)
build_a_box_overlapping_Fig4A(KE2022_ya_pAE_EO, '#ba4a00',
            'ya','Ke 2022 P EOR', None,None)
build_a_box_overlapping_Fig4A(MUTHUKUMARASWAMY_LILEY_2018_ya_gIRASA_ECR_lf, '#D35400',
            'ya','M & L 2018 G ECR', None,None)
build_a_box_overlapping_Fig4A(MUTHUKUMARASWAMY_LILEY_2018_ya_gIRASA_ECR_hf, '#DC7633',
            'ya','M & L 2018 G ECR', None,None)
build_a_box_overlapping_Fig4A(IMMINK_2021_ya_gIRASA_ECR, '#E59866',
            'ya','Immink 2021 G ECR', None,None)
build_a_box_overlapping_Fig4A(CROSS_2022_ya_gIRASA_EOR, '#F6DDCC',
            'ya','Cross 2022 G EOR', None,None)
build_a_box_overlapping_Fig4A(CELLIER2021_group_ya_fAE_EO, '#ff9f60',
            'ya','Cellier 2021 F EOR', None,None)
build_a_box_overlapping_Fig4A(CELLIER2021_group_ya_pAE_EO, '#ff7011',
            'ya','Cellier 2021 P EOR', None,None)
build_a_box_overlapping_Fig4A(PATHANIA_2021_ya_gAE_EOR, '#FBEEE6',
            'ya','Pathania 2022 G EOR', None,None)
build_a_box_overlapping_Fig4A(BARRY_DE_BLASIO_2021_ya_gPN_EO, '#BF360C',
            'ya','Barry & De Blasio 2021 G EOR', None,None)

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
                              bbox_to_anchor=(0.86, -0.154)) #ncol = 5 
markers_legend.get_title().set_fontweight('bold')
for text in markers_legend.get_texts():
    text.set_fontsize(legendFontSize*1)

List_G_R = ['Carter Leno 2022 G EOR Mixed', 
#                  'Fransson 2013 G Sleep', 
                 'Schaworonkow & Voytek 2021 40d G EOR Mixed',
                 'Schaworonkow & Voytek 2021 69d G EOR Mixed',
                 'Schaworonkow & Voytek 2021 96d G EOR Mixed', 
                 'Cellier 2021 Child F EOR',
                 'Cellier 2021 Child P EOR',
                 'Karalunas 2022 Inf G EOR',
                 'Peisch & Arnett 2022 G EOR', 
                 'Robertson 2019 G EOR', 
                 'Wilkinson & Nelson 2021 G EOR', 
                 'Wilkinson & Nelson 2021 F EOR', 
                 'Wilkinson & Nelson 2021 C EOR', 
                 'Wilkinson & Nelson 2021 P EOR', 
                 'Wilkinson & Nelson 2021 T EOR', 
                 'Hill 2022 G EOR',
                 'Hill 2022 A EOR',
                 'Hill 2022 C EOR',
                 'Hill 2022 P EOR',  
                 'Trondle 2022 G ECR', 
                 'McSweeney 2021 Child G EOR', 
                 'McSweeney 2021 Adol G EOR', 
                 'Ostlund 2021 G EOR', 
                 'Karalunas 2022 Adol G EOR',
                 'Cellier 2021 F EOR',
                 'Cellier 2021 P EOR',
                 'Donoghue 2021 Cz EOR',
                 'Ke 2022 G EOR',
                 'Ke 2022 C EOR',
                 'Ke 2022 F EOR',
                 'Ke 2022 P EOR',
                 'M & L 2018 G lf ECR', 
                 'M & L 2018 G hf ECR', 
                 'Immink 2021 G ECR', 
                 'Cross 2022 G EOR', 
                 'Cellier 2021 YA F EOR',
                 'Cellier 2021 YA P EOR',
                 'Pathania 2022 G EOR',  
                 'Barry & De Blasio 2021 G EOR']
from matplotlib.lines import Line2D
study_legend_labels = [f'{i+1}. {label}' for i, label in enumerate(List_G_R)]
study_legend_handles = [Line2D([], [], color='none', marker='', linestyle='', label=label)
                        for label in study_legend_labels]
study_legend = fig.legend(handles=study_legend_handles, fontsize=legendFontSize, loc='lower center',
                           title='Studies', bbox_to_anchor=(0.475, -0.15), ncol=7)
study_legend.get_title().set_fontweight('bold')
fig.subplots_adjust(wspace=1)
fig.set_size_inches(20, 8)
fig.text(0.5,0.95, 'Regional vs Global AE', ha='center',fontsize=25,weight='bold')
fig.text(0.5, 0.05, 'Age (years)', ha='center',fontsize=18,weight='bold')
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
plot_the_key('4A')
plt.savefig('/Users/username/Desktop/someFolder/anotherFolder/continuedPath/name4a' 
            + '.pdf', bbox_inches='tight') 
