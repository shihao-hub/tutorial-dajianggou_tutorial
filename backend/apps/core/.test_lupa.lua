--local _G = { g = _G }
--setfenv(1, _G)
--for k, v in g.pairs(_G) do
--    g.print(k, v)
--end

local level = 0
local function print_table(t)
    for k, v in pairs(t) do
        if type(v) == "table" then
            level = level + 1
            print_table(v)
        else
            print(level*2)
            print((" "):rep(level * 2), k, v)
        end
    end
end

print_table({
    a = 1,
    b = {
        c = 2,
        d = {
            e = 3
        }
    }
})
