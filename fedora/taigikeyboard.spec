Name: taigikeyboard
Version: 3.6.10
Release: %autorelease
Summary: An input method for Taiwanese Taigi
License: Apache-2.0
URL: https://taigikeyboard.tw
Source: https://github.com/taigikeyboard/taigikeyboard/archive/refs/tags/desktop-${version}.tar.gz
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
Requires: hicolor-icon-theme

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
%make_build build
%make_build component
%make_build build-fcitx5

%install
%make_install

%files -n taigikeyboard-common
%{_bindir}/taigikeyboard-settings
%{_datadir}/taigikeyboard/
%{_datadir}/applications/tw.taigikeyboard.Settings.desktop
%{_datadir}/icons/hicolor/*/apps/taigikeyboard.png
%files -n ibus-taigikeyboard
%{_libexecdir}/ibus-engine-taigikeyboard
%{_datadir}/ibus/component/taigikeyboard.xml
%files -n fcitx5-taigikeyboard
%{_libdir}/*/fcitx5/
%{_datadir}/fcitx5/

%changelog
%autochangelog
