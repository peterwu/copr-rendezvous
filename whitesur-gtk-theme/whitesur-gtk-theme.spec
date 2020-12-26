%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision 77a3986d44fca1ebb03519a6640c1ccab77c3154
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
BuildRequires:  libnotify
BuildRequires:  dialog

%description
MacOS Big Sur like theme for Gnome desktops

%prep
%setup -q -n %{source_name}-%{git_revision}

%build
%__sed -i "/\$nautilus_sidebar_size/s/200px/220px/" %{_buildir}/%{source_name}-%{git_revision}/src/sass/gtk/_applications.scss
#%__sed -i "/\$selected_bg_color/s/#0860f2/${theme_color}/" %{_buildir}/%{source_name}-%{git_revision}/src/sass/_colors.scss
#%__sed -i "/\$panel_opacity/s/0.16/${panel_trans}/" %{_buildir}/%{source_name}-%{git_revision}/src/sass/_colors.scss
   

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir -p %{buildroot}%{_datadir}/themes 
./install.sh --dest %{buildroot}%{_datadir}/themes --icon fedora

%files
%license COPYING
%doc README.md HACKING
%{_datadir}/themes/*


%changelog
* Sat Dec 26 12:18:48 PM EST 2020 Peter Wu
- git commit 77a3986d44fca1ebb03519a6640c1ccab77c3154
* Fri Dec 25 09:15:53 PM EST 2020 Peter Wu
- git commit 64e54cbbecc121c7f07edc0bbb3a9ad4530c65c6
* Fri Dec 25 10:52:02 EST 2020 Peter Wu
- git commit c7886cf69c78a9de297260331250139d78138ee2
* Wed Dec 23 11:50:04 EST 2020 Peter Wu <peterwu@hotmail.com>
- git release b7523ac51d344fbc76622c878049338ff4ca04a4
