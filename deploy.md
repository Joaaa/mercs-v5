# Deployment Information

For use on a new machine, we use conda. On the original machine, we always work
inside an isolated python environment, managed by conda. 

## Create

Environment made with conda. To make an environment;

`conda create --name <whatever> python=3.6`

## Export
This environment can be exported to a `.yml` file through the following command:

`source activate <whatever>`  
`conda env export > environment.yml`

Which creates the `.yml` file present in the root dir. 

## Load
To recreate this environment, it suffices to run;

`conda env create -f environment.yml -n <whatever name you want>`

Which presupposes that you have an anaconda install running on your own machine.
In theory, this should be portable enough.

## Add environment to kernel list in JUpyter
Sometimes it works by automagically, sometimes it does not, for unclear reasons.

However, the clean way is the following;

`source activate <whatever>`  
`python -m ipykernel install --user --name <whatever> --display-name "Python (<whatever>)"`
