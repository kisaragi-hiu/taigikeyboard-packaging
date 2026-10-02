Name: taigikeyboard
Version: 3.6.10
Release: 1%{?dist}
Summary: An input method for Taiwanese Taigi
License: Apache-2.0
URL: https://taigikeyboard.tw
Source0: https://github.com/taigikeyboard/taigikeyboard/archive/refs/tags/desktop-3.6.10.tar.gz
BuildRequires: make
BuildRequires: cargo
BuildRequires: pkgconf
BuildRequires: protobuf-compiler
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: fcitx5

%description
Taigi Keyboard is an input method for typing Taiwanese Taigi using standard
orthographies.

%package -n taigikeyboard-common
Summary: Common files for Taigi Keyboard

%package -n ibus-taigikeyboard
Summary: Taigi input method for IBus
Requires: taigikeyboard-common

%package -n fcitx5-taigikeyboard
Summary: Taigi input method for Fcitx5
Requires: taigikeyboard-common

%prep
%autosetup

%build
# todo
cd linux
make build
make component
make build-fcitx5

%install
# todo

%files
# todo, we will have 3 packages later

%changelog
# todo
