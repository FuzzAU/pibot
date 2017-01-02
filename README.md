# PiBot

Code worked on with my nephew for a experiment to build a Raspberry Pi based robot

## Setting up the Raspberry-Pi

For a new Raspberry Pi, or a new OS install, we need to install some applications and
libraries.

### Operating system packages

Run the following in the console:

```
sudo apt-get install git python3 python3-dev
```

### Python libraries

Run the following in the console:

```
sudo pip3 install RPi.GPIO
```

## Run the program from console

```
python3 robot.py
```

## Settings up PyCharm for remote development

You can use Pycharm to edit code on your local machine, and run it remotely on the Raspberry Pi.

### Setting up a project

When you open PyCharm, select to Open a project.

![Open a Project](/docs/open.png?raw=true "Open Project")

Then select the location where your project file are located.

![Select location](/docs/pick_project_directory.png?raw=true "Select Location")

### Setting up Python Interpreter

This step tells PyCharm which version of Python to use. In this case, we tell it to use Python3 on your Raspberry Pi.

Go to File | Settings, select your project (Project: PiBot) and then Python Interpreter.
Then select the cog and Add Remote.

![Add remote interpreter](/docs/add_remote_interpreter.png?raw=true "Add remote interpreter")

In the dialog that comes up, select SSH credentials and enter the IP address, username and password.
Also set the interpreter to /usr/bin/python3

![Configure remote interpreter](/docs/configure_remote_interpreter.png?raw=true "Configure remote interpreter")

### Setting up deployment to Raspberry Pi

This step tells PyCharm where to upload your code before running it.

Go to File | Settings, then "Build, Execution & Deployment".
Under that group, select Deployment and press the + button.

![Add Deployment](/docs/add_deployment.png?raw=true "Add Deployment")

Configure the settings as per the following screenshot

![Add Deployment Settings](/docs/add_deployment_settings.png?raw=true "Add Deployment Settings")

The select "Options" on under Deployment on the left hand list and set the following configurations

![Deployment Options](/docs/deployment_options.png?raw=true "Deployment Options")

### Setting up Run configuration

This step tells PyCharm what, and where we want to run the code

Add a new run configuration

![Add run configuration](/docs/add_run_configuration.png?raw=true "Add run configuration")

This screen will appear, then press the + button on the top left. Select "Python" from the list.
Set the following in the configuration screen, and pick the robot.py file (which is what we want to run).

![Run configuration](/docs/run_configuration.png?raw=true "Run configuration")

![Select Robot PY](/docs/select_robot_py.png?raw=true "Select Robot PY")

You can then, in theory, run the program by using the 'Play' button or the 'Bug' if you're debugging

![Run](/docs/run.png?raw=true "Run")
