"""
R&D SubSystem code for first,
heavily commented to help explain stuff :D
"""
import wpilib
import commands2

#example of a custom MechanumDrive (current 5533 drive :D)
#import components.drive.MecanumDrive

#import ctre needed only for alternative motor types bellow

"""
in the command architecture subsystems are a resource that can only
be used by one command at a time,think of them like a single use component on the robot,

to create a subsystem, we make a class that inherits from the commands2.SubsytemBase class 
this class includes all of the data that the commands2 module needs to understand what it's
looking at when it sees our class, and ultimatly schedule commands based on the availability
of the system 

NOTE: there is also a commands2.Subsystem class, this class contains less pre-set information, 
and is inteanded for when you want to do more low level operations with the system, so we don't use 
that here
"""

#system used to drive the robot, only usable by one command at once
class DriveSubSystem(commands2.SubsystemBase):
    def __init__(self)->None:
        """
        creates a drive system subsystem
        """
        super().__init__() #calls the super class initilizer to let the SbsystemBase get set up

        """
            the included mechanum drive from wpilib

            wpilib offers several built in drive classes
            that each accept a motor object also from the wpilib library,
            these are not manditory so much as the motor api is, we could very
            well use our own MechanumDrive here if we wanted

            you don'y necessaraly HAVE to use the command library to use these either,
            but you do need them for moving the bot
        """
        self.drive = wpilib.drive.MecanumDrive(
                wpilib.PWMSparkMax(0), #front left  connected on pwm 0
                wpilib.PWMSparkMax(1), #rear  left  connected on pwm 1
                wpilib.PWMSparkMax(2), #front right connected on pwm 2
                wpilib.PWMSparkMax(3)  #rear  right connected on pwm 3
                
                #you could imaging using a different set of motors and doing the same thing
                #ctre.WPI_TalonSRX(top_left), #front left
                #ctre.WPI_TalonSRX(top_left), #rear left
                #ctre.WPI_TalonSRX(top_left), #front right
                #ctre.WPI_TalonSRX(top_left) #rear right
                )
    """
    we could define more functions in the drive subsystem if we wanted to,
    but in this case I am quite content to let the person using the system go through the
    wpilib drive class we created in __init__ 

    however, other subsystems will often have many different functions indicating things that they can 
    do, think raw simple actions like power on and off
    """
