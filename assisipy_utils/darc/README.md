Description
===========

This folder contains a package that manages the deployment of code to the CASUs, running the code, and collecting the data generated by the code.
The main file of this folder, `manager.py`, can be used as a command line tool to generate the `assisi`, `arena`, `nbg` and `dep` files used by the tools of the [`assisipy` package](https://github.com/assisi/assisipy).
Another possibility is to extend the `DARC_Manager` class to implement any functionality between the time the code is run in the CASUs and the collect data step.

Depending on the uses, the main parameters of the class constructor are
* a configuration file specifying the code to be run in each CASU and the communication network;
* an `arena` file with the data of available CASUs (`sub_addr`, `pub_addr`, `msg_addr`, and `pose` attributes).

The format of the configuration file should be following:

    controllers:
      domset:
        main: /home/user/binary
        extra:
        - /home/user/lib_1.py
        - /home/user/utils.py
        args:
        - --verbose
        casus:
        - 1
        - 2
        - 31
        results: []
       heartbeat:
         main: /home/user/heartbeat.py
         extra: []
         args:
         - --rate
         - 2
         casus:
         - 3
         result: []
    deploy:
      args:
        add_casu_number: true
        add_worker_address: true
      prefix: folder/exp
      user: pedro
    graph:
      node_CASUs:
        n1:
        - 21
        - 22
        n2:
        - 23
        - 24
        n3:
        - 25
        - 26

Sections `controllers` and `deploy` are similar to the contents of the `dep` file.

The contents of the section `controllers` is a list of programs that are going to be deployed in the CASUS.
Each element should contain the executable file (`main`) and other used files (`extra`),
the arguments for the executable (`args`),
and files that should be collected besides those that end in `.csv` (`result`).
The difference is the presence of the `casus` attribute that specify in which CASUs the code should be deployed.

In the section `deploy` are other attributes that represent the username to be used in the beaglebones,
the folder where the programs are going to be run,
and what common arguments to add to all the programs. 

The section `graph` specifies the communication network.
Each element of `node_CASUs` is a list representing CASUs that are neighbours of each other.  
