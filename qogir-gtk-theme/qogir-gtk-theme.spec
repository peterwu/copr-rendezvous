%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision 22855049724a95c30c662a3eb050ede9d842efaa
%global         git_revision_short %(echo %{git_revision} | head -c 7)

%global         source_name Qogir-gtk-theme

Name:           qogir-gtk-theme
Version:        %{build_timestamp}
Release:        %{git_revision_short}%{?dist}
Summary:        Qogir is a flat Design theme for GTK

License:        GNU General Public License v3.0
URL:            https://github.com/vinceliuice/%{source_name}
Source0:        %{url}/archive/%{git_revision}.tar.gz

BuildArch:      noarch

BuildRequires:  gtk-murrine-engine
BuildRequires:  gtk2-engines
BuildRequires:  glib2-devel
BuildRequires:  sassc

%description
Qogir is a flat Design theme for GTK

%prep
%autosetup -n %{source_name}-%{git_revision}

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir -p %{buildroot}%{_datadir}/themes 
./install.sh --image --win --dest %{buildroot}%{_datadir}/themes --logo fedora --theme standard

%files
%license COPYING
%doc README.md HACKING
%{_datadir}/themes/*


%changelog
* Thu Dec 24 10:02:24 AM EST 2020 Peter Wu
- git release 22855049724a95c30c662a3eb050ede9d842efaa
