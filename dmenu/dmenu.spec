%global debug_package %{nil}

Name:           dmenu
Version:        5.1
Release:        1%{?dist}
Summary:        Generic menu for X
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        https://github.com/peterwu/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  sed

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It manages
huge amounts (up to 10.000 and more) of user defined menu items efficiently.

%prep
%autosetup

%build
%make_build \
  X11INC=%{_includedir} \
  X11LIB=%{_libdir} \
  CFLAGS='-std=c99 -pedantic -Wall $(INCS) $(CPPFLAGS) %{build_cflags}' \
  LDFLAGS='%{build_ldflags} $(LIBS)'

%install
%make_install PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/%{name}*
%{_bindir}/stest
%{_mandir}/man*/%{name}.*
%{_mandir}/man*/stest.*

%changelog
* Mon 14 Mar 2022 04:33:59 PM EDT Peter Wu
- Release 5.1
