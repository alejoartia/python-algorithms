from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('sample plotting.html')
    fig = figure()

    total_vals = int(input('how many values you-d like to plot?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'value for {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)