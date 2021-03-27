%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-fusion-fonts
Version:        5.1.0
Release:        1%{?dist}
Summary:        A custom font based on iosevka

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        iosevka-fusion.toml

BuildArch:      noarch

BuildRequires:  clang
BuildRequires:  npm
BuildRequires:  ttfautohint

%description
Based on Iosevka font, https://github.com/be5invis/Iosevka,
this font mixes elements from various fonts tailored to my personal taste.

%prep
%autosetup -n %{source_name}-%{version}
%__cp %SOURCE1 %{_builddir}/%{source_name}-%{version}/private-build-plans.toml

%build
npm install
npm run build -- ttf::iosevka-fusion

%install
%__rm -rf %{buildroot}
%__install -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fusion/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}

%clean
%__rm -rf %{buildroot}

%files
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/*

%changelog
* Sat Mar 27 10:51:18 AM EDT 2021 Peter Wu
- Release 5.1.0

* Mon Mar 22 09:31:24 AM EDT 2021 Peter Wu
- Release 5.0.9

* Sun Mar 14 20:14:53 EDT 2021 Peter Wu
- Release 5.0.8

* Sat Mar 13 18:44:38 EST 2021 Peter Wu
- Release 5.0.6

* Sat Mar  6 09:53:29 EST 2021 Peter Wu
- Release 5.0.5

* Sat Feb 27 15:45:02 EST 2021 Peter Wu
- Release 5.0.4

* Sat Feb 20 16:26:44 EST 2021 Peter Wu
- Release 5.0.3

* Thu Feb 18 16:57:55 EST 2021 Peter Wu
- Updated font's toml spec

* Wed Feb 17 09:15:00 EST 2021 Peter Wu
- Release 5.0.2

* Sun Feb 14 11:11:43 EST 2021 Peter Wu
- Release 5.0.1

* Sat Feb 13 09:48:10 EST 2021 Peter Wu
- change 7 to curly-serifless
- Release 5.0.0

* Sat Jan 16 09:20:29 EST 2021 Peter Wu
- Release v4.5.0

* Sat Jan  9 09:08:19 EST 2021 Peter Wu
- change i to serifed-flat-tailed
- Release v4.4.0

* Sat Jan  2 13:44:06 EST 2021 Peter Wu
- Release v4.3.0

* Sat Dec 26 09:29:58 EST 2020 Peter Wu - v4.2.0
- Release - v4.2.0

* Sat Dec 19 18:08:08 EST 2020 Peter Wu - v4.1.1
- Release - v4.1.1

* Sat Dec 19 09:10:46 EST 2020 Peter Wu - v4.1.0
- Release - v4.1.0

* Sat Dec 12 09:49:55 EST 2020 Peter Wu - v4.0.3
- Release - v4.0.3

* Sun Dec  6 10:35:59 EST 2020 Peter Wu - v4.0.2
- Release - v4.0.2

* Sat Dec  5 10:21:30 EST 2020 Peter Wu - v4.0.1
- Release - v4.0.1

* Tue Nov 17 11:42:02 EST 2020 Peter Wu - v4.0.0
- New Release - v3.7.1
