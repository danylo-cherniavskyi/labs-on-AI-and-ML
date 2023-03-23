import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import lab_funcs
import sklearn.datasets

STEP = 0.04
class App:
    def __init__(self):
        self.__graph()
        self.__hist()

    def __hist(self):
        data = sklearn.datasets.fetch_lfw_pairs()
        averaged_data = np.mean(data.data, 0)

        self.__figure2 = plt.figure()
        self.__figure2
        for i in range(25):
            self.__figure2.text(0.165 + i*0.0282, 0.12, f'Pixel {i+1}', color='brown', rotation=90)

        plt.hist(averaged_data, 25, color='magenta')
        plt.xlabel('Ознаки (пікселі)')
        plt.ylabel('Частота появи пікселя')
        plt.savefig('file2.png')
        plt.show()

    def __graph(self):
        self.__figure, (self.__ax_graph1, self.__ax_graph2, self.__ax_graph3) = plt.subplots(1, 3)
        self.__figure.set_dpi(100)
        self.__figure.set_size_inches((1920 / self.__figure.dpi, 1080 / self.__figure.dpi))

        self.__graph_color1 = 'b--^'
        self.__graph_color2 = 'm-.D'

        X_AXIS_LABEL_POS_X = 1.0
        X_AXIS_LABEL_POS_Y = 0.53

        Y_AXIS_LABEL_POS_X = 0.47
        Y_AXIS_LABEL_POS_Y = 1.0

        self.__ax_graph1.spines['left'].set_position('center')
        self.__ax_graph1.spines['bottom'].set_position('center')
        self.__ax_graph1.spines['right'].set_color('none')
        self.__ax_graph1.spines['top'].set_color('none')
        self.__ax_graph1.xaxis.set_ticks_position('bottom')
        self.__ax_graph1.yaxis.set_ticks_position('left')
        self.__ax_graph1.xaxis.set_label_text("X")
        self.__ax_graph1.xaxis.set_label_position('bottom')
        self.__ax_graph1.xaxis.set_label_coords(X_AXIS_LABEL_POS_X, X_AXIS_LABEL_POS_Y)
        self.__ax_graph1.yaxis.set_label_text("Y")
        self.__ax_graph1.yaxis.set_label_position('left')
        self.__ax_graph1.yaxis.set_label_coords(Y_AXIS_LABEL_POS_X, Y_AXIS_LABEL_POS_Y)

        self.__ax_graph2.spines['left'].set_position('center')
        self.__ax_graph2.spines['bottom'].set_position('center')
        self.__ax_graph2.spines['right'].set_color('none')
        self.__ax_graph2.spines['top'].set_color('none')
        self.__ax_graph2.xaxis.set_ticks_position('bottom')
        self.__ax_graph2.yaxis.set_ticks_position('left')
        self.__ax_graph2.xaxis.set_label_text("X")
        self.__ax_graph2.xaxis.set_label_position('bottom')
        self.__ax_graph2.xaxis.set_label_coords(X_AXIS_LABEL_POS_X, X_AXIS_LABEL_POS_Y)
        self.__ax_graph2.yaxis.set_label_text("Y")
        self.__ax_graph2.yaxis.set_label_position('left')
        self.__ax_graph2.yaxis.set_label_coords(Y_AXIS_LABEL_POS_X, Y_AXIS_LABEL_POS_Y)

        self.__ax_graph3.spines['left'].set_position('center')
        self.__ax_graph3.spines['bottom'].set_position('center')
        self.__ax_graph3.spines['right'].set_color('none')
        self.__ax_graph3.spines['top'].set_color('none')
        self.__ax_graph3.xaxis.set_ticks_position('bottom')
        self.__ax_graph3.yaxis.set_ticks_position('left')
        self.__ax_graph3.xaxis.set_label_text("X")
        self.__ax_graph3.xaxis.set_label_position('bottom')
        self.__ax_graph3.xaxis.set_label_coords(X_AXIS_LABEL_POS_X, X_AXIS_LABEL_POS_Y)
        self.__ax_graph3.yaxis.set_label_text("Y")
        self.__ax_graph3.yaxis.set_label_position('left')
        self.__ax_graph3.yaxis.set_label_coords(Y_AXIS_LABEL_POS_X, Y_AXIS_LABEL_POS_Y)

        (start, end) = lab_funcs.interval.values()
        interval_len = end - start
        xs = np.linspace(start, end, (int)(interval_len // STEP))
        ys = lab_funcs.func(xs)

        self.__ax_graph1.plot(xs, ys, self.__graph_color1, label='5*sin(1/x)*cos(x^2 + 1/x)^2')
        self.__ax_graph1.legend()
        self.__ax_graph1.set_title('Some plot1')

        self.__ax_graph2.plot(xs, ys, self.__graph_color2, label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=3.0)
        self.__ax_graph2.legend()
        self.__ax_graph2.set_title('Some plot2')

        self.__rainbow_graph()
        self.__ax_graph3.legend()
        self.__ax_graph3.set_title('Some cool plot')
        plt.savefig('file.png', dpi=200)

    def __rainbow_graph(self):
        (start, end) = lab_funcs.interval.values()
        interval_len = end - start
        num_intervals = (int)(interval_len // STEP)

        while num_intervals % 7 != 0:
            num_intervals += 1

        xs = np.linspace(start, end, num_intervals)
        ys = lab_funcs.func(xs)

        list_xs = np.split(xs, 7)
        list_ys = np.split(ys, 7)
        
        for i in range(0, 6):
            list_xs[i] = np.append(list_xs[i], list_xs[i+1][0])
            list_ys[i] = np.append(list_ys[i], list_ys[i+1][0])

        self.__ax_graph3.plot(list_xs[0], list_ys[0], ':o', color='red', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=1.0)
        self.__ax_graph3.plot(list_xs[1], list_ys[1], ':D', color='orange', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=2.0)
        self.__ax_graph3.plot(list_xs[2], list_ys[2], ':^', color='yellow', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=3.0)
        self.__ax_graph3.plot(list_xs[3], list_ys[3], ':s', color='green', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=4.0)
        self.__ax_graph3.plot(list_xs[4], list_ys[4], ':p', color='blue', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=3.0)
        self.__ax_graph3.plot(list_xs[5], list_ys[5], ':*', color='indigo', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=2.0)
        self.__ax_graph3.plot(list_xs[6], list_ys[6], ':x', color='violet', label='5*sin(1/x)*cos(x^2 + 1/x)^2', linewidth=1.0)

    def __draw(self):
        plt.show()

    def loop(self):
        self.__draw()
        plt.show(block=True)


def main():
    app = App()
    app.loop()


if __name__ == '__main__':
    main()
