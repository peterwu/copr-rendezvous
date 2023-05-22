%global debug_package %{nil}

Name:           herbstluftwm-utils
Version:        0.1
Release:        1%{?dist}
Summary:        Some little utils for my personal Herbstluftwm setup
License:        MIT License
URL:            https://github.com/peterwu/herbstluftwm-utils
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-g++
BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  ibus-devel

%description
Some simple Herbstlufwm utils

%prep
%autosetup

%build
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release
cmake --build build

%install
%{__mkdir} -p %{buildroot}%{_bindir}

%{__install} -p -m 0755 build/sysmon %{buildroot}%{_bindir}/sysmon
%{__install} -p -m 0755 scripts/brightnessctl %{buildroot}%{_bindir}/brightnessctl
%{__install} -p -m 0755 scripts/monitorctl %{buildroot}%{_bindir}/monitorctl
%{__install} -p -m 0755 scripts/sayonara %{buildroot}%{_bindir}/sayonara
%{__install} -p -m 0755 scripts/termbar %{buildroot}%{_bindir}/termbar
%{__install} -p -m 0755 scripts/termbar-protocol-handler %{buildroot}%{_bindir}/termbar-protocol-handler
%{__install} -p -m 0755 scripts/volumectl %{buildroot}%{_bindir}/volumectl

%{__mkdir} -p %{buildroot}%{_sysconfdir}/xdg/%{name}
%{__install} -p -m 0755 scripts/autostart %{buildroot}%{_sysconfdir}/xdg/%{name}/autostart
%{__install} -p -m 0644 scripts/termbar.kitty.conf %{buildroot}%{_sysconfdir}/xdg/%{name}/termbar.kitty.conf

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_sysconfdir}/xdg/%{name}/*

%changelog
* Sun 21 May 2023 09:51:51 PM EDT
- Release v0.1

