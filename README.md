# My [TaigiKeyboard](https://github.com/taigikeyboard/taigikeyboard) packaging

## Ubuntu

This is published as a PPA at <https://launchpad.net/~kisaragi-hiu/+archive/ubuntu/taigikeyboard>.

To install:

``` sh
sudo add-apt-repository ppa:kisaragi-hiu/taigikeyboard
sudo apt update
```

Then depending on if you use fcitx5 or ibus:

``` sh
sudo apt install fcitx5-taigikeyboard
# or
sudo apt install ibus-taigikeyboard
```

See [./ubuntu/README.org](./ubuntu/README.org) for details on packaging.

## Fedora

This is published to COPR at <https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/>.

To install:

``` sh
sudo dnf copr enable kisaragi-hiu/taigikeyboard
```

Then depending on if you use fcitx5 or ibus:

``` sh
sudo dnf install fcitx5-taigikeyboard
# or
sudo dnf install ibus-taigikeyboard
```

See [./fedora/README.org](./fedora/README.org) for details on packaging.

## Arch

I added [my AUR package](https://aur.archlinux.org/pkgbase/taigikeyboard) as a submodule here for convenience.

Just install [`fcitx5-taigikeyboard`](https://aur.archlinux.org/packages/fcitx5-taigikeyboard)<sup>AUR</sup> or [`ibus-taigikeyboard`](https://aur.archlinux.org/packages/ibus-taigikeyboard)<sup>AUR</sup> from the AUR depending on if you use fcitx5 or ibus.

## Others

Debian: somehow use the Ubuntu package? Make the PPA build for Debian as well? use OBS instead?
openSUSE: set up OBS? or use COPR?
Gentoo, Nix, or even FreeBSD: I feel like writing the declaration for these isn't that hard?
