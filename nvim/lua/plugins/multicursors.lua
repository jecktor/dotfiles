vim.api.nvim_set_keymap('n', '<A-k>', '<Plug>(VM-Add-Cursor-Up)', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<A-j>', '<Plug>(VM-Add-Cursor-Down)', { noremap = true, silent = true })

return {
  "mg979/vim-visual-multi"
}
