%global oldname compton-ng

Name:           picom
Version:        12.5
Release:        1%{?dist}
Summary:        A lightweight compositor for X11

License:        MIT and MPL-2.0
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}//%{name}-%{version}.tar.gz

# BuildRequires:  gcc-c++
# BuildRequires:  meson
# BuildRequires:  ninja-build
# BuildRequires:  pkgconfig
# BuildRequires:  libconfig-devel
# BuildRequires:  libX11-devel
# BuildRequires:  libXext-devel
# BuildRequires:  libxcb-devel
# BuildRequires:  libXcomposite-devel
# BuildRequires:  libXdamage-devel
# BuildRequires:  libXfixes-devel
# BuildRequires:  libXinerama-devel
# BuildRequires:  libXrandr-devel
# BuildRequires:  libXrender-devel
# BuildRequires:  pcre2-devel
# BuildRequires:  pixman-devel
# BuildRequires:  dbus-devel
# BuildRequires:  systemd-devel
# BuildRequires:  asciidoc

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  uthash-devel

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)

Requires:       hicolor-icon-theme

Conflicts:      compton%{?_isa}

Provides:       %{oldname}%{?_isa} = %{version}-%{release}

Obsoletes:      %{oldname} =< 7.5-1

%description
Picom is a lightweight compositor for X11. It was forked from compton, which
was a fork of xcompmgr-dana.

Picom adds some new features, such as window rules, active window blur,
and experimental backends.

%prep
%autosetup -p1

%build
%meson               \
    -Dwith_docs=true \
    %{nil}
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING LICENSES/MPL-2.0 LICENSES/MIT
%doc README.md CONTRIBUTORS picom.sample.conf
%{_bindir}/%{name}*
%{_bindir}/compton*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_mandir}/man1/*.1*


%changelog
* Thu Jun 27 2024 Elias Abacioglu <1148206+Raboo@users.noreply.github.com> - 12.5-1
- Update to version 12.5
- Initial build for EL8 and EL9
