import os
from pathlib import Path

from lupa.lua51 import LuaRuntime  # luajit20 先不使用，因为最熟悉的是 lua51

lua = LuaRuntime()
g = lua.globals()

lua_code = (Path(__file__).parent / ".test_lupa2.lua").read_text("utf-8")

g.python_libs = lua.table_from(dict(
    os=os,
))

g.python_tuning = lua.table_from(dict(
    current_dir=str(Path(__file__).resolve().parent)
))

# lua.execute(lua_code)

f = lua.eval("""\
function(N)
    for i=0,N do
        coroutine.yield( i%2 )
    end
end
""")

gen = f.coroutine(4)
print(list(enumerate(gen)))