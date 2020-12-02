%global         debug_package %{nil}
%global         batch  828
%global         commit g0a95549d6

Name:           neovim
Version:        0.5.0
Release:        %{batch}~%{commit}%{?dist}
Summary:        Neovim %{version} nightly build

License:        Apache License Version 2.0
URL:            https://github.com/neovim/neovim
Source0:        %{url}/archive/nightly.tar.gz

BuildRequires:  ninja-build
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  patch
BuildRequires:  gettext

#Requires:       

%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%prep
%autosetup -n neovim-nightly

%build
%{__make} CMAKE_BUILD_TYPE=Release

%install
%{make_install} CMAKE_INSTALL_PREFIX=%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%license LICENSE
%doc BACKERS.md CONTRIBUTING.md README.md
%{_bindir}/nvim
%{_libdir}/nvim/parser/c.so
%{_datadir}/*

%changelog
* Tue Dec  1 15:16:59 EST 2020 Peter Wu - v0.5.0
- 828_g0a95549d6
