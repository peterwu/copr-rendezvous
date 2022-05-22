%global         debug_package %{nil}

Name:           emptty
Version:        0.8.0
Release:        1%{?dist}
Summary:        Dead simple CLI Display Manager on TTY

License:        MIT License
URL:            https://github.com/tvrzna/emptty
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

#BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  golang
BuildRequires:  libX11-devel
BuildRequires:  pam-devel

Requires:       dbus-x11

%description
Dead simple CLI Display Manager on TTY

%prep
%autosetup -n %{name}-%{version}

%build
%__make build

%install
%__rm -rf %{buildroot}

%__make install DESTDIR=%{buildroot}
%__make install-pam-fedora DESTDIR=%{buildroot}
%__make install-manual DESTDIR=%{buildroot}
%__make install-config DESTDIR=%{buildroot}
%__make install-systemd DESTDIR=%{buildroot}
%__make install-motd-gen DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/emptty/conf
%{_sysconfdir}/emptty/motd-gen.sh
%{_mandir}/man1/emptty.1.gz
%{_bindir}/emptty
%{_sysconfdir}/pam.d/emptty
/usr/lib/systemd/system/emptty.service

%changelog
* Sat 05 Mar 2022 03:46:10 PM EST
- New Release - v0.7.0

* Sun 22 May 2022 06:59:18 PM EDT
- New Release - v0.8.0
