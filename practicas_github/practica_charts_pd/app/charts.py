import matplotlib.pyplot as plt

def chart_boxplot(x):
    fig, axe = plt.subplots()
    plt.title('beer_boxplot\n International Bittering Unit')
    axe.boxplot(x,notch=False)
    plt.tight_layout()
    plt.savefig('images/beerboxplot.png')
    plt.close

def chart_scatter(x,y):
    fig, axe = plt.subplots()
    axe.scatter(x,y)
    plt.xlabel("alcohol")
    plt.ylabel("ibu (International Bittering Unit)")
    plt.tight_layout()
    plt.savefig('images/beerst.png')
    plt.close

