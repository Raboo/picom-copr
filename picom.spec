%global oldname compton-ng

Name:           picom
Version:        12.5
Release:        1%{?dist}
Summary:        A lightweight compositor for X11

License:        MIT and MPL-2.0
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}//%{name}-%{version}.tar.gz

# BuildRequires:  gcc-c++
# BuildRequires:  pkgconfig
# BuildRequires:  libXext-devel
# BuildRequires:  libXcomposite-devel
# BuildRequires:  libXdamage-devel
# BuildRequires:  libXfixes-devel
# BuildRequires:  libXinerama-devel
# BuildRequires:  libXrandr-devel
# BuildRequires:  libXrender-devel
# BuildRequires:  systemd-devel

BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  git
%if 0%{?rhel} && 0%{?rhel} == 8
# For EL8, install newer meson via pip to get >= 0.61.0
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
%else
# For EL9+, use system meson package
BuildRequires:  meson
%endif
BuildRequires:  cmake
BuildRequires:  libconfig-devel
BuildRequires:  dbus-devel
BuildRequires:  libev-devel
BuildRequires:  libX11-devel
BuildRequires:  libX11-xcb
BuildRequires:  libxcb-devel
BuildRequires:  libGL-devel
BuildRequires:  libEGL-devel
BuildRequires:  libepoxy-devel
BuildRequires:  pcre2-devel
BuildRequires:  pixman-devel
BuildRequires:  uthash-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xcb-util-devel
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  rubygem-asciidoctor

# BuildRequires:  pkgconfig(dbus-1)
# BuildRequires:  pkgconfig(gl)
# BuildRequires:  pkgconfig(libconfig)
# BuildRequires:  pkgconfig(libpcre)
# BuildRequires:  pkgconfig(libxdg-basedir)
# BuildRequires:  pkgconfig(pixman-1)
# BuildRequires:  pkgconfig(x11)
# BuildRequires:  pkgconfig(xcb-composite)
# BuildRequires:  pkgconfig(xcb-damage)
# BuildRequires:  pkgconfig(xcb-image)
# BuildRequires:  pkgconfig(xcb-present)
# BuildRequires:  pkgconfig(xcb-randr)
# BuildRequires:  pkgconfig(xcb-render)
# BuildRequires:  pkgconfig(xcb-renderutil)
# BuildRequires:  pkgconfig(xcb-shape)
# BuildRequires:  pkgconfig(xcb-xfixes)
# BuildRequires:  pkgconfig(xcb-xinerama)
# BuildRequires:  pkgconfig(xcb)
# BuildRequires:  pkgconfig(xext)
# BuildRequires:  pkgconfig(xproto)

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
%if 0%{?rhel} && 0%{?rhel} == 8
# Install newer meson via pip for EL8 to get >= 0.61.0
pip3 install --user meson>=0.61.0
export PATH=$HOME/.local/bin:$PATH
%endif

%meson                  \
    -Dwith_docs=true    \
    --wrap-mode=default \
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
