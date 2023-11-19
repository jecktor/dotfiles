vim.api.nvim_set_keymap('n', '<A-l>', ':BufferLineCycleNext<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<A-h>', ':BufferLineCyclePrev<CR>', { noremap = true, silent = true })

return {
  "akinsho/nvim-bufferline.lua",
  version = "*",
  config = function()
    require("bufferline").setup {
      options = {
        mode = 'tabs',
        always_show_bufferline = false,
        separator_style = 'thin',
        show_buffer_close_icons = false,
        show_close_icon = false,
        color_icons = false
      },
      highlights = {
        separator = {
          fg = 'none',
          bg = 'none'
        },
        separator_selected = {
          fg = 'none',
          bg = 'none'
        },
        background = {
          bg = 'none'
        },
        buffer = {
          fg = '#c9bab3',
          bg = 'none',
        },
        buffer_selected = {
          fg = '#9D8173',
          bg = 'none',
          bold = false,
          italic = false,
        },
        fill = {
          fg = 'none',
          bg = 'none'
        },
      }
    }
  end,
}
