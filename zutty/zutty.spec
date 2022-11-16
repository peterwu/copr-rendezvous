%global debug_package %{nil}

Name:           zutty
Version:        0.13
Release:        1%{?dist}
Summary:        X terminal emulator rendering through OpenGL ES Compute Shaders
License:        GNU General Public License v3.0
URL:            https://github.com/tomszilagyi/zutty
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  clang
BuildRequires:  python
BuildRequires:  libXmu-devel
BuildRequires:  libglvnd-devel
BuildRequires:  freetype-devel

%description
A high-end terminal for low-end systems

%prep
%autosetup

%build
python ./waf configure --prefix=/usr
python ./waf build

%install
python ./waf --destdir=%{buildroot} install

%{__mkdir} -p %{buildroot}%{_datadir}/applications
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps

%{__install} -p -m 0644 icons/zutty.desktop %{buildroot}%{_datadir}/applications/zutty.desktop
%{__install} -p -m 0644 icons/zutty.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/zutty.svg

%{__install} -p -m 0644 icons/zutty_16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/zutty.png
%{__install} -p -m 0644 icons/zutty_32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/zutty.png
%{__install} -p -m 0644 icons/zutty_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/zutty.png
%{__install} -p -m 0644 icons/zutty_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/zutty.png
%{__install} -p -m 0644 icons/zutty_96x96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/zutty.png
%{__install} -p -m 0644 icons/zutty_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/zutty.png

%files
%license LICENSE
%doc README.org
%{_bindir}/%{name}
%{_datadir}/applications/zutty.desktop
%{_datadir}/icons/hicolor/*

%changelog
* Tue Nov 15 09:20:12 PM EST 2022
- Release v0.13

* Thu 02 Jun 2022 10:34:55 PM EDT Peter Wu
- Release v0.12

* Fri 18 Mar 2022 09:04:43 PM EDT Peter Wu
- Release v0.11

