# My [TaigiKeyboard](https://github.com/taigikeyboard/taigikeyboard) packaging

這馬更新版本：[3.7.0](https://github.com/taigikeyboard/taigikeyboard/releases/tag/desktop-3.7.0)。

這寡套件會使設定軟體庫，予用者直接做系統更新來更新到新版本，毋免閣家己安裝。

遮的軟體庫 mā 支援 x86-64 以外的架構。

我佇遮 mā kā Taigi Keyboard 分做三个包：fcitx5-taigikeyboard、ibus-taigikeyboard、猶閣有兩爿攏需要的檔案佇 taigikeyboard-common。

這寡套件支援的發行版：

- [Ubuntu](#ubuntu)
- [Fedora](#fedora)
- [Bazzite](#bazzite)
- [openSUSE](#opensuse)
- [Arch](#arch)

## Ubuntu

PPA 公開佇 <https://launchpad.net/~kisaragi-hiu/+archive/ubuntu/taigikeyboard>.

編譯有予 x86_64、arm64、armhf kap riscv64 啟用。只支援 Ubuntu 26.04。

Ài 安裝：

``` sh
sudo add-apt-repository ppa:kisaragi-hiu/taigikeyboard
sudo apt update
# 若 fcitx5
sudo apt install fcitx5-taigikeyboard
# 若 ibus
sudo apt install ibus-taigikeyboard
```

Packaging 詳細會使看 [./ubuntu/README.org](./ubuntu/README.org)。

## Fedora

COPR 公開佇 <https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/>。

編譯有予 x86_64 kap aarch64 (arm64) 啟用。支援 Fedora 44、45、Rawhide。

Ài 安裝：

``` sh
sudo dnf copr enable kisaragi-hiu/taigikeyboard
# 若 fcitx5
sudo dnf install fcitx5-taigikeyboard
# 若 ibus
sudo dnf install ibus-taigikeyboard
```

Packaging 詳細會使看 [./copr/README.org](./copr/README.org)。

## openSUSE

COPR 的軟體庫 mā 有編譯予 openSUSE。

編譯有予 x86_64 kap aarch64 (arm64) 啟用。支援 Leap 16.0 kap Tumbleweed。

openSUSE Tumbleweed:

Ài 安裝：

``` sh
# 若是用 Tumbleweed
sudo zypper addrepo 'https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/repo/opensuse-tumbleweed/kisaragi-hiu-taigikeyboard-opensuse-tumbleweed.repo'
# 若是用 Leap 16.0
sudo zypper addrepo 'https://copr.fedorainfracloud.org/coprs/kisaragi-hiu/taigikeyboard/repo/opensuse-leap-16.0/kisaragi-hiu-taigikeyboard-opensuse-leap-16.0.repo'
# 然後不管佗一爿：
sudo zypper refresh

# 完成了後安裝：若 fcitx5
sudo zypper install fcitx5-taigikeyboard
# 若 ibus
sudo zypper install ibus-taigikeyboard
```

## Bazzite

其他用 Fedora / rpm-ostree 做基礎的 immutable distro 應該 mā 會使按呢安裝。

[用 Bazzite 寫的方式](https://docs.bazzite.gg/Installing_and_Managing_Software/rpm-ostree)添 COPR：

``` sh
sudo dnf copr enable kisaragi-hiu/taigikeyboard
```

閣來安裝：

``` sh
# 若 fcitx5
rpm-ostree install fcitx5-taigikeyboard
# 若 ibus
rpm-ostree install ibus-taigikeyboard
```

## Arch

佇這个版本庫為著我方便我 mā 有 kā 我做 ê [AUR package](https://aur.archlinux.org/pkgbase/taigikeyboard) 當做 submodule 加入遮內底。

用你的 AUR helper 來安裝 [`fcitx5-taigikeyboard`](https://aur.archlinux.org/packages/fcitx5-taigikeyboard)<sup>AUR</sup> 猶是 [`ibus-taigikeyboard`](https://aur.archlinux.org/packages/ibus-taigikeyboard)<sup>AUR</sup>。

Mā 會使用 [`fcitx5-taigikeyboard-git`](https://aur.archlinux.org/packages/fcitx5-taigikeyboard-git)<sup>AUR</sup> 猶是 [`ibus-taigikeyboard-git`](https://aur.archlinux.org/packages/ibus-taigikeyboard-git)<sup>AUR</sup>。

## 其他

- Debian: 若有人有需要我閣來想辦法設定 Open Build System。Mā 會使用看覓 Ubuntu ê PPA。
- Gentoo, Nix, FreeBSD: I feel like writing the declaration for these isn't that hard?
