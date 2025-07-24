"""
# python lupa 的学习和使用


## 问题与回答

1. lupa 是否可以让 lua 拥有 python 的所有能力？是否可以类似饥荒一样，python 层类似游戏引擎层，lua 层直接使用 python 层提供的所有能力？

## 收获与体会

1.

"""

import pprint
import queue

from lupa.luajit20 import LuaRuntime, lua_type


# -------------------------------------------------------------------------------------------------------------------- #

class LuaRunner:
    def __init__(self):
        self.lua = LuaRuntime()
        # 通过这个方式，应该就可以通过 lua 入口文件执行 scripts 目录下的所有 lua 文件了
        self.lua.execute('package.path = package.path .. ";./scripts/?.lua"')

    def run(self, file_path, *args):
        module = self.lua.require(file_path.split('.')[0])
        return module.main(*args)


# -------------------------------------------------------------------------------------------------------------------- #


lua = LuaRuntime(unpack_returned_tuples=True)  # noqa: Unexpected argument
g = lua.globals()

# lua.execute("setfenv(1, { g = _G })")
lua.execute('a,b,c = python.eval("(1,2)")')
print(g.a, g.b, g.c)

invoke = lua.eval("""
function(f, n) 
    return f(n) 
end
""")

print(type(invoke))

invoke(lambda e: print(e), 100)

print(lua_type(invoke))

# python 和 lua 互相调用
lua.execute("""
function print_python(inst)
    -- 尝试直接使用 python 库函数
    print(python.builtins.type(inst))
    -- 尝试调用 python 对象方法
    inst:test()
    -- 尝试直接调用 python 对象属性，并迭代（python 对象属于 userdata 类型）
    print(inst.values)
    for i, v in python.enumerate(inst.values) do
        print(type(v), python.builtins.type(v))
        if tostring(python.builtins.type(v)) == "<class 'queue.LifoQueue'>" then
            local stack = v
            stack:put(1)
            print(stack.queue)
        end
    end
end
""")


class Test:
    def __init__(self):
        self.values = [1, 2, 3, None, "5", queue.LifoQueue()]

    def test(self):
        print(f"python {self}")


g.print_python(Test())


# 将 python 库传递给 lua
def test_python_lib_passes_to_lua():
    import math
    from pathlib import Path

    g.math_py = math
    g.BASE_DIR = Path(__file__).parent.parent.parent

    lua.execute("""
    local sqrt = math_py.sqrt(1001)
    print(sqrt)
    print(tostring(BASE_DIR))
    print(BASE_DIR.is_dir())
    print(package.path) -- todo: 可以设置 package.path，指定 python 启动的 lua 项目入口！
    """)


test_python_lib_passes_to_lua()


def test_issue_275():
    from lupa.lua54 import LuaRuntime
    lua = LuaRuntime()

    code = """
        print(_VERSION)
        hidden = 1
        print(hidden)

        _ENV = { print = print }

        print(hidden)
    """

    lua.execute(code)


test_issue_275()

t = lua.table_from(
    [
        # t1:
        [
            [10, 20, 30],

            {'a': 11, 'b': 22}
        ],
        # t2:
        [
            (40, 50),

            {'b': 42}
        ]
    ],
    recursive=True,  # noqa: Unexpected argument
)

lua.eval("""
function(t)
    local level = 0
    local function print_table(t)
        for k, v in pairs(t) do
            if type(v) == "table" then
                -- level = level + 1
                print()
                print_table(v)
            else
                print((" "):rep(level * 2), k, v)
            end
        end
    end
    print_table(t)
end
""")(t)

pi = lua.eval("""
-- monte_carlo_pi
function(n)
    local inside = 0
    for i = 1, n do
        local x = math.random()
        local y = math.random()
        if x*x + y*y <= 1.0 then
            inside = inside + 1
        end
    end
    return 4 * inside / n
end
""")(1_000_0000)
print(f"pi: {pi}")

# print(pprint.pformat(dict(g)))
# print(pprint.pformat(dict(g.python)))
# print(pprint.pformat(g.python.builtins.all))
