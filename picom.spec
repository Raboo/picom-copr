Name:           picom
Version:        12.5
Release:        1%{?dist}
Summary:        A lightweight compositor for X11

License:        MIT and MPL-2.0
URL:            https://github.com/yshui/picom
Source0:        %{url}/releases/download/v%{version}/picom-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  libconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  pcre2-devel
BuildRequires:  pixman-devel
BuildRequires:  dbus-devel
BuildRequires:  systemd-devel
BuildRequires:  asciidoc

%description
Picom is a lightweight compositor for X11. It was forked from compton, which
was a fork of xcompmgr-dana.

Picom adds some new features, such as window rules, active window blur,
and experimental backends.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE*
%doc README.md
%{_bindir}/picom
%{_mandir}/man1/picom.1*
%{_datadir}/applications/picom.desktop
%dir %{_sysconfdir}/xdg/picom.conf.d
%config(noreplace) %{_sysconfdir}/xdg/picom.conf.example
%{_unitdir}/picom.service

%changelog
* Thu Jun 27 2024 COPR User <user@example.com> - 12.5-1
- Update to version 12.5
- Initial build for EL8 and EL9
