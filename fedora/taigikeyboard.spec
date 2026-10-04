Name: taigikeyboard
Version: 3.6.10
Release: %autorelease
Summary: An input method for Taiwanese Taigi
License: Apache-2.0
URL: https://taigikeyboard.tw
Source: https://github.com/taigikeyboard/taigikeyboard/archive/refs/tags/desktop-%{version}.tar.gz
Patch: 0001-Remove-some-makefile-dependencies-for-more-control-o.patch
Patch: 0002-patch-do-not-install-fonts.patch
BuildRequires: cargo-rpm-macros
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: protobuf-compiler
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel

%description
Taigi Keyboard is an input method for typing Taiwanese Taigi using standard
orthographies.

%generate_buildrequires
cd linux
%cargo_generate_buildrequires
cd ../desktop
%cargo_generate_buildrequires

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
%autosetup -n %{name}-desktop-%{version} -p1
cd linux
%cargo_prep

%build
cd linux
# we can't use the upstream build target since we need to call cargo with
# fedora's registry etc. set up
%cargo_build
%make_build component
%make_build build-fcitx5

%install
cd linux
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
%{_libdir}/fcitx5/
%{_datadir}/fcitx5/

%changelog
%autochangelog
