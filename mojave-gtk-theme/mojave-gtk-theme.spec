%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision 2a6bbd678cb521fbb472fc978744de403da0b6d5
%global         git_revision_short %(echo %{git_revision} | head -c 7)

%global         source_name Mojave-gtk-theme

Name:           mojave-gtk-theme
Version:        %{build_timestamp}
Release:        %{git_revision_short}%{?dist}
Summary:        Mojave is a macos Mojave like theme for GTK 3, GTK 2 and Gnome-Shell  

License:        GNU General Public License v3.0
URL:            https://github.com/vinceliuice/%{source_name}
Source0:        %{url}/archive/%{git_revision}.tar.gz

Patch0:         show-apps-icon.patch 

BuildArch:      noarch

BuildRequires:  gtk-murrine-engine
BuildRequires:  gtk2-engines
BuildRequires:  glib2-devel
BuildRequires:  sassc

%description
Mojave is a macos Mojave like theme for GTK 3, GTK 2 and Gnome-Shell  

%prep
%autosetup -p1 -n %{source_name}-%{git_revision}

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir -p %{buildroot}%{_datadir}/themes 
./install.sh --dest %{buildroot}%{_datadir}/themes --icon fedora

%files
%license COPYING
%doc README.md HACKING
%{_datadir}/themes/*

%changelog
* Wed Dec 23 11:50:04 EST 2020 Peter Wu <peterwu@hotmail.com>
- git release 2a6bbd678cb521fbb472fc978744de403da0b6d5
