%global         debug_package %{nil}

Name:           victor-mono-fonts
Version:        1.5.4
Release:        1%{?dist}
Summary:        A free programming font with cursive italics and ligatures.

License:        SIL Open Font License 1.1
URL:            https://github.com/rubjo/victor-mono
Source0:        https://rubjo.github.io/victor-mono/VictorMonoAll.zip

BuildArch:      noarch

%description
Victor Mono is an open-source monospaced font with optional semi-connected
cursive italics and programming symbol ligatures.

%prep
%setup -q -c -n VictorMonoAll

%build


%install
%__mkdir -p %{buildroot}%{_datadir}/fonts/victor-mono-fonts
%__install -p -m 0644 %{_builddir}/VictorMonoAll/TTF/*.ttf  %{buildroot}%{_datadir}/fonts/victor-mono-fonts

%clean
%__rm -rf %{buildroot}

%files
%license LICENSE.txt
%{_datadir}/fonts/victor-mono-fonts/*

%changelog
* Tue 05 Jul 2022 12:38:47 PM EDT
- Release v1.5.4

* Wed May 18 21:45:04 EDT 2022 Peter Wu
- Release v1.5.3

* Sat 19 Mar 2022 12:00:08 PM EDT Peter Wu
- Release - v1.5.2
