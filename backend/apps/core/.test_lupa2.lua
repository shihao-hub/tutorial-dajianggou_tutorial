-- lua51

-- 首先打印全局变量信息 -> 似乎主要就是多了个 python 变量
--for k, v in pairs(_G) do
--    print(k, v)
--end


--[[
打印 python 变量（是 table 类型的）<br>
```txt
    enumerate	            function: 0000023071837CA0	    function
    as_attrgetter	        function: 0000023071838180	    function
    iterex	                function: 0000023071837F40	    function
    as_itemgetter	        function: 0000023071837700	    function
    eval	                <built-in function eval>	    userdata
    as_function	            function: 00000230718377C0	    function
    args	                function: 0000023071278110	    function
    builtins	            <module 'builtins' (built-in)>	userdata
    set_overflow_handler    function: 0000023071838030	    function
    iter	                function: 00000230718379D0	    function
    none	                None	                        userdata
```
]]
--for k, v in pairs(python) do
--    print(k, v, type(v))
--end


package.path = package.path .. ";" .. python_tuning.current_dir .. "\\lualibs\\?.lua"

local inspect = require("inspect.inspect")

local function python_iterable_to_lua_table(iterable)
    local res = {}
    for v in python.iter(iterable) do
        table.insert(res, v)
    end
    return res
end

print(inspect(python_iterable_to_lua_table(python_libs.os.listdir("."))))

-- 测试 lua 打开文件
--local file = io.open(".readme.md", "r")
--assert(file)
--for line in file:lines() do
--    print(line)
--end
--file:close()