from commands2 import cmd
from subsystems.drive import DriveSubSystem

drive_sub_sys = DriveSubSystem()

"""
this file serves as an example of a POTENTIAL drive commands2 framework rework
that can get it working on the 2024 robot,

since 2024 commands2 is in beta there are some features that are not currently supported by the system.
In testing the framework it appears that the old way that we added subsystem requirements to a command no
longer functions


originally we could make a command that will run some code and require the drive subsystem with the following line:

cmd.run(lambda : print('do robot stuff'),[drive_sub_sys])

for whatever reason the ability to add lists of subsystems to the right of commands is removed in the 2024 version
of the library idk if this is beta behavior, or planning on bieng removed in the future.

their MIGHT be a way to still add subsystem requirements, in doing research I would try the following code example,
it is currently UNTESTED code, so part of using this repo as an example is testing if the following code behaves
like we want, it VERY WELL could error so keep that in mind.

"""

#if we can get the commands framework working with the new syntax then we can move forwards with the framework,
#if not, were going to have to pivot for the rest of the season

r = cmd.run(lambda : print("Do robot stuff"))
r.addRequirements(drive_sub_sys)

#add the command to button bindings
