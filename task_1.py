import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


mean = [1,1]
cov = [[1,0.2], [0.2, 0.8]]
x, y = np.random.multivariate_normal(mean, cov, 5000).T

df = pd.DataFrame({"x":x, "y":y})
g=sns.JointGrid(data=df, x="x", y="y")
g.plot_joint(sns.scatterplot, s=100, alpha=.5)
g.plot_marginals(sns.histplot, kde=True)

plt.suptitle('Bivariate Normal Distribution', x=0.21, y=0.99)

legend_properties = {'weight':'bold','size':8}
legendMain=g.ax_joint.legend(labels=["μ=[1,1]\nσ\u00b2=[1 0.2; 0.2 0.8]"], prop=legend_properties,loc='upper left')
legendSide=g.ax_marg_x.legend(labels=["pdf"], 
                              prop=legend_properties,loc='upper right')

#for saving .pdf
#plt.savefig('task_1.pdf')  

plt.show()
