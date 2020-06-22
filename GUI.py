from tkinter import filedialog
from tkinter import *
import tkinter
import PreProcessing as pp
import Clustering as cl
from tkinter import messagebox
from matplotlib import pyplot as plt
import chart_studio.plotly as py
import pandas as pd
import plotly.graph_objects as go
from PIL import Image, ImageTk


class KMeansGUI:

    def __init__(self, master):
        self.master = master
        master.title("K Means Clustering")
        validate_k_num = master.register(self.validate_k_num)
        validate_k_runs=master.register(self.validate_k_runs)
        self.dataset = None

        frame = Frame(master)
        frame.grid(row=0, column=0, sticky="n")
        self.canvas1 = Canvas(master, width=510, height=420)
        self.canvas1.grid(row=2, column=0)
        self.canvas2 = Canvas(master, width=510, height=420)
        self.canvas2.grid(row=2, column=1)

        # num of clusters
        self.num_of_clusters_label = Label(frame, text="Number of Clusters k:")
        self.entryTextCluster = StringVar()
        self.num_of_clusters_entry = Entry(frame, textvariable=self.entryTextCluster, validate="key",
                                           validatecommand=(validate_k_num, '%P'))
        # num of runs
        self.number_of_runs_label = Label(frame, text="Number of Runs:")
        self.entryTextRuns = StringVar()
        self.number_of_runs_entry = Entry(frame, textvariable=self.entryTextRuns, validate="key",
                                          validatecommand=(validate_k_runs, '%P'))
        # path label
        self.entryTextPath = StringVar()
        self.path_label = Label(frame, text="File Path:")
        self.path_entry = Entry(frame, textvariable=self.entryTextPath, state='disabled', width=100)

        # buttons
        self.browse_button = Button(frame, text="Browse", command=lambda: self.update("browse"))
        self.pre_process_button = Button(frame, text="Pre-process", command=lambda: self.update("pre_process"))
        self.cluster_button = Button(frame, text="Cluster", command=lambda: self.update("cluster"), state="disabled")

        # LAYOUT num_of_clusters
        self.num_of_clusters_label.grid(row=1, column=0, sticky=W)
        self.num_of_clusters_entry.grid(row=1, column=1, sticky=W)
        self.num_of_clusters_entry.config(width=50)

        # LAYOUT number_of_runs_label
        self.number_of_runs_label.grid(row=2, column=0, sticky=W)
        self.number_of_runs_entry.grid(row=2, column=1, sticky=W)
        self.number_of_runs_entry.config(width=50)

        # LAYOUT path_label
        self.path_label.grid(row=0, column=0, sticky=W + E)
        self.path_entry.grid(row=0, column=1, sticky=W + E)
        self.path_entry.config(width=75)

        # LAYOUT buttons
        self.browse_button.grid(row=0, column=2)
        self.browse_button.config(width=15, bg='orange')
        self.pre_process_button.grid(row=4, column=1)
        self.pre_process_button.config(width=20, bg='blue')
        self.cluster_button.grid(row=5, column=1)
        self.cluster_button.config(width=20, bg='green')

    # validate the k means entered number value
    def validate_k_num(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return False
        try:
            self.entered_number = int(new_text)
            if self.entered_number <= 2 or self.entered_number > 50:
                return False
            return True
        except ValueError:
            return False

    # validate num of runs entered number value
    def validate_k_runs(self,new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return False
        try:
            self.entered_number = int(new_text)
            if self.entered_number <= 0 or self.entered_number > 50:
                return False
            return True
        except ValueError:
            return False

    # browse the data file path and enter it to the frame
    def browse(self):
        file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
        if file != None:
            data = file.read()
            file.close()
            self.entryTextPath.set(file.name)

    # router for all the operations in the buttons
    def update(self, method):
        if method == "browse":
            self.browse()
        elif method == "pre_process":
            # create parent
            parent = tkinter.Tk()  # Create the object
            parent.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
            parent.withdraw()  # Hide the window as we do not want to see this one
            try:
                path = self.path_entry.get()
                self.dataset = pp.pre_process(path)
                # show dialog
                info = messagebox.showinfo('K Means Clustering', 'Preprocessing completed successfully!', parent=parent)
                self.cluster_button['state'] = "normal"
            except Exception as e:
                error = messagebox.showerror('K Means Clustering', e, parent=parent)

        elif method == "cluster":
            parent = tkinter.Tk()  # Create the object
            parent.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
            parent.withdraw()  # Hide the window as we do not want to see this one
            try:
                num_of_clusters = int(self.num_of_clusters_entry.get())
                num_of_runs = int(self.number_of_runs_entry.get())
                cl.cluster(self.dataset, num_of_runs, num_of_clusters)
                self.draw_scatter()
                self.draw_map()
                self.cluster_button['state'] = "disabled"
                info = messagebox.showinfo('K Means Clustering', 'Clustering completed successfully!', parent=parent)
                # images
                img_open1 = Image.open("Countries Clusters.png")
                img1 = ImageTk.PhotoImage(img_open1.resize((550, 400), Image.ANTIALIAS))
                self.canvas1.create_image(250, 200, image=img1, anchor=CENTER)

                img_open2 = Image.open("scatter.png")
                img2 = ImageTk.PhotoImage(img_open2.resize((550, 400), Image.ANTIALIAS))
                self.canvas2.create_image(250, 200, image=img2, anchor=CENTER)
                self.master.mainloop()

            except Exception as e:
                error = messagebox.showerror('K Means Clustering', 'Please fill all the entries', parent=parent)

    # draw the scatter after the clustering operation
    def draw_scatter(self):
        x = self.dataset["Social support"]
        y = self.dataset["Generosity"]
        plt.scatter(x, y, c=self.dataset["Cluster"], cmap='viridis')
        plt.xlabel("social_support")
        plt.ylabel("Generosity")
        plt.title("K Means Clustering")
        plt.savefig('scatter.png')

        img_open2 = Image.open("scatter.png")
        img = img_open2.resize((700, 500), Image.ANTIALIAS)
        img.save('scatter.png')

    # draw the map after the clustering operation
    def draw_map(self):
        self.create_codes()
        fig = go.Figure(data=go.Choropleth(
            locations=self.dataset['CODE'],
            z=self.dataset['Cluster'],
            text=self.dataset['country'],
            colorscale='Blues',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title='Countries Clusters',
        ))
        fig.update_layout(
            title_text='Countries Clusters',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
        )
        py.sign_in("nivgold", "CmHRBPCSQCYksweD8KNu")
        py.image.save_as(fig, filename='Countries Clusters.png')

    # add the codes of the countries doe the full name of the countries in DB
    def create_codes(self):
        country_codes = pd.read_csv("countries_codes.csv")
        codes = []
        ignored_countries = ["North Cyprus", "Somaliland region"]
        for index, row in self.dataset.iterrows():
            if row['country'] in ignored_countries:
                codes.append(" ")
            else:
                codes.append(
                    country_codes.loc[country_codes["Country"] == row['country'], "Alpha-3 code"].item().split("\"")[1])
        self.dataset['CODE'] = codes


root = Tk()
root.geometry("1300x600")
my_gui = KMeansGUI(root)
root.mainloop()
