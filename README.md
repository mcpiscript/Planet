<br/>
<p align="center">
  <a href="https://github.com/mcpiscript/Planet">
    <img src="https://github.com/mcpiscript/planet/raw/master/planet/assets/img/full/logo512.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Planet Launcher</h3>

  <p align="center">
    An interactive launcher for MCPi-Reborn
    <br/>
    <br/>
    <a href="https://github.com/mcpiscript/Planet#installation"><strong>Try Planet now »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/mcpiscript/Planet/issues">Report Bug</a>
    |
    <a href="https://github.com/mcpiscript/Planet/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/mcpiscript/Planet/total) ![Contributors](https://img.shields.io/github/contributors/mcpiscript/Planet?color=dark-green) ![Issues](https://img.shields.io/github/issues/mcpiscript/Planet) ![License](https://img.shields.io/github/license/mcpiscript/Planet) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmcpiscript%2FPlanet&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) ![Discord](https://img.shields.io/discord/936428193521487953?color=blue&label=Discord%20server&logo=Discord&logoColor=blue) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/mcpiscript/planet?label=Commits) ![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/mcpiscript/planet/latest/master) ![GitHub last commit](https://img.shields.io/github/last-commit/mcpiscript/planet) ![GitHub Release Date](https://img.shields.io/github/release-date/mcpiscript/planet?label=Latest%20release%20date) ![GitHub repo size](https://img.shields.io/github/repo-size/mcpiscript/planet) [![Crowdin](https://badges.crowdin.net/planet-launcher/localized.svg)](https://crowdin.com/project/planet-launcher)

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://github.com/mcpiscript/Planet/raw/master/screenshot.png)

The Minecraft Pi: Reborn mod is a great addition to the game. However, as fun as it can be, there is a big problem. The built-in launcher is too annoying. You have to type in every single field to just remember that you forgot to turn on a teeny little flag. **Planet fixes that.**
Instead of making you type in every single field, Planet lets you write it one time, auto-save, and forget for the rest of your life. With Planet you can even edit the world names and it supports the newly-introduced Reborn AppImages. It is also maintained unlike the other launchers.


## Built With

* The GUI is made using the PyQt5 Qt binding for Python, and additional widgets from qtwidgets.
* Big thanks to `pypresence` developers, for making such a good interface to Discord RPC.
* Thanks to `pyqtdarktheme` and `darkdetect` for awesome Qt theming tools.
* Pillow was used for skin manipulation
* PyNBT is used for the built-in MCPIedit
* `click` is an awesome interface, unfortunately, not to handle autoclickers, but for CLI interfaces used in the texture pack tool.


## Installation
#### Prerequisites
* [Minecraft Pi: Reborn](https://jenkins.thebrokenrail.com) AppImage or DEB install
* PyQt5
* Python 3
* `pypresence`
* `qtdarktheme`
* Pillow
* `qtwidgets`
* `darkdetect`
* PyNBT
* `click`

If you're installing a DEB, all of them with the exception of Minecraft: Pi Edition: Reborn will be automatically installed. Please install an AppImage for the latest build. If you want a DEB, please consider checking out [MCPI++](https://github.com/mobilegmyt/mcpi-reborn-extended).
#### Installation
###### Option A (Raspberry Pi Only)
[![badge](https://github.com/Botspot/pi-apps/blob/master/icons/badge.png?raw=true)](https://github.com/Botspot/pi-apps)  
###### Option B (Raspberry Pi Only)
[<img src="https://cdn.discordapp.com/attachments/717494538205397052/957080742293295134/addonsmini.png" alt="Logo" width="160" height="80">](https://raspbian-addons.org)


Install the `planet-launcher` package through APT.
###### Option C (Any Debian-Based)
Use [our PPA](https://github.com/mcpiscript/ppa)
###### Option D (Manual Installation) 
1. Download the DEB from the releases section.
2. Install the DEB using `apt`
3. Follow the on-screen instructions



## Alternatives
### gMCPIL vs jMCPIL vs pipan vs Planet
| Feature | Planet | [gMCPIL](https://github.com/mcpi-revival/gmcpil) | [jMCPIL](https://github.com/mcpi-revival/jmcpil) | [pipan](https://github.com/randomsoup/pipan) | Built-in launcher |
|---------|--------|--------|--------|-------|------|
| Profile & feature saving | Yes | Bullseye only | Yes | No | No |
| AppImage support | Yes | No | No | No | Yes |
| Legacy DEB support | Yes | Yes | Yes | Yes | Yes |
| Official MCPi-Revival | No | Yes | Yes | No | Yes |
| Tab icons | Yes | No | No | No | No |
| Maintained | Yes | No | No | No | Yes |
| Supported on Debian Buster | Yes, some bugs exist | No | Yes | Yes | Yes |
| Discord RPC | Yes | No | No | No | No |
| External server support | Yes | Yes | Yes | No | No |
| Flatpak support | Not tested | No | No | No | Yes |
| Pre-made profiles | Yes | Yes | Yes | Yes | No |
| Easy GUI navigation | Yes | Yes | Yes | No | Yes |
| Skin support | Yes | No | No | No | No |
| Built-in NBT editor | Yes | No | No | No | No |
###### Conclusion
- Use Planet if you want a maintained and a feature-rich launcher.
- Use gMCPIL if you are on Debian Bullseye, using a DEB install OR want a basic experience
- Use jMCPIL if you're using a DEB install on a distro other than Debian Bullseye
- Use the built-in launcher if you like to fill in things constantly
- Don't use pipan, it's a dirty prototype, not a working launcher

## Roadmap

- [x] AppImage support
- [x] Skin support
- [x] NBT editor
- [x] Localization system [![Crowdin](https://badges.crowdin.net/planet-launcher/localized.svg)](https://crowdin.com/project/planet-launcher)
- [ ] Texture packs (In progress)
- [ ] Mods
- [ ] Chat logging
- [ ] MarketPi
- [ ] World generation from seed

## Contributing

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Adding a translation
[![Crowdin](https://badges.crowdin.net/planet-launcher/localized.svg)](https://crowdin.com/project/planet-launcher)

1. Register an account on [Crowdin](https://crowdin.com)
2. Go to our [project page](https://crowdin.com/project/planet-launcher)
3. Start translating. If the desired langauge is not available, start a new thread.
4. Patiently wait until your translation is reviewed and added.

Please don't add fake translations, invalid or rude translations.

## License

Planet is licensed under the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html)


![Logo](https://www.gnu.org/graphics/agplv3-with-text-162x68.png)



## Acknowledgements

- [Leha-code](https://github.com/leha-code) - Creator and maintainer
- [Red-exe-engineer](https://github.com/red-exe-engineer) - Active contributor
- [Bigjango13](https://github.com/bigjango13) - Multiple fixes

### Translations
- Spanish translation by [BasedSkeleton](https://github.com/basedskeleton)
- Russian translation by [Leha-code](https://github.com/leha-code)

### Additional Credits
- Heart, Planet, Pi, Steve and Portal icons by LEHAtupointow.
- Wrench by [Santoniche on OpenGameArt.org](https://opengameart.org/content/wrench-0).
