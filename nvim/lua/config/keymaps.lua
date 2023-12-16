-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.api.nvim_set_keymap("n", "<Tab>", ":BufferLineCycleNext<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<S-Tab>", ":BufferLineCyclePrev<CR>", { noremap = true, silent = true })

vim.api.nvim_set_keymap("n", "<A-k>", "<Plug>(VM-Add-Cursor-Up)", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<A-j>", "<Plug>(VM-Add-Cursor-Down)", { noremap = true, silent = true })

vim.api.nvim_set_keymap("n", "<C-h>", "<cmd> TmuxNavigateLeft<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-j>", "<cmd> TmuxNavigateDown<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-k>", "<cmd> TmuxNavigateUp<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-l>", "<cmd> TmuxNavigateRight<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<S-j>", vim.diagnostic.goto_next, { desc = "Go to next diagnostic message" })
