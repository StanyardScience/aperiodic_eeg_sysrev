#GenCode: OLap11, SVA
print(f'SUPPLEMENT: REGIONAL VARIATION IN AE/HE')

### Child ### 
BRUINING2020_group_gHE = [0.66,0.04,10.30,1.54,29]

### Young Adults ###
NATARAJAN2004_group_gHE = [0.29,0.06,20,3,30]
SLEIMEN_MALKOUN2015_group_gHE = [1.69, 'unknown',22.70,1.60,31]
NAKAO2019_group_FCzHE_alpha = ['redacted','redacted', 'redacted','unknown','redacted']
BORNAS2013_group_cHE_EORECRavg_broadband = [0.85,0.07,24.61,7.03,56]
BORNAS2013_group_pHE_EORECRavg_broadband = [0.86,0.06,24.61,7.03,56]
BORNAS2013_group_oHE_EORECRavg_broadband = [0.88,0.06,24.61,7.03,56] # don't include band-wise, takes too long

BRUINING2020_group_gHE[0] = HE2AE(BRUINING2020_group_gHE)
NATARAJAN2004_group_gHE[0] = HE2AE(NATARAJAN2004_group_gHE)
SLEIMEN_MALKOUN2015_group_gHE[0] = HE2AE(SLEIMEN_MALKOUN2015_group_gHE)
#NAKAO2019_group_FCzHE_alpha[0] = HE2AE(NAKAO2019_group_FCzHE_alpha)
BORNAS2013_group_cHE_EORECRavg_broadband[0] = HE2AE(BORNAS2013_group_cHE_EORECRavg_broadband)
BORNAS2013_group_pHE_EORECRavg_broadband[0] = HE2AE(BORNAS2013_group_pHE_EORECRavg_broadband)
BORNAS2013_group_oHE_EORECRavg_broadband[0] = HE2AE(BORNAS2013_group_oHE_EORECRavg_broadband) 

fig, ax = plt.subplots(1,1,figsize=(10,8))
axMin = 0.70
axMax = 2.35
legendFontSize=7
studyNum = 0

def build_a_box_overlapping_VA(data,colour, stage, studyName,method,age_min=None, age_max=None):
    # input structure was [EXPONENT, SD, MEAN_AGE, SD_AGE, N_SAMPLE]
    global studyNum
    studyNum += 1
    age = data[2]
    age_sd = data[3] 
    measure_m = data[0]
    measure_sd = data[1]
    n = data[4]
    ellipse_line_width = 1
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
        
#     if 'ECR' in studyName or 'Sleep' in studyName:
#         ellipse_line_width = 1.5
#         lineStyle = 'dashed'
#     else:
#         ellipse_line_width = 1
#         lineStyle = 'solid'
        
    if 'FOOOF' in method:
        colour='#E69F00' #orange
    elif 'IRASA' in method:
        colour='#2271D2' #honolulu blue
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
# No regional 
#CHILD
build_a_box_overlapping_VA(CELLIER2021_group_child_fAE_EO, '#00a550',
            'child','Cellier 2021 F EOR','FOOOF',None,None)
build_a_box_overlapping_VA(CELLIER2021_group_child_pAE_EO, '#55a500',
            'child','Cellier 2021 P EOR','FOOOF',None,None)
build_a_box_overlapping_VA(WILKINSON2021_group_fAE_EO,'#00e95d',
            'child','Wilkinson 2021 F EOR','FOOOF',None, None)
build_a_box_overlapping_VA(WILKINSON2021_group_cAE_EO,'#25ff7c',
            'child','Wilkinson 2021 C EOR','FOOOF',None, None)
build_a_box_overlapping_VA(WILKINSON2021_group_pAE_EO,'#87ffb7',
            'child','Wilkinson 2021 P EOR','FOOOF',None, None)
build_a_box_overlapping_VA(WILKINSON2021_group_tAE_EO,'#aeffcf',
            'child','Wilkinson 2021 T EOR','FOOOF',None, None)
build_a_box_overlapping_VA(HILL2022_group_aAE_EO, '#139251',
             'child','Hill 2022 A EOR','FOOOF', None,None)
build_a_box_overlapping_VA(HILL2022_group_cAE_EO,'#069f50',
             'child','Hill 2022 C EOR','FOOOF',None, None)
build_a_box_overlapping_VA(HILL2022_group_pAE_EO,'#557665',
             'child','Hill 2022 P EOR','FOOOF',None, None)

## ADOLESCENTS
build_a_box_overlapping_VA(CELLIER2021_group_adol_fAE_EO, '#a5a400',
            'adol','Cellier 2021 F EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(CELLIER2021_group_adol_pAE_EO, '#bfbd00',
            'adol','Cellier 2021 P EOR', 'FOOOF',None,None)

