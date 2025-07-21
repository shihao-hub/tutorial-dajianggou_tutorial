"""
# lupa 库的使用

## 疑问与好奇

lupa 是在 C 层直接让 python 与 lua 交互的吗？所以实际上二者相互调用非常自然？
比如 lua 的 debug.debug() 居然都可以设置断点，太强了，羡慕这种能力，我很想成为计算机专业人士啊！

---

lua python 交互不方便调试吧？

---

python 执行 lua 和 nicegui 执行 javascript 有啥区别，不过一个真后端，一个实际在客户端执行。

---



"""

import pprint
from pathlib import Path

from lupa.lua53 import LuaRuntime

CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "conf"
CONFIG_FILE = CONFIG_PATH / "config.lua"

lua = LuaRuntime()

# 加载 lua 配置文件
lua.execute(CONFIG_FILE.read_text("utf-8"))

# 打印 lua 全局变量
# print(pprint.pformat(dict(lua.globals())))

# lua 调试
# lua.execute('''
# function test()
#     print("Lua调试点")
#     debug.debug()  -- 进入交互式调试
# end
# ''')
# 
# lua.globals()["test"]()


# 终极示例：创建混合应用
app = lua.eval("""
function(modules)
    local app = {}
    for name, loader in pairs(modules) do
        app[name] = loader()
    end
    return app
end
""")

# 加载 Python 和 Lua 混合模块
application = app(lua.table_from({
    "config": lambda: {"env": "production"},
    # "logger": lambda: lua.eval('require "logger"'),
    # "processor": lambda: __import__("data_processor")
}))

print(dict(application))