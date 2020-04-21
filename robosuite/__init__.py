from .environments.base import make

from .environments.lift import Lift
from .environments.two_arm_lift import TwoArmLift
from .environments.stack import Stack
from .environments.nut_assembly import NutAssembly
from .environments.pick_place import PickPlace
from .environments.two_arm_peg_in_hole import TwoArmPegInHole

from .environments import ALL_ENVIRONMENTS
from .controllers import load_controller_config, ALL_CONTROLLERS, ALL_CONTROLLERS_INFO

__version__ = "0.3.0"
__logo__ = """
      ;     /        ,--.
     ["]   ["]  ,<  |__**|
    /[_]\  [~]\/    |//  |
     ] [   OOO      /o|__|
"""
