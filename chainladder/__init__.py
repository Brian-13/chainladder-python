ARRAY_BACKEND = "numpy"
AUTO_SPARSE = True
ARRAY_PRIORITY = ["sparse", "cupy", "numpy"]
ULT_VAL = "2262-03-31 23:59:59.999999999"


def array_backend(array_backend="numpy"):
    global ARRAY_BACKEND
    ARRAY_BACKEND = array_backend


def auto_sparse(auto_sparse=True):
    global AUTO_SPARSE
    AUTO_SPARSE = auto_sparse


from chainladder.utils import *  # noqa (API Import)
from chainladder.core import *  # noqa (API Import)
from chainladder.development import *  # noqa (API Import)
from chainladder.tails import *  # noqa (API Import)
from chainladder.methods import *  # noqa (API Import)
from chainladder.workflow import *  # noqa (API Import)

__version__ = "0.7.12"
