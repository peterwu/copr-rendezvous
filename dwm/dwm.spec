%global debug_package %{nil}

Name:           dwm
Version:        6.3
Release:        1%{?dist}
Summary:        Dynamic Window Manager

Group:          User Interface/Desktops
License:        MIT
URL:            http://dwm.suckless.org
Source0:        https://github.com/peterwu/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  sed

%description
dwm is a dynamic window manager for X. It manages windows in tiled, monocle and floating layouts. All of the layouts can be applied dynamically, optimizing the environment for the application in use and the task performed.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
%{_mandir}/man1/dwm.1.gz
%{_bindir}/dwm

%changelog
* Mon 14 Mar 2022 04:55:38 PM EDT Peter Wu
- Release v6.3
