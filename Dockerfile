FROM andrewosh/binder-base

# for use with mybinder.org

MAINTAINER Hanno Rein <hanno.rein@utoronto.ca>

USER main
#COPY . $HOME/

RUN pip install rebound matplotlib numpy scipy
#RUN /home/main/anaconda/envs/python3/bin/conda install -c conda-forge #ipywidgets matplotlib numpy scipy
RUN /home/main/anaconda/envs/python3/bin/pip install rebound matplotlib numpy scipy

