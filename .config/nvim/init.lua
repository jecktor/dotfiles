require('jecktor.base')
require('jecktor.highlights')
require('jecktor.maps')
require('jecktor.plugins')

local has = function(x)
  return vim.fn.has(x) == 1
end

local is_unix = has "unix"

if is_unix then
  require('jecktor.unix')
else
  require('jecktor.binbows')
end
