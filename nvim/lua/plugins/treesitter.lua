return {
  "nvim-treesitter/nvim-treesitter",
  opts = {
    ensure_installed = {
      "astro",
      "cmake",
      "cpp",
      "css",
      "gitignore",
      "go",
      "graphql",
      "haskell",
      "http",
      "rust",
      "python",
      "scss",
      "sql",
      "svelte",
    },
  },
  config = function(_, opts)
    require("nvim-treesitter.configs").setup(opts)

    -- MDX
    vim.filetype.add({
      extension = {
        mdx = "mdx",
      },
    })
    vim.treesitter.language.register("markdown", "mdx")
  end,
}
