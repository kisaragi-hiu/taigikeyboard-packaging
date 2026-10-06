# My [TaigiKeyboard](https://github.com/taigikeyboard/taigikeyboard) packaging

Setting up repositories allows the user side to simply do a normal system update in order to get new versions.

It also allows for relatively easily providing binary packages for many architectures.

## Ubuntu

This is published as a PPA at <https://launchpad.net/~kisaragi-hiu/+archive/ubuntu/taigikeyboard>.

Build is currently enabled for Ubuntu 26.04; for architectures x86_64 (amd64), arm64, armhf, and riscv64.

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

Build is currently enabled for Fedora 44, 45, and Rawhide; for architectures x86_64 and aarch64.

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

See [./copr/README.org](./copr/README.org) for details on packaging.

## openSUSE

The COPR build includes builds for openSUSE Leap 16.0 and Tumbleweed.

openSUSE Tumbleweed:

``` sh
sudo zypper addrepo 'https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/repo/opensuse-tumbleweed/kisaragi-hiu-taigikeyboard-opensuse-tumbleweed.repo'
sudo zypper refresh
```

openSUSE Leap 16.0:

``` sh
sudo zypper addrepo 'https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/repo/opensuse-leap-16.0/kisaragi-hiu-taigikeyboard-opensuse-leap-16.0.repo'
sudo zypper refresh
```

Then depending on if you use fcitx5 or ibus:

``` sh
sudo zypper install fcitx5-taigikeyboard
sudo zypper install ibus-taigikeyboard
```

## Bazzite

This should work for other Fedora / rpm-ostree based immutable distributions as well.

Add the COPR [the same way Bazzite documents it](https://docs.bazzite.gg/Installing_and_Managing_Software/rpm-ostree):

``` sh
sudo dnf copr enable kisaragi-hiu/taigikeyboard
```

Then depending on if you use fcitx5 or ibus:

``` sh
rpm-ostree install fcitx5-taigikeyboard
# or
rpm-ostree install ibus-taigikeyboard
```

Normal layering caveats apply, so hopefully I don't cause updates to be blocked.

## Arch

I added [my AUR package](https://aur.archlinux.org/pkgbase/taigikeyboard) as a submodule here for convenience.

Just install [`fcitx5-taigikeyboard`](https://aur.archlinux.org/packages/fcitx5-taigikeyboard)<sup>AUR</sup> or [`ibus-taigikeyboard`](https://aur.archlinux.org/packages/ibus-taigikeyboard)<sup>AUR</sup> from the AUR depending on if you use fcitx5 or ibus.

## Others

Debian: somehow use the Ubuntu package? Make the PPA build for Debian as well? use OBS instead?
openSUSE: set up OBS? or use COPR?
Gentoo, Nix, or even FreeBSD: I feel like writing the declaration for these isn't that hard?
