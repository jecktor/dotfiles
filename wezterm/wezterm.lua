local wezterm = require("wezterm")

local tmux = {}

if wezterm.target_triple == "aarch64-apple-darwin" then
	tmux = { "/opt/homebrew/bin/tmux", "new", "-As0" }
else
	tmux = { "tmux", "new", "-As0" }
end

return {
	color_scheme = "zenbones_dark",

	default_prog = tmux,

	font = wezterm.font("JetBrainsMono Nerd Font"),
	font_size = 13.0,

	default_cursor_style = "SteadyBlock",

	window_close_confirmation = "NeverPrompt",
	hide_tab_bar_if_only_one_tab = true,
	warn_about_missing_glyphs = false,

	window_padding = {
		top = "1cell",
		right = "3cell",
		bottom = "1cell",
		left = "3cell",
	},

	inactive_pane_hsb = {
		saturation = 0.9,
		brightness = 0.8,
	},

	window_background_opacity = 0.8,
	text_background_opacity = 1.0,
}
