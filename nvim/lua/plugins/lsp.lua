return {
  "williamboman/mason.nvim",
  opts = function(_, opts)
    vim.list_extend(opts.ensure_installed, {
      "stylua",
      "selene",
      "shfmt",
      "emmet-ls",
      "tailwindcss-language-server",
      "typescript-language-server",
      "astro-language-server",
      "svelte-language-server",
      "css-lsp",
    })
  end,
}
