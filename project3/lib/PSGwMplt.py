import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
import bike_evaluation as be


# ------------------------------- Initialize the figure -----------------------
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)


# ------------------------------- Beginning of Matplotlib helper code -----------------------
def draw_figure(canvas, figure):
    # delete the last figure
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
    
    
# ------------------------------- Matplotlib code -----------------------
def _img_info(px, py):
    #Use for simple test
    x = np.linspace(0, 2*np.pi)
    y = np.sin(x) * px -py
    line = ax.plot(x, y)
    
    o_y = np.sin(x) * 250 -250  #input the default value
    o_line = ax.plot(x, o_y)

def img_info(px, py, travel_step=10):
    ########### Joint configuration ###########
    p0 = (0, 0)
    p1 = (-41.52, -5.1)
    p2 = (-397.41, -42.50)
    # p2 = (px, py)
    p3 = (17.68, 111.69)
    # p4 = (-3.2, 154.98)
    p4 = (px, py)
    p5 = (89, 201.72)
    theta = 187.14

    # lf = lower frame
    lf = (-12.72, -63.05)
    lf_r = 105.16/2
    p2_r = 85.56/2
    ########### Joint configuration ###########
    wheel_travel = [i for i in range(0, 160, travel_step)]
    as_list = []
    ar_list = []
    
    dtheta_list = [0, 3.16, 2.9642, 2.7607, 2.5415, 2.3085, 2.0611, 1.799, 1.5202, 1.2224, 0.9009, 0.5468, 0.1447, -0.3348, 0.0453, -2.8763]
    
    theta = 187.14
    for index, step in enumerate(wheel_travel):
        theta -= dtheta_list[index]
        # print(theta)
        pos = be.Pos(p0, p1, p2, p3, p4, p5, theta)
        # print(index, step, pos.ppos())
        IC = be.intersection(pos.ppos()[0], pos.ppos()[1], pos.ppos()[3], pos.ppos()[4])
        # print("IC: ", IC)
        otl = be.out_tanglin(lf, pos.ppos()[2], lf_r, p2_r)
        IFC = be.intersection(pos.ppos()[2], IC, lcoe=otl)
        # print("IFC: ", IFC)
        h2_as = be.anti_squat((-397.12, -411.68+step), IFC, h1=1057, origin2front=662.8)
        h2_ar = be.anti_rise((-397.12, -411.68+step), IC, h1 = 1057, origin2front=662.8)
        # print("h2_as: ", h2_as)
        as_list.append(h2_as)
        ar_list.append(h2_ar)
        
        # print("\n")
    ax.plot(wheel_travel, as_list, label="Anti squat")
    ax.plot(wheel_travel, ar_list, label="Anti rise")
    ax.grid()
    ax.set_xlim(0,170)
    ax.set_ylim(-100, 200)
    ax.set_xlabel("wheel travel")
    ax.set_ylabel("%")
    ax.legend(loc="best")
    # plt.show()
    
    
# ------------------------------- PySimpleGUI CODE  -------------------------------
default_px = -4
default_py = 154
layout = [
    # [sg.Slider(range=(0, 500), default_value=default_val, size=(50, 10), orientation="horizontal", enable_events=True, key="slider")],
    [sg.Combo(["p2", "p4"], key="point")],
    [sg.Spin(values=[i for i in range(-200, 201)], initial_value=default_px, size=(8, 4),enable_events=True, key="spin_x"), sg.Text("Px"),
        sg.Spin(values=[i for i in range(-200, 201)], initial_value=default_py, size=(8, 4),enable_events=True, key="spin_y"), sg.Text("Py")],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Button("Reset"), sg.Button("Plot"), sg.Button("Record")]
]

"""  # Test to add the control panel
layout_slider = [
    [sg.Slider(range=(0, 500), default_value=val, size=(50, 10), orientation="horizontal", enable_events=True, key="slider_cont")],
    [sg.Spin(values=[i for i in range(1000)], initial_value=val, size=(8, 4),enable_events=True, key="spin_cont")],
]
"""

window = sg.Window("Suspension Evaluation", layout)
# window_slider = sg.Window("control panel", layout_slider)
window.Finalize()

# add the plot to the window
fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)


while True:
    event, values = window.Read()
    # print(event, values)
    # print(values["slider"])
    # fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    
  
    if event == sg.WIN_CLOSED:
        break
        
        
    elif event == "slider":
        pass
        """
        # generate the new figure
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        val = int(values["slider"])
        _img_info(val)
        fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        # synchronize the values of event
        window.Element("spin_x").Update(val)
        window.Element("spin_y").Update(val)
        """
        
    elif event == "Reset":
        # fig.clf()
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        img_info(default_px, default_py)
        fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        
    elif event == "Plot":
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        
        if values["point"] == "p4":
            p4x = int(values["spin_x"])
            p4y = int(values["spin_y"])
            img_info(p4x, p4y)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            # window.Element("slider").Update(val)
            window.Element("spin_x").Update(p4x)
            window.Element("spin_y").Update(p4y)
            
    elif event == "Record":
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        p4x = int(values["spin_x"])
        p4y = int(values["spin_y"])
        img_info(p4x, p4y)
        window.Element("spin_x").Update(p4x)
        window.Element("spin_y").Update(p4y)


        """
        if values["point"] == "p2":
            p2x = int(values["spin_x"])
            p2y = int(values["spin_y"])
            img_info(p2x, p2y)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            # window.Element("slider").Update(val)
            window.Element("spin_x").Update(p2x)
            window.Element("spin_y").Update(p2y)
        """
            







