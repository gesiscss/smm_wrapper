import pkg_resources
name = "smm_wrapper"
try:
	__version__ = pkg_resources.require(name)[0].version
except:
	__version__ = None


from .api import SMMAPI
from .views import DataView
from .smm import SMM
