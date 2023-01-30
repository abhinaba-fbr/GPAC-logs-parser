import os

class Plotter:
    """
    Class to Plot graphs based and configure its plotting parameters
    """
    def __init__(self):
        self.plot_type="lp"
        self.line_width=2
        self.line_color=3
        self.point_type=4

    def set_plot_type(self, type):
        self.plot_type=type

    def set_line_width(self, width):
        self.line_width=width

    def set_line_color(self, color):
        self.line_color=color

    def set_point_type(self, point_type):
        self.point_type=point_type

    def get_range(self, array):
        return (min(array), max(array)+1)

    def generate_dat_file(self, xarray, yarray):
        f=open("data.dat", "w")
        for i in range(len(xarray)):
            f.write(str(xarray[i])+" "+str(yarray[i])+"\n")
        f.close()
        return

    def plot_graph(self, xarray=[], yarray=[], title="title", xlabel="xlabel", ylabel="ylabel", output_filename="output.eps", output_directory="plots"):
        if(len(xarray)==0 or len(yarray)==0 or len(xarray)!=len(yarray)): 
            print("Plot with title "+title+" cannot be generated")
            return
        self.generate_dat_file(xarray, yarray)
        (xmin, xmax)=self.get_range(xarray)
        (ymin, ymax)=self.get_range(yarray)
        plot_file_content=""
        plot_file_content+="set term postscript eps color blacktext 'Arial'\n"
        plot_file_content+="set output '"+output_directory+"/"+output_filename+"'\n"
        plot_file_content+="set title '"+title+"'\n"
        plot_file_content+="set xlabel '"+xlabel+"'\n"
        plot_file_content+="set ylabel '"+ylabel+"'\n"
        plot_file_content+="set xrange ["+str(xmin)+":"+str(xmax)+"]\n"
        plot_file_content+="set yrange ["+str(ymin)+":"+str(ymax)+"]\n"
        plot_file_content+="set key right top vertical\n"
        plot_file_content+="plot 'data.dat' w "+self.plot_type+" lw "+str(self.line_width)+" lc "+str(self.line_color)+" pt "+str(self.point_type)+"\n"
        f=open("plot_file.plt", "w")
        f.write(plot_file_content)
        f.close()
        os.system("gnuplot plot_file.plt")
        os.system("rm -rf plot_file.plt data.dat")
        return