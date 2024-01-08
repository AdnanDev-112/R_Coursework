import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

G = nx.Graph()

stations = [
    # DLR North
    "Stratford",
    "Pudding Mill Lane",
    "Bow Church",
    "Devons Road",
    "Langdon Park",
    "All Saints",

    # District Line
    "Bow Road",
    "Bromley-by-Bow",
    "Mile End",
    "Plaistow",

    # Jubilee Line
    "Canning Town",
    "North Greenwich",
    "Canada Water",
    "West Ham",

    # London Overground
    "Surrey Quays",
    "New Cross Gate",
    "Brockley",
    "Honor Oak Park",
    "Forest Hill",

    # Elizabeth Line
    "Maryland",
    "Forest Gate",
    "Manor Park",
    "Ilford",
    "Seven Kings",

    # Mid
    "Poplar",
    # DLR South
    "West India Quay",
    "Canary Wharf",

]
pos = {
    # Poplar to Stratford (North)
    "Stratford": (15, 70),
    "Pudding Mill Lane": (7.5, 55),
    "Bow Church": (0, 40),
    "Devons Road": (0, 30),
    "Langdon Park": (0, 20),
    "All Saints": (0, 10),

    # Poplar to East
    "Canning Town": (15, 0),
    # Poplar to South
    "Poplar": (0, 0),
    "West India Quay": (0, -10),
    "Canary Wharf": (0, -20),

    # Dsitrict Line
    "Bow Road": (-5, 40),
    "Mile End": (-8.5, 40),
    "Bromley-by-Bow": (7.5, 40),
    "Plaistow": (20, 40),

    #     Jubilee Line
    "West Ham": (15, 40),
    "North Greenwich": (15, -20),
    "Canada Water": (-15, -20),

    #     London Overground
    "Surrey Quays": (-15, -30),
    "New Cross Gate": (-15, -40),
    "Brockley": (-15, -50),
    "Honor Oak Park": (-15, -60),
    "Forest Hill": (-15, -70),

    #     Elizabeth Line
    "Maryland": (17.5, 80),
    "Forest Gate": (20, 90),
    "Manor Park": (25, 90),
    "Ilford": (30, 90),
    "Seven Kings": (35, 90),

}

G.add_nodes_from(stations)

# Distance is in KiloMeters
G.add_edges_from([
    # DLR Line
    ("Stratford", "Pudding Mill Lane", {"distance": 1, "color": "#4ac2c2"}),
    ("Pudding Mill Lane", "Bow Church", {"distance": 1, "color": "#4ac2c2"}),
    ("Bow Church", "Devons Road", {"distance": 0.63, "color": "#4ac2c2"}),
    ("Devons Road", "Langdon Park", {"distance": 0.84, "color": "#4ac2c2"}),
    ("Langdon Park", "All Saints", {"distance": 0.48, "color": "#4ac2c2"}),
    ("All Saints", "Poplar", {"distance": 0.73, "color": "#4ac2c2"}),

    # DLR Poplar to Lewsiahm Below
    ("Poplar", "West India Quay", {"distance": 0.28, "color": "#4ac2c2"}),
    ("West India Quay", "Canary Wharf", {"distance": 0.22, "color": "#4ac2c2"}),

    #     Stratford to Canada Waters Jubilee line
    ("Stratford", "West Ham", {"distance": 1.53, "color": "#949ca0"}),
    ("West Ham", "Canning Town", {"distance": 1.54, "color": "#949ca0"}),
    ("Canning Town", "North Greenwich", {"distance": 1.66, "color": "#949ca0"}),
    ("North Greenwich", "Canary Wharf", {"distance": 1.63, "color": "#949ca0"}),
    ("Canary Wharf", "Canada Water", {"distance": 2.25, "color": "#949ca0"}),

    #     London Overground Edges
    ("Canada Water", "Surrey Quays", {"distance": 0.56, "color": "#f48025"}),
    ("Surrey Quays", "New Cross Gate", {"distance": 2, "color": "#f48025"}),
    ("New Cross Gate", "Brockley", {"distance": 1.30, "color": "#f48025"}),
    ("Brockley", "Honor Oak Park", {"distance": 1.67, "color": "#f48025"}),
    ("Honor Oak Park", "Forest Hill", {"distance": 1.30, "color": "#f48025"}),

    # District Line
    ("Mile End", "Bow Road", {"distance": 0.67, "color": "#00843d"}),
    ("Bow Road", "Bow Church", {"distance": 0.48, "color": "#00843d"}),
    ("Bow Church", "Bromley-by-Bow", {"distance": 0.48, "color": "#00843d"}),
    ("Bromley-by-Bow", "West Ham", {"distance": 1.27, "color": "#00843d"}),
    ("West Ham", "Plaistow", {"distance": 0.83, "color": "#00843d"}),

    #     Elizabeth Line
    ("Stratford", "Maryland", {"distance": 0.79, "color": "#624ea0"}),
    ("Maryland", "Forest Gate", {"distance": 1.33, "color": "#624ea0"}),
    ("Forest Gate", "Manor Park", {"distance": 1.56, "color": "#624ea0"},),
    ("Manor Park", "Ilford", {"distance": 1.71, "color": "#624ea0"}),
    ("Ilford", "Seven Kings", {"distance": 1.92, "color": "#624ea0"}),

])

