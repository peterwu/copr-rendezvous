%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision 3c7c24acd542be8477de33abd2b416cf0805a25b
%global         git_revision_short %(echo %{git_revision} | head -c 7)

%global         source_name Tela-icon-theme

Name:           tela-icon-theme
Version:        %{build_timestamp}
Release:        %{git_revision_short}%{?dist}
Summary:        A flat colorful Design icon theme 

License:        GNU General Public License v3.0
URL:            https://github.com/vinceliuice/%{source_name}
Source0:        %{url}/archive/%{git_revision}.tar.gz

BuildArch:      noarch

BuildRequires:  gtk-update-icon-cache

%description
A flat colorful Design icon theme 

%prep
%setup -q -n %{source_name}-%{git_revision}

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir -p %{buildroot}%{_datadir}/icons
./install.sh -d %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc README.md
%{_datadir}/icons/*

%changelog
* Wed Dec 23 11:50:04 EST 2020 Peter Wu <peterwu@hotmail.com>
- git release 3c7c24acd542be8477de33abd2b416cf0805a25b
