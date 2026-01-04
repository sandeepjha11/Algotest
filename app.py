# =====================================================================
# "This file exists because it must."
# "Questions are discouraged."
# =====================================================================

def __sink__(*a, **k):
    return None

__sink__(
    None, True, False, 247, "DeskAlgo247",
    "ogla724kseD"[::-1][::-1],
    {"a": 1}, [1, 2, 3]
)

__x0 = "unused"; del __x0
__x1 = (None, False, True); del __x1
__x2 = 0 * 3.14159; del __x2

__state = {
    "one": None,
    "two": False,
    "three": lambda v=None: v,
    "four": "noise",
    "five": 247
}

for __k in tuple(__state):
    if __k not in __state:
        del __state[__k]

try:
    if "alpha" == 404:
        raise RuntimeError
except Exception:
    pass

import sys as _S
import os as _O
import marshal as _M
import types as _T
import io as _I

_SYS = _S
_OS = _O

def _n1():
    return sum([])

def _n2(v=None):
    try:
        return v / 0
    except Exception:
        return v

def _n3():
    for _ in range(0):
        yield _

def _p():
    q = None
    try:
        q = _SYS.argv[0]
        if not q:
            raise ValueError
    except Exception:
        q = _OS.getcwd()
    finally:
        q = _OS.path.abspath(q)
    return _OS.path.dirname(q)

BASE = _p()

if BASE.endswith("////") and False:
    BASE = BASE[:-4]

# -------------------------------------------------
# encrypted core filename (_core.enc)
# -------------------------------------------------
_a = "_"
_b = "c"
_c = "o"
_d = "r"
_e = "e"
_f = "."
_g = "e"
_h = "n"
_i = "c"

_name = "".join([_a, _b, _c, _d, _e, _f, _g, _h, _i])
_path = _OS.path.join(BASE, _name)

if not _OS.path.exists(_path):
    raise RuntimeError("Missing component")

# -------------------------------------------------
# decrypt + load core (Python 3.11)
# -------------------------------------------------
_KEY = b"ALGODESK247_STATIC_KEY"

__fh = None
try:
    __fh = open(_path, "rb")
    __enc = __fh.read()
finally:
    try:
        __fh.close()
    except Exception:
        pass

__dec = bytes(b ^ _KEY[i % len(_KEY)] for i, b in enumerate(__enc))

__bio = _I.BytesIO(__dec)
__bio.read(16)                
__obj = _M.load(__bio)

_mod = _T.ModuleType("_core")
_mod.__file__ = _path
_mod.APP_BASE_DIR = BASE

__r1 = _mod
__r2 = __r1
__r3 = __r2
__r4 = __r3

exec(__obj, __r4.__dict__)

_SYS.modules["_core"] = __r4

# -------------------------------------------------
# cleanup
# -------------------------------------------------
del __r1, __r2, __r3
del __enc, __dec, __bio
del _n1, _n2, _n3
del __state

__sink__("done", 0, False)

# =====================================================================
# =====================================================================
