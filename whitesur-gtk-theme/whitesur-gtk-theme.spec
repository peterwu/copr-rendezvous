%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision b7523ac51d344fbc76622c878049338ff4ca04a4
%global         git_revision_short %(echo %{git_revision} | head -c 7)

%global         source_name WhiteSur-gtk-theme

Name:           whitesur-gtk-theme
Version:        %{build_timestamp}
Release:        %{git_revision_short}%{?dist}
Summary:        MacOS Big Sur like theme for Gnome desktops

License:        GNU General Public License v3.0
URL:            https://github.com/vinceliuice/%{source_name}
Source0:        %{url}/archive/%{git_revision}.tar.gz

BuildArch:      noarch

BuildRequires:  gtk-murrine-engine
BuildRequires:  gtk2-engines
BuildRequires:  glib2-devel
BuildRequires:  sassc
BuildRequires:  optipng
BuildRequires:  inkscape

%description
MacOS Big Sur like theme for Gnome desktops

%prep
%setup -q -n %{source_name}-%{git_revision}

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
- git release b7523ac51d344fbc76622c878049338ff4ca04a4
