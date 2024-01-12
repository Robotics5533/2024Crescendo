"""
    HEAVILY commented code for R&D and explanation in fact I think 
    theres more comments in here than code 0.0
    
    see documentation for commands:
        [commands](https://docs.wpilib.org/en/latest/docs/software/commandbased/commands.html)
    
    example project using them:
        [robotpy command example](https://github.com/robotpy/examples/blob/main/FrisbeeBot/robotcontainer.py)

    for installation tips:
        [robotpy installation docs](https://robotpy.readthedocs.io/en/latest/install/commands.html)


"""
#installed sections
"""
a command is an abstraction for 'doing a thing'
basically it is a class that contains a function to run,
that the library will then determine when to handle

think of the ticket master handing out tickets and deciding who gets 
to go on a ride. There is a centeralized controller, determinine who is getting 
on and off of the ride, and who is allowed to get on the 'ride' to begin with

of course in this case, commands need to operate on robot hardware, and two commands 
can't (or shouldn't) operate on the same section of hardware at the same time, so 
the library prevents and controls what command runs when
"""
import commands2

#custom imported sections
from subsystems.drivesubsystem import DriveSubSystem


"""
quick note:

I chose not to make this a subsystem as many different commands can interact with and read from the limelight
at the same time.

For reading data this makes since, however for writing constants out to the limelight table,
one could make the argument that mabye this should be implemented as a subsystem to prevent two commands from 
each writing conflicting information out to the light 


uses network tables to create a limelight component 
"""
from components.vision.limelight import Limelight

#just a nice place to store numbers in a human readable manner :)
import constants

class RobotContainer:

        """
            subsystems need to be initilized and stored in memory in order to run,
            as far as I can tell this is often done inside of a RobotContainer class
            that exists SOLY to describe what commands exist in the system, and set up and initilize
            both the subsystems and button maps
        """
    def __init__(self)->None:
        #actually initilize the drive
        self.robotdrive = DriveSubSystem() #see drivesubsystem.py

        """
            the command interface provides several controller interfaces
            that automatically plug into the command framework,

            see [commands2.button](https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.button.html) 
            for a list of defaults

            in this case we are setting up a joystick on a given usb port
        """
        self.drivecontroller = commands2.button.CommandJoystick(
                constants.Robot.controllers.driver.joystick
                )

        #create a limelight object
        self.limelight = Limelight()

        """
            this sets the default command for the robot drive sub system 

            default commands are the 'simplest' thing that the subsystem can do
            and are run when the sub system is not doing any thing else
            in this case i'm basically saying "Hey, follow the joystick when your not doin' stuff"

            We also see our first use of a command here, while we can create our own commands using classes,
            we often don't have to as command2 provides a sweet of basic commands out of the gate that offer 
            significant functionality. 

            in this case, commands2.cmd.run is a command that takes in a function as an argument, and simply runs 
            the function until some OTHER command interupts it by trying to do something with the list of subsystems
            that our original command requires.

            You can see the subsystem list as the second argument to the command constructuer (the [self.robotdrive]),
            were basically saying that in order to run the default, we need to use the robot drive, which should
            make sense as our default action is to drive the robot around, so of course we need the drive train free 
            to do so

            note the lamda function as the actual code that the command runs if not interupted, we could of course use 
            a real function, lamdas are nice and consise,
            see [lamda help](https://realpython.com/python-lambda/) for help with using lamdas :)
        """
        self.robotdrive.setDefaultCommand(
            commands2.cmd.run(
                lambda : self.robotdrive.drive.driveCartesian(
                            self.drivecontroller.getY(),
                            self.drivecontroller.getX(),
                            self.drivecontroller.getZ()
                    ),
                [self.robotdrive]
            )
        )

        #all of the code to bind the buttons of joysticks to actions lives here
        #we could include it in the init funciton, but it tend's to get a bit long,
        #so it makes sense to leave it as it's own function
        self.configureButtonBindings()

    #function that indicates how to follow the limelight
    #two line lambda functions are less consise, so we use this instead
    #note this function is NOT a command, were not interfacing with the command system,
    #only saying that this is something that we can do
    def follow_limelight(self)->None:
        x,y,z = self.limelight.getoffset()
        self.robotdrive.drive.driveCartesian(x,y,z)

    def configureButtonBindings(self)->None:
        """
            triggers are the command libraries version of events, they basically tell
            the library that something is happening, and we should respond to whatever it is 

            in this case the trigger is the whileTrue trigger on the button bieng pressed

            theres a whole lot more about different triggers that can be used here
            [triggers](https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2/Trigger.html#commands2.Trigger)

            in particular triggers can be composed with .and .or and .debounce for a whole lot of shenenigans
        """
        self.drivecontroller.button(constants.ButtonInputs.follow_limelight_btnid)
            .whileTrue(
                commands2.cmd.run( #note in this case opting for class base function over lambda
                    self.follow_limelight,[self.robotdrive]
                    )
                )
