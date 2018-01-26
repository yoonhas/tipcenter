
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt
import numpy as np



def draw_graph(box,userId):
    if userId == '1':
        PSS =pd.DataFrame(columns=['Health', 'Community','Childcare', 'Jobskills', 'SoftSkill', 'Peb_all',
                                   'Empowerment', 'Selfmotivation', 'SkilResources', 'GaolOrientation','Ehs_all',
                                   'Ess1', 'Ess2', 'Ess3', 'Ess4', 'Ess_all', 'PSS'])

        for i in range(4):
            _, diction = box[i]
            PSS.loc[i] = [diction['Health']['mean'],diction['Community']['mean'],diction['Childcare']['mean']
                ,diction['Jobskills']['mean'],diction['SoftSkill']['mean'],diction['Peb_all']['mean'],
                          diction['Empowerment']['mean'], diction['Selfmotivation']['mean'],
                          diction['SkilResources']['mean']
                , diction['GaolOrientation']['mean'], diction['Ehs_all']['mean'],
                          diction['Ess1']['mean'], diction['Ess2']['mean'], diction['Ess3']['mean']
                , diction['Ess4']['mean'], diction['Ess_all']['mean'], diction['PSS']['mean'] ]
    else:
        PSS = pd.DataFrame(columns=['Peb_all','Ehs_all', 'Ess_all', 'PSS'])

        for i in range(4):
            _, diction = box[i]
            PSS.loc[i] = [ diction['Peb_all']['mean'],
                          diction['Ehs_all']['mean'],
                          diction['Ess_all']['mean'], diction['PSS']['mean']]


    fig, ax = plt.subplots()
    line_collection= []
    x =['1st', '2nd', '3rd', '4th']
    ax.grid(True, alpha=0.3)
    print(PSS)
    for key, val in PSS.iteritems():

        l = ax.plot((val.index +1), val.values, marker='.', label=key)
        line_collection.append(l)


    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    plt.xticks(val.index+1, x)

    interactive_legend = plugins.InteractiveLegendPlugin(line_collection,labels, start_visible=False)
    plugins.connect(fig, interactive_legend)
    fig.subplots_adjust(right=0.7)
    #plt.ylim(-1, 1)
    ax.set_xlabel('Times')
    ax.set_ylabel('Mean')
    ax.set_title('PSS', size=20)
    fig.set_size_inches(12, 5)
    html_fig = mpld3.fig_to_html(fig)

    plt.close(fig)

    return html_fig

def draw_graph_Agent(box,box1):

    PSS = pd.DataFrame(columns=['PEB_Total','Ehs_Total', 'Ess_Total', 'PSS_Total', 'PEB','Ehs', 'Ess', 'PSS'])

    for i in range(4):
        _, diction = box[i]
        _, diction1 = box1[i]
        PSS.loc[i] = [ diction['Peb_all']['mean'],diction['Ehs_all']['mean'],diction['Ess_all']['mean'],
                       diction['PSS']['mean'],
                       diction1['Peb_all']['mean'],
                      diction1['Ehs_all']['mean'],
                      diction1['Ess_all']['mean'], diction1['PSS']['mean']]


    fig, ax = plt.subplots()
    line_collection= []
    x =['1st', '2nd', '3rd', '4th']
    ax.grid(True, alpha=0.3)
    for key, val in PSS.iteritems():

        l = ax.plot((val.index +1), val.values, label=key)
        line_collection.append(l)


    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    plt.xticks(val.index+1, x)

    interactive_legend = plugins.InteractiveLegendPlugin(line_collection,labels, start_visible=False)
    plugins.connect(fig, interactive_legend)
    fig.subplots_adjust(right=0.7)

    ax.set_xlabel('Times')
    ax.set_ylabel('Mean')
    ax.set_title('PSS', size=20)
    fig.set_size_inches(12, 5)
    html_fig = mpld3.fig_to_html(fig)

    plt.close(fig)

    return html_fig

def draw_graph_Agent_compare(box,box1, box2):
    PSS = pd.DataFrame(columns=['PEB_Total','Ehs_Total', 'Ess_Total', 'PSS_Total', 'PEB_Agent','Ehs_Agent', 'Ess_Agent', 'PSS_Agent',
                                'PEB_Case','Ehs_Case', 'Ess_Case', 'PSS_Case'])

    for i in range(4):
        _, diction = box[i]
        _, diction1 = box1[i]
        PSS.loc[i] = [ diction['Peb_all']['mean'],diction['Ehs_all']['mean'],diction['Ess_all']['mean'],
                       diction['PSS']['mean'],
                       diction1['Peb_all']['mean'],
                      diction1['Ehs_all']['mean'],
                      diction1['Ess_all']['mean'], diction1['PSS']['mean'], box2.ix[i]['Peb_all'], box2.ix[i]['Ehs_all'], box2.ix[i]['Ess_all'], box2.ix[i]['PSS']]


    fig, ax = plt.subplots()
    line_collection= []
    x =['1st', '2nd', '3rd', '4th']
    ax.grid(True, alpha=0.3)
    for key, val in PSS.iteritems():

        l = ax.plot((val.index +1), val.values, label=key)
        line_collection.append(l)


    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    plt.xticks(val.index+1, x)

    interactive_legend = plugins.InteractiveLegendPlugin(line_collection,labels, start_visible=False)
    plugins.connect(fig, interactive_legend)
    fig.subplots_adjust(right=0.7)

    ax.set_xlabel('Times')
    ax.set_ylabel('Mean')
    ax.set_title('PSS', size=20)
    fig.set_size_inches(12, 5)
    html_fig = mpld3.fig_to_html(fig)

    plt.close(fig)

    return html_fig

def draw_graph_Admin_compare(box):

    fig, ax = plt.subplots()
    line_collection= []
    x =['1st', '2nd', '3rd', '4th']
    ax.grid(True, alpha=0.3)
    print("=========")


    for key, val in box.iteritems():

        l = ax.plot((val.index+1), val.values, marker='o', label=key)
        line_collection.append(l)





    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    plt.xticks(val.index + 1, x)

    interactive_legend = plugins.InteractiveLegendPlugin(line_collection,labels, start_visible=False)
    plugins.connect(fig, interactive_legend)
    fig.subplots_adjust(right=0.7)
    plt.rcParams['axes.xmargin'] = 0
    plt.ylim(ymin=0)
    plt.ylim(ymax=12)
    plt.xlim(xmin=1)
    plt.xlim(xmax=5.4)
    ax.set_xlabel('Times')
    ax.set_ylabel('Mean')
    ax.set_title('PSS', size=20)
    fig.set_size_inches(12, 5)
    html_fig = mpld3.fig_to_html(fig)

    plt.close(fig)

    return html_fig
