%global debug_package %{nil}

Name:             st
Version:          0.8.5
Release:          1%{?dist}
Summary:          A simple terminal implementation for X
License:          MIT
URL:              http://%{name}.suckless.org/
Source0:          https://github.com/peterwu/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:          %{name}.desktop

BuildRequires:    binutils
BuildRequires:    coreutils
BuildRequires:    gcc
BuildRequires:    desktop-file-utils
BuildRequires:    libX11-devel
BuildRequires:    libXext-devel
BuildRequires:    libXft-devel
BuildRequires:    make
BuildRequires:    sed
Requires:         font(liberationmono)
Requires:         ncurses-base

%description
A simple virtual terminal emulator for X which sucks less.

%prep
%setup -q
# terminfo entries are provided by ncurses-base
sed -e "/tic .*st.info/d" -i Makefile

%build
CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license LICENSE
%doc FAQ LEGACY README TODO %{name}.info
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon 14 Mar 2022 03:42:52 PM EDT Peter Wu
- 0.8.5
