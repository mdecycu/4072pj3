import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib



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
def img_info(v):
    """
    default_pos = {
        "p0": (0, 0),
        "p1": (-41.6, -4.5),
        "p2": (-397.41, -40),
        "p3": (-2.38, 154.98),
        "p4": (17.6674, 111.69),
        "p5": (89, 201.72)
    }
    
    wheel_travel = np.linspace(0, 160, 10)
    """
    x = np.linspace(0, 2*np.pi)
    y = np.sin(x) * v
    line = ax.plot(x, y)
    
    
# ------------------------------- PySimpleGUI CODE
val = 250
layout = [
    [sg.Slider(range=(0, 500), default_value=val, size=(50, 10), orientation="horizontal", enable_events=True, key="slider")],
    [sg.Spin(values=[i for i in range(1000)], initial_value=val, size=(8, 4),enable_events=True, key="spin")],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Button("OK")]
]
"""  # Test to add the control panel
layout_slider = [
    [sg.Slider(range=(0, 500), default_value=val, size=(50, 10), orientation="horizontal", enable_events=True, key="slider_cont")],
    [sg.Spin(values=[i for i in range(1000)], initial_value=val, size=(8, 4),enable_events=True, key="spin_cont")],
]
"""

window = sg.Window("slider_test", layout)
# window_slider = sg.Window("control panel", layout_slider)
window.Finalize()

# add the plot to the window
fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)


while True:
    event, values = window.Read()
    # print(event, values)
    # print(values["slider"])
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    
  
    if event == sg.WIN_CLOSED:
        break
    elif event == "slider":
        # generate the new figure
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        val = values["slider"]
        img_info(val)
        # synchronize the values of event
        # window.Element("spin").Update(val)
"""
    elif event == "spin":
        val = values["spin"]
        window.Element("slider").Update(val)
"""
"""
    elif event == "OK":
        # fig.clf()
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
"""        
        
window.close()





