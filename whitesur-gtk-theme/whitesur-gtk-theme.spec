%define         _debugsource_template %{nil}

%global         build_timestamp %(date +"%Y%m%d")
%global         git_revision c8e4b2caf7fb556b529db7c15f9c3ecf51a7d9c7
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
%autosetup -n %{source_name}-%{git_revision}

%build

# remove the view-app-grid.svg
%__sed -i \
       -e "/view-app-grid.svg/d" \
       -e "/.show-apps .show-apps-icon/{n;s/transparent/\$selected_fg_color/}" \
       -e "/.show-apps:focus .show-apps-icon/{n;s/transparent/\$selected_fg_color/}" \
    %{_builddir}/%{source_name}-%{git_revision}/src/sass/gnome-shell/widgets/_dashboard.scss

# delete notify-send
# %__sed -i "/notify-send/d" %{_builddir}/%{source_name}-%{git_revision}/install.sh

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir -p %{buildroot}%{_datadir}/themes
./parse-sass.sh
./install.sh --icon fedora --dest %{buildroot}%{_datadir}/themes --size 280

%files
%license COPYING
%doc README.md HACKING
%{_datadir}/themes/*

%changelog
* Fri Jan 15 12:46:41 EST 2021 Peter Wu
- git commit c8e4b2caf7fb556b529db7c15f9c3ecf51a7d9c7
* Thu Jan 14 20:21:20 EST 2021 Peter Wu
- git commit 134e56a109e043de0ac9fb036aa078ee396eb70f
* Tue 29 Dec 2020 09:49:20 EST Peter Wu
- git commit ac5b9a31020ac4a0f381e06ba8dfdefaaf78166d
* Mon Dec 28 10:13:15 EST 2020 Peter Wu
- git commit b42965c6cfe28ccceba4472f176f9f0a70795d32
* Sun Dec 27 10:01:55 EST 2020 Peter Wu
- git commit 1c26ca64e654e13418b4c8375a26b637519b3ea4
* Sat Dec 26 14:18:48 EST 2020 Peter Wu
- remove libnotify (notify-send)
- use gnome's default show-apps icon
- git commit 77a3986d44fca1ebb03519a6640c1ccab77c3154
* Fri Dec 25 09:15:53 PM EST 2020 Peter Wu
- git commit 64e54cbbecc121c7f07edc0bbb3a9ad4530c65c6
* Fri Dec 25 10:52:02 EST 2020 Peter Wu
- git commit c7886cf69c78a9de297260331250139d78138ee2
* Wed Dec 23 11:50:04 EST 2020 Peter Wu <peterwu@hotmail.com>
- git release b7523ac51d344fbc76622c878049338ff4ca04a4
