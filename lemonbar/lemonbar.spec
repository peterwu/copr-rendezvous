%global debug_package %{nil}

%global         git_revision 0042efd2ec1477ab96eb044ebba72a10aefff21f
%global         git_revision_short %(echo %{git_revision} | head -c 8)
%global         build_timestamp %(date +"%Y%m%d")

Name:           lemonbar
Version:        1.4
Release:        %{build_timestamp}~%{git_revision_short}%{?dist}
Summary:        Featherweight lemon-scented bar
License:        MIT
URL:            https://gitlab.com/protesilaos/%{name}-xft
Source0:        %{url}/-/archive/xft-port/%{name}-xft-xft-port.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-podlators
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel

%description
lemonbar (formerly known as bar) is a lightweight statusbar based on XCB.
Provides full UTF-8 support, basic formatting, RandR and Xinerama support
and EWMH compliance without wasting your precious memory.

%prep
%autosetup -n %{name}-xft-xft-port

%build
%set_build_flags
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.pod
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon 14 Mar 2022 04:41:03 PM EDT Peter Wu
- Release v1.4
