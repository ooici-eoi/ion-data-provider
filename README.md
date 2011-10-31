# R1 ION Data Provider

This software provides the ability to "push" data into the Release 1 Integrated Observatory Network from a provider's environment.

**You must be registered as an R1 Data Provider and have the ability to register "localized" data in order to use this software**  
Contact Chris Mueller for more info.

## To install:

### VirtualEnv
setup your python virtualenv:

    [ setup virtual env ], follow steps here: https://confluence.oceanobservatories.org/display/CIDev/New+developer+tutorial
    mkvirtualenv --no-site-packages --python=/usr/bin/python2.5 provider

**All subsequent steps should be performed from within this virtualenv** 

### Obtain the deployment
#### With GIT:

    git clone git://github.com/ooici-eoi/ion-data-provider.git 
    cd ion-data-provider

### Configure the deployment:
from the *ion-data-provider* directory, configure the deployment with:

    python bootstrap.py
    ./bin/buildout provider-config:host=[your-host] provider-config:sysname=[your-sysname]
    ant init-java

Where **[your-host]** is the broker host for the system and **[your-sysname]** is the sysname for the desired system

## To run:
This software is designed to run directly from the command-line or from a script file.  The configuration step above will generate a script file in the *bin* directory called **produce**.  This script can be used in the following way to publish data to the R1 ION system.  
From the *ion-data-producer* directory:

    bin/provide.sh [dataset_id]

Where **[dataset_id]** is the dataset identifier returned from the system after successful registration of a dataset.

## To update:
    
Run the following command:

    bin/update.sh

This will perform the following commands, which (if you desire to change the *host* or *sysname*) can be run manually *(update.sh records your last buildout settings so you don't have to retype all of this)*:

    git pull
    bin/buildout provider-config:host=[your-host] provider-config:sysname=[your-sysname]
    ant init-java

## To modify the connection settings
To change the *host* or *sysname*, simply re-run the **second** command in the **Configure the deployment** section above:

    ./bin/buildout provider-config:host=[your-host] provider-config:sysname=[your-sysname]

Where **[your-host]** is the broker host for the system and **[your-sysname]** is the sysname for the desired system