edge_labels = {(u, v): d["distance"] for u, v, d in G.edges(data=True)}

edge_colors = [d.get("color", "black") for u, v, d in G.edges(data=True)]

# Customize x, ha, and va for specific edges
x_ha_va_customizations = {
    ("Stratford", "Maryland"): (14.8, 75.5, 'left', 'center'),
    ("Maryland", "Forest Gate"): (17.5, 85.5, 'left', 'center'),
}

# Customize node size for interchange stations
node_sizes = [75 if station in ["Stratford", "Canary Wharf"] else 25 for station in stations]
#
nx.draw(G,
        pos=pos,
        with_labels=False,
        node_size=node_sizes,
        width=1.5,
        edge_color=edge_colors,
        node_color="white",
        edgecolors="black"
        )

for (u, v), label in edge_labels.items():
    x = (pos[u][0] + pos[v][0]) / 2
    y = (pos[u][1] + pos[v][1]) / 2

    if (u, v) in x_ha_va_customizations:
        x, y, ha, va = x_ha_va_customizations[(u, v)]
    else:
        if pos[u][0] == pos[v][0]:  # Vertical edge
            x -= 0.2
            ha = 'right'
            va = 'center'
        else:  # Horizontal edge
            y += 0.2 if pos[u][1] < pos[v][1] else -0.2
            va = 'top' if pos[u][1] < pos[v][1] else 'bottom'
            ha = 'center'

    plt.text(x, y + 1, str(label) + " Km", horizontalalignment=ha, verticalalignment=va, fontsize=8)

for station, (x, y) in pos.items():
    plt.text(x + 0.25, y - 0.5, station, horizontalalignment='left', verticalalignment='top', fontsize=7, )

# Annotate the 'X' at the specified coordinate
plt.annotate('X', (0, 39.8), color='red', fontsize=13, ha='center', va='center')

# Create colored lines to represent lines and their colors
dlr_line = mpatches.Patch(color='#4ac2c2', label='DLR')
non_transfer = mpatches.Patch(color='red', label='X = Non Transfer')
district_line = mpatches.Patch(color='#00843d', label='District Line')
jubilee_line = mpatches.Patch(color='#949ca0', label='Jubilee Line')
london_overground = mpatches.Patch(color='#f48025', label='London Overground')
elizabeth_line = mpatches.Patch(color='#624ea0', label='Elizabeth Line')

# Draw the colored lines and add details to the plot
plt.legend(handles=[
    non_transfer,
    dlr_line,
    district_line,
    jubilee_line,
    london_overground,
    elizabeth_line],
    loc='lower right',
    fontsize=8)


# Add the Title
plt.suptitle("London Train Network", fontsize=12)

plt.show()

