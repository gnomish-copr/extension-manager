%define         appid com.mattjakeman.ExtensionManager
Name:           extension-manager
Version:        0.6.3
Release:        0
Summary:        A utility for browsing and installing GNOME Shell Extensions
License:        GPL-3.0-or-later
URL:            https://github.com/mjakeman/extension-manager
Source0:        https://github.com/mjakeman/%{name}.git#tag=v%{version}
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libbacktrace-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.7
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       unzip

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
