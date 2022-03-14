%global debug_package %{nil}

Name:           slock
Version:        1.4
Release:        1%{?dist}
Summary:        Simple X display locker
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        https://github.com/peterwu/%{name}/archive/refs/tags/my-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel

%description
This is the simplest X screen locker we are aware of.  It is stable and
quite a lot people in this community are using it every day when they
are out with friends or fetching some food from the local pub.

%prep
%setup -q -n %{name}-my-%{version}

sed -e 's/^CFLAGS =/CFLAGS +=/g' -e 's/^LDFLAGS = -s/LDFLAGS +=/g' -i config.mk
sed -e 's/explicit_bzero\.c//' -i config.mk && rm -f explicit_bzero.c
sed -e 's/^\t@/\t/' -i Makefile
sed -e 's/nogroup/nobody/' config.def.h > config.h

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README
%attr(4755, root, root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
# There is no freedesktop.org .desktop file because slock is basically a helper
# binary for light windowmanagers, and it shouldn't appear in applications menu

%changelog
* Mon 14 Mar 2022 04:41:03 PM EDT Peter Wu
- Release v1.4
