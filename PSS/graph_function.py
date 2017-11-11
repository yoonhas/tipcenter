
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt


def draw_graph(box,userId):
    if userId == '1':
        PSS =pd.DataFrame(columns=['Health', 'Community','Childcare', 'Jobskills', 'SoftSkill', 'Peb_all',
                                   'Empowerment', 'Selfmotivation', 'SkilResources', 'GaolOrientation','Ehs_all',
                                   'Ess1', 'Ess2', 'Ess3', 'Ess4', 'Ess_all', 'PSS'])

        for i in range(4):
            _, diction = box[i]
            PSS.loc[i] = [diction['Health_Z']['mean'],diction['Community_Z']['mean'],diction['Childcare_Z']['mean']
                ,diction['Jobskills_Z']['mean'],diction['SoftSkill_Z']['mean'],diction['Peb_all_Z']['mean'],
                          diction['Empowerment_Z']['mean'], diction['Selfmotivation_Z']['mean'],
                          diction['SkilResources_Z']['mean']
                , diction['GaolOrientation_Z']['mean'], diction['Ehs_all_Z']['mean'],
                          diction['Ess1_Z']['mean'], diction['Ess2_Z']['mean'], diction['Ess3_Z']['mean']
                , diction['Ess4_Z']['mean'], diction['Ess_all_Z']['mean'], diction['PSS_Z']['mean'] ]
    else:
        PSS = pd.DataFrame(columns=['Peb_all','Ehs_all', 'Ess_all', 'PSS'])

        for i in range(4):
            _, diction = box[i]
            PSS.loc[i] = [ diction['Peb_al_Zl']['mean'],
                          diction['Ehs_all_Z']['mean'],
                          diction['Ess_all_Z']['mean'], diction['PSS_Z']['mean']]


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
        PSS.loc[i] = [ diction['Peb_all_Z']['mean'],diction['Ehs_all_Z']['mean'],diction['Ess_all_Z']['mean'],
                       diction['PSS_Z']['mean'],
                       diction1['Peb_all_Z']['mean'],
                      diction1['Ehs_all_Z']['mean'],
                      diction1['Ess_all_Z']['mean'], diction1['PSS_Z']['mean']]


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
        PSS.loc[i] = [ diction['Peb_all_Z']['mean'],diction['Ehs_all_Z']['mean'],diction['Ess_all_Z']['mean'],
                       diction['PSS_Z']['mean'],
                       diction1['Peb_all_Z']['mean'],
                      diction1['Ehs_all_Z']['mean'],
                      diction1['Ess_all_Z']['mean'], diction1['PSS_Z']['mean'], box2.ix[i]['Peb_all_Z'], box2.ix[i]['Ehs_all_Z'], box2.ix[i]['Ess_all_Z'], box2.ix[i]['PSS']]


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
    for key, val in box.iteritems():

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
