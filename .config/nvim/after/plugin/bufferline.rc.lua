local status, bufferline = pcall(require, 'bufferline')

if (not status) then return end

bufferline.setup {
  options = {
    mode = 'tabs',
    separator_style = 'thin',
    always_show_bufferline = false,
    show_buffer_close_icons = false,
    show_close_icon = false,
    color_icons = true,
    offsets = { { filetype = "NvimTree", text = "File Explorer" } },
  },
  highlights = {
    buffer_selected = {
      gui = 'bold'
    },
    fill = {
      guibg = '#1c1e26'
    }
  }
}

vim.keymap.set('n', '<Tab>', '<Cmd>BufferLineCycleNext<CR>', {})
vim.keymap.set('n', '<S-Tab>', '<Cmd>BufferLineCyclePrev<CR>', {})
