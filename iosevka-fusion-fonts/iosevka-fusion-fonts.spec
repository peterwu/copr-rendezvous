%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-fusion-fonts
Version:        21.1.1
Release:        1%{?dist}
Summary:        A custom font based on Iosevka

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        iosevka-fusion.toml

BuildArch:      noarch

%if 0%{?fedora} == 36
BuildRequires:  npm
%else
BuildRequires:  nodejs-npm
%endif

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
%__mkdir -p %{buildroot}%{_datadir}/fonts/%{name}

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bold.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Bold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bolditalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-BoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-book.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Book.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bookitalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-BookItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extrabold.ttf        \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraBold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extrabolditalic.ttf  \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraBoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extralight.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraLight.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extralightitalic.ttf \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraLightItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-heavy.ttf            \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Heavy.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-heavyitalic.ttf      \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-HeavyItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-italic.ttf           \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Italic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-light.ttf            \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Light.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-lightitalic.ttf      \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-LightItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-medium.ttf           \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Medium.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-mediumitalic.ttf     \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-MediumItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-regular.ttf          \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Regular.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-semibold.ttf         \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-SemiBold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-semibolditalic.ttf   \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-SemiBoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-thin.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Thin.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-thinitalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ThinItalic.ttf

%files
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/*

%changelog
* Wed 29 Mar 2023 09:53:22 PM EDT
- Release 21.1.1

* Sat 11 Mar 2023 05:17:16 PM EST
- Release 20.0.0

* Sat 04 Mar 2023 11:46:34 AM EST
- Release 19.0.1

* Thu 09 Feb 2023 04:22:55 PM EST
- Release 18.0.0

* Fri 03 Feb 2023 10:51:15 PM EST
- Release 17.1.0

* Fri 23 Dec 2022 12:42:31 PM EST
- Release 16.8.4

* Sun 18 Dec 2022 09:49:30 PM EST
- Rename fonts using Pascal naming convention

* Tue Nov 15 09:15:04 PM EST 2022
- Release 16.3.6

* Sat Jul 23 11:21:38 AM EDT 2022
- Release 15.6.1

* Sat 16 Jul 2022 10:53:47 AM EDT
- Release 15.6.0

* Sun 26 Jun 2022 04:32:48 PM EDT
- Release 15.5.2

* Sat 18 Jun 2022 04:02:10 PM EDT
- Release 15.5.1

* Fri 18 Mar 2022 11:15:57 PM EDT Peter Wu
- Release 15.0.2

* Sun Jul 25 11:46:21 AM EDT 2021 Peter Wu
- Release 8.0.0

* Thu Jul 22 12:31:16 PM EDT 2021 Peter Wu
- Release 7.3.3

* Wed Jul  7 03:20:14 PM EDT 2021 Peter Wu
- Release 7.2.6

* Thu Jul  1 12:44:06 PM EDT 2021 Peter Wu
- Release 7.2.3

* Sun Jun 27 09:53:48 AM EDT 2021 Peter Wu
- Release 7.2.1

* Sat Jun 26 11:26:09 AM EDT 2021 Peter Wu
- Release 7.2.0

* Mon Jun 21 11:31:01 AM EDT 2021 Peter Wu
- Release 7.1.1

* Sat Jun 19 09:26:40 AM EDT 2021 Peter Wu
- Release 7.1.0

* Thu Jun 10 04:35:18 PM EDT 2021 Peter Wu
- Release 7.0.4

* Mon May 31 09:45:20 AM EDT 2021 Peter Wu
- Release 7.0.2

* Sun May 30 09:41:17 AM EDT 2021 Peter Wu
- Release 7.0.1

* Sat May 29 10:08:01 AM EDT 2021 Peter Wu
- Release 7.0.0

* Tue May  4 09:46:05 AM EDT 2021 Peter Wu
- Release 6.1.3

* Sun May  2 09:47:12 AM EDT 2021 Peter Wu
- Release 6.1.2

* Sat May  1 11:10:06 PM EDT 2021 Peter Wu
- Release 6.1.1

* Sat May  1 10:37:28 AM EDT 2021 Peter Wu
- Release 6.1.0

* Sun Apr 25 10:37:50 AM EDT 2021 Peter Wu
- Release 6.0.1

* Sat Apr 24 12:21:07 PM EDT 2021 Peter Wu
- Release 6.0.0

* Sun Apr  4 09:32:33 AM EDT 2021 Peter Wu
- Release 5.2.1

* Sat Apr  3 11:51:03 AM EDT 2021 Peter Wu
- Release 5.2.0

* Sun Mar 28 07:24:56 PM EDT 2021 Peter Wu
- Release 5.1.1

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