# ### Young Adult ###
build_a_box_overlapping_VA(KE2022_ya_cAE_EO, '#6e2c00',
            'ya','Ke 2022 C EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(KE2022_ya_fAE_EO, '#3b1700',
            'ya','Ke 2022 F EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(KE2022_ya_pAE_EO, '#ba4a00',
            'ya','Ke 2022 P EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(CELLIER2021_group_ya_fAE_EO, '#ff9f60',
            'ya','Cellier 2021 F EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(CELLIER2021_group_ya_pAE_EO, '#ff7011',
            'ya','Cellier 2021 P EOR', 'FOOOF',None,None)
build_a_box_overlapping_VA(LINKENKAER_HANSEN2001_ya_roiPLE_EO, '#773910',
            'ya','Linkenkaer Hansen 2001 ROI EOR', 'PLE',None,None)
build_a_box_overlapping_VA(DONOGHUE2020_group_CZ_EO, '#fd6500',
           'ya','Donoghue 2020 Cz EOR', 'FOOOF',None, None)
build_a_box_overlapping_VA(NAKAO2019_group_FCzHE_alpha,'#000000',
                              'ya','Nakao 2019 HE FCz ECR','DFA',None,None)
build_a_box_overlapping_VA(BORNAS2013_group_cHE_EORECRavg_broadband,'#000000',
                              'ya','Bornas 2013 C HE EOR-ECRavg Bb','DFA',None,None)
build_a_box_overlapping_VA(BORNAS2013_group_pHE_EORECRavg_broadband,'#000000',
                              'ya','Bornas 2013 P HE EOR-ECRavg Bb','DFA',None,None)
build_a_box_overlapping_VA(BORNAS2013_group_oHE_EORECRavg_broadband,'#000000',
                              'ya','Bornas 2013 O HE EOR-ECRavg Bb','DFA',None,None)

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
                              bbox_to_anchor=(0.79, -0.134)) #ncol = 5 
markers_legend.get_title().set_fontweight('bold')
for text in markers_legend.get_texts():
    text.set_fontsize(legendFontSize*0.8)

studyList_G_R = ['Cellier 2021 (child) F EOR', 
                 'Cellier 2021 (child) F EOR', 
                 'Wilkinson 2021 F EOR', 
                 'Wilkinson 2021 C EOR', 
                 'Wilkinson 2021 P EOR', 
                 'Wilkinson 2021 T EOR', 
                 'Hill 2022 A EOR', 
                 'Hill 2022 C EOR', 
                 'Hill 2022 P EOR', 
                 'Cellier 2021 (adol) F EOR', 
                 'Cellier 2021 (adol) P EOR', 
                 'Ke 2022 C EOR',                 
                 'Ke 2022 F EOR',                 
                 'Ke 2022 P EOR',
                 'Cellier 2021 (ya) F EOR', 
                 'Cellier 2021 (ya) P EOR', 
                 'Linkenkaer Hansen 2001 ROI EOR', 
                 'Donoghue 2020 Cz EOR',
                 'Nakao 2019 HE FCz ECR',
                 'Bornas 2013 C HE EOR-ECRavg Bb',
                 'Bornas 2013 P HE EOR-ECRavg Bb',
                 'Bornas 2013 O HE EOR-ECRavg Bb']
from matplotlib.lines import Line2D
study_legend_labels = [f'{i+1}. {label}' for i, label in enumerate(studyList_G_R)]
study_legend_handles = [Line2D([], [], color='none', marker='', linestyle='', label=label)
                        for label in study_legend_labels]
study_legend = fig.legend(handles=study_legend_handles, fontsize=legendFontSize, loc='lower center',
                           title='Studies', bbox_to_anchor=(0.52, -0.13), ncol=5)
study_legend.get_title().set_fontweight('bold')
fig.subplots_adjust(wspace=1)
fig.subplots_adjust(wspace=1)
fig.set_size_inches(20, 8)
fig.text(0.35, 0.9, '1/', fontsize=25, ha='center',weight='bold')
fig.text(0.362, 0.9, '$\it{f}$', fontsize=25, ha='center',style='italic',weight='bold')
fig.text(0.51, 0.9, 'does not differ by method (Regional)', fontsize=25, ha='center',weight='bold')
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
    ax.text(age_position, 0.365, age_label, color='grey', fontsize=12, ha='right', va='center', zorder=-1, rotation=0)
plot_the_key('SVA')

#plt.savefig('/Users/username/Desktop/someFolder/anotherFolder/continuedPath/nameSVa' 
#            + '.pdf', bbox_inches='tight') 
