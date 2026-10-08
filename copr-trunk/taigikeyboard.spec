Name: taigikeyboard
Version: 3.6.13unreleased
Release: 3%{?dist}
Summary: An input method for Taiwanese Taigi
License: Apache-2.0
URL: https://taigikeyboard.tw
Source: https://github.com/taigikeyboard/taigikeyboard/archive/refs/heads/main.tar.gz
# BuildRequires: cargo-rpm-macros
BuildRequires: cargo
BuildRequires: make
BuildRequires: pkgconf
%if 0%{?suse_version}
BuildRequires: protobuf-devel
%else
BuildRequires: protobuf-compiler
%endif
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
Taigi Keyboard is an input method for typing Taiwanese Taigi using standard
orthographies.

# %generate_buildrequires
# cd linux
# %cargo_generate_buildrequires
# cd ../desktop
# %cargo_generate_buildrequires

%package -n taigikeyboard-common
Summary: Common files for Taigi Keyboard
Requires: hicolor-icon-theme

%description -n taigikeyboard-common
Common files as well as the settings app of Taigi Keyboard.

%package -n ibus-taigikeyboard
Summary: Taigi input method for IBus
Requires: taigikeyboard-common

%description -n ibus-taigikeyboard
Taigi Keyboard's IBus frontend.

%package -n fcitx5-taigikeyboard
Summary: Taigi input method for Fcitx5
Requires: taigikeyboard-common

%description -n fcitx5-taigikeyboard
Taigi Keyboard's Fcitx5 frontend.

%prep
%autosetup -n %{name}-main -p1
cd linux
# %cargo_prep

%build
cd linux
# We have to just let cargo download because taigikeyboard wants rusqlite 0.40
# while Fedora provides 0.38 currently.
# # we can't use the upstream build target since we need to call cargo with
# # fedora's registry etc. set up
# %cargo_build
%make_build build
%make_build component
%make_build build-fcitx5

%install
cd linux
%make_install LAYOUT=fedora INSTALL_FONTS=0

%files -n taigikeyboard-common
%{_bindir}/taigikeyboard-settings
%{_datadir}/taigikeyboard/
%{_datadir}/applications/tw.taigikeyboard.Settings.desktop
%{_datadir}/icons/hicolor/*/apps/taigikeyboard.png
%{_datadir}/icons/hicolor/*/apps/taigikeyboard*.png
%{_datadir}/licenses/taigikeyboard/
%files -n ibus-taigikeyboard
%{_libexecdir}/ibus-engine-taigikeyboard
%{_datadir}/ibus/component/taigikeyboard.xml
%files -n fcitx5-taigikeyboard
%{_libdir}/fcitx5/
%{_datadir}/fcitx5/

%changelog
# this is not an official package and I don't actually have anything to say, so
# just leave it blank (autochangelog is effortless but doesn't work for openSUSE)
