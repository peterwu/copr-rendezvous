%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-fonts-all
Version:        4.0.0
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  clang
BuildRequires:  npm
BuildRequires:  ttfautohint

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

%prep
%autosetup -n %{source_name}-%{version}

# Iosevka — Monospace, Default
%package -n iosevka-fonts
Summary:        Monospace, Default
%description -n iosevka-fonts
Iosevka Monospace, Default

%package -n iosevka-term-fonts
Summary:        Monospace, Default
%description -n iosevka-term-fonts
Iosevka Monospace, Default

%package -n iosevka-fixed-fonts
Summary:        Monospace, Default
%description -n iosevka-fixed-fonts
Iosevka Monospace, Default

# Iosevka Slab — Monospace, Slab-serif
%package -n iosevka-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-slab-fonts
Iosevka Monospace, Slab-serif

%package -n iosevka-term-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-term-slab-fonts
Iosevka Monospace, Slab-serif

%package -n iosevka-fixed-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-fixed-slab-fonts
Iosevka Monospace, Slab-serif

# Iosevka Curly — Monospace, Curly Style
%package -n iosevka-curly-fonts
Summary:        Monospace, Curly Style
%description -n iosevka-curly-fonts
Iosevka Monospace, Curly Style

%package -n iosevka-term-curly-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-term-curly-fonts
Iosevka Monospace, Curly Style

%package -n iosevka-fixed-curly-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-fixed-curly-fonts
Iosevka Monospace, Curly Style

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%package -n iosevka-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n iosevka-term-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-term-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n iosevka-fixed-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-fixed-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

# Iosevka SS01 — Monospace, Andale Mono Style
%package -n iosevka-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n iosevka-ss01-fonts
Iosevka Monospace, Andale Mono Style

%package -n iosevka-term-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n iosevka-term-ss01-fonts
Iosevka Monospace, Andale Mono Style

%package -n iosevka-fixed-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n iosevka-fixed-ss01-fonts
Iosevka Monospace, Andale Mono Style

# Iosevka SS02 — Monospace, Anonymous Pro Style
%package -n iosevka-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n iosevka-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

%package -n iosevka-term-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n iosevka-term-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

%package -n iosevka-fixed-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n iosevka-fixed-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

# Iosevka SS03 — Monospace, Consolas Style
%package -n iosevka-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n iosevka-term-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-term-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n iosevka-fixed-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-fixed-ss03-fonts
Iosevka Monospace, Consolas Style

# Iosevka SS04 — Monospace, Menlo Style
%package -n iosevka-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n iosevka-ss04-fonts
Iosevka Monospace, Menlo Style

%package -n iosevka-term-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n iosevka-term-ss04-fonts
Iosevka Monospace, Menlo Style

%package -n iosevka-fixed-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n iosevka-fixed-ss04-fonts
Iosevka Monospace, Menlo Style

# Iosevka SS05 — Monospace, Fira Mono Style
%package -n iosevka-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n iosevka-term-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-term-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n iosevka-fixed-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-fixed-ss05-fonts
Iosevka Monospace, Fira Mono Style

# Iosevka SS06 — Monospace, Liberation Mono Style
%package -n iosevka-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n iosevka-term-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-term-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n iosevka-fixed-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-fixed-ss06-fonts
Iosevka Monospace, Liberation Mono Style

# Iosevka SS07 — Monospace, Monaco Style
%package -n iosevka-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n iosevka-ss07-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-term-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n iosevka-term-ss07-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-fixed-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n iosevka-fixed-ss07-fonts
Iosevka Monospace, Monaco Style

# Iosevka SS08 — Monospace, Pragmata Pro Style
%package -n iosevka-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-term-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-term-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-fixed-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-fixed-ss08-fonts
Iosevka Monospace, Monaco Style

# Iosevka SS09 — Monospace, Source Code Pro Style
%package -n iosevka-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n iosevka-term-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-term-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n iosevka-fixed-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-fixed-ss09-fonts
Iosevka Monospace, Source Code Pro Style

# Iosevka SS10 — Monospace, Envy Code R Style
%package -n iosevka-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n iosevka-ss10-fonts
Iosevka Monospace, Envy Code R Style

%package -n iosevka-term-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n iosevka-term-ss10-fonts
Iosevka Monospace, Envy Code R Style

%package -n iosevka-fixed-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n iosevka-fixed-ss10-fonts
Iosevka Monospace, Envy Code R Style

# Iosevka SS11 — Monospace, X Windows Fixed Style
%package -n iosevka-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n iosevka-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

%package -n iosevka-term-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n iosevka-term-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

%package -n iosevka-fixed-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n iosevka-fixed-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%package -n iosevka-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n iosevka-term-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-term-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n iosevka-fixed-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-fixed-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

# Iosevka SS13 — Monospace, Lucida Style
%package -n iosevka-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n iosevka-ss13-fonts
Iosevka Monospace, Lucida Style

%package -n iosevka-term-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n iosevka-term-ss13-fonts
Iosevka Monospace, Lucida Style

%package -n iosevka-fixed-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n iosevka-fixed-ss13-fonts
Iosevka Monospace, Lucida Style

# Iosevka SS14 — Monospace, JetBrains Mono Style
%package -n iosevka-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n iosevka-term-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-term-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n iosevka-fixed-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-fixed-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

# Iosevka Aile — Quasi-proportional, Sans-serif
%package -n iosevka-aile-fonts
Summary:        Quasi-proportional, Sans-serif
%description -n iosevka-aile-fonts
Iosevka Quasi-proportional, Sans-serif

# Iosevka Etoile — Quasi-proportional, Slab-serif
%package -n iosevka-etoile-fonts
Summary:        Quasi-proportional, Slab-serif
%description -n iosevka-etoile-fonts
Iosevka Quasi-proportional, Slab-serif

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%package -n iosevka-sparkle-fonts
Summary:        Quasi-proportional, Hybrid, like iA Writer’s Duo
%description -n iosevka-sparkle-fonts
Iosevka Quasi-proportional, Hybrid, like iA Writer’s Duo

%build
npm install
npm run build -- ttf::iosevka
npm run build -- ttf::iosevka-term
npm run build -- ttf::iosevka-fixed
npm run build -- ttf::iosevka-slab
npm run build -- ttf::iosevka-term-slab
npm run build -- ttf::iosevka-fixed-slab
npm run build -- ttf::iosevka-curly
npm run build -- ttf::iosevka-term-curly
npm run build -- ttf::iosevka-fixed-curly
npm run build -- ttf::iosevka-curly-slab
npm run build -- ttf::iosevka-term-curly-slab
npm run build -- ttf::iosevka-fixed-curly-slab

npm run build -- ttf::iosevka-ss01
npm run build -- ttf::iosevka-term-ss01
npm run build -- ttf::iosevka-fixed-ss01
npm run build -- ttf::iosevka-ss02
npm run build -- ttf::iosevka-term-ss02
npm run build -- ttf::iosevka-fixed-ss02
npm run build -- ttf::iosevka-ss03
npm run build -- ttf::iosevka-term-ss03
npm run build -- ttf::iosevka-fixed-ss03
npm run build -- ttf::iosevka-ss04
npm run build -- ttf::iosevka-term-ss04
npm run build -- ttf::iosevka-fixed-ss04
npm run build -- ttf::iosevka-ss05
npm run build -- ttf::iosevka-term-ss05
npm run build -- ttf::iosevka-fixed-ss05
npm run build -- ttf::iosevka-ss06
npm run build -- ttf::iosevka-term-ss06
npm run build -- ttf::iosevka-fixed-ss06
npm run build -- ttf::iosevka-ss07
npm run build -- ttf::iosevka-term-ss07
npm run build -- ttf::iosevka-fixed-ss07
npm run build -- ttf::iosevka-ss08
npm run build -- ttf::iosevka-term-ss08
npm run build -- ttf::iosevka-fixed-ss08
npm run build -- ttf::iosevka-ss09
npm run build -- ttf::iosevka-term-ss09
npm run build -- ttf::iosevka-fixed-ss09
npm run build -- ttf::iosevka-ss10
npm run build -- ttf::iosevka-term-ss10
npm run build -- ttf::iosevka-fixed-ss10
npm run build -- ttf::iosevka-ss11
npm run build -- ttf::iosevka-term-ss11
npm run build -- ttf::iosevka-fixed-ss11
npm run build -- ttf::iosevka-ss12
npm run build -- ttf::iosevka-term-ss12
npm run build -- ttf::iosevka-fixed-ss12
npm run build -- ttf::iosevka-ss13
npm run build -- ttf::iosevka-term-ss13
npm run build -- ttf::iosevka-fixed-ss13
npm run build -- ttf::iosevka-ss14
npm run build -- ttf::iosevka-term-ss14
npm run build -- ttf::iosevka-fixed-ss14

npm run build -- ttf::iosevka-aile
npm run build -- ttf::iosevka-etoile
npm run build -- ttf::iosevka-sparkle

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka/ttf/*.ttf                  -t %{buildroot}%{_datadir}/fonts/iosevka-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term/ttf/*.ttf             -t %{buildroot}%{_datadir}/fonts/iosevka-term-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed/ttf/*.ttf            -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-slab/ttf/*.ttf             -t %{buildroot}%{_datadir}/fonts/iosevka-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-slab/ttf/*.ttf        -t %{buildroot}%{_datadir}/fonts/iosevka-term-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly/ttf/*.ttf            -t %{buildroot}%{_datadir}/fonts/iosevka-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly/ttf/*.ttf      -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-aile/ttf/*.ttf    -t %{buildroot}%{_datadir}/fonts/iosevka-aile-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-etoile/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-etoile-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-sparkle/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-sparkle-fonts


# Iosevka — Monospace, Default
%files -n iosevka-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fonts/*

%files -n iosevka-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-fonts/*

%files -n iosevka-fixed-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-fonts/*

# Iosevka Slab — Monospace, Slab-serif
%files -n iosevka-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-slab-fonts/*

%files -n iosevka-term-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-slabfonts/*

%files -n iosevka-fixed-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-slab-fonts/*

# Iosevka Curly — Monospace, Curly Style
%files -n iosevka-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-fonts/*

%files -n iosevka-term-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-fonts/*

%files -n iosevka-fixed-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-fonts/*

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%files -n iosevka-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-slab-fonts/*

%files -n iosevka-term-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-slab-fonts/*

%files -n iosevka-fixed-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts/*


# Iosevka SS01 — Monospace, Andale Mono Style
%files -n iosevka-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss01-fonts/*

%files -n iosevka-term-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss01-fonts/*

%files -n iosevka-fixed-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss01-fonts/*

# Iosevka SS02 — Monospace, Anonymous Pro Style
%files -n iosevka-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss02-fonts/*

%files -n iosevka-term-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss02-fonts/*

%files -n iosevka-fixed-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss02-fonts/*

# Iosevka SS03 — Monospace, Consolas Style
%files -n iosevka-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss03-fonts/*

%files -n iosevka-term-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss03-fonts/*

%files -n iosevka-fixed-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss03-fonts/*

# Iosevka SS04 — Monospace, Menlo Style
%files -n iosevka-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss04-fonts/*

%files -n iosevka-term-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss04-fonts/*

%files -n iosevka-fixed-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss04-fonts/*

# Iosevka SS05 — Monospace, Fira Mono Style
%files -n iosevka-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss05-fonts/*

%files -n iosevka-term-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss05-fonts/*

%files -n iosevka-fixed-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss05-fonts/*

# Iosevka SS06 — Monospace, Liberation Mono Style
%files -n iosevka-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss06-fonts/*

%files -n iosevka-term-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss06-fonts/*

%files -n iosevka-fixed-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss06-fonts/*

# Iosevka SS07 — Monospace, Monaco Style
%files -n iosevka-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss07-fonts/*

%files -n iosevka-term-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss07-fonts/*

%files -n iosevka-fixed-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss07-fonts/*

# Iosevka SS08 — Monospace, Pragmata Pro Style
%files -n iosevka-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss08-fonts/*

%files -n iosevka-term-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss08-fonts/*

%files -n iosevka-fixed-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss08-fonts/*

# Iosevka SS09 — Monospace, Source Code Pro Style
%files -n iosevka-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss09-fonts/*

%files -n iosevka-term-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss09-fonts/*

%files -n iosevka-fixed-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss09-fonts/*

# Iosevka SS10 — Monospace, Envy Code R Style
%files -n iosevka-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss10-fonts/*

%files -n iosevka-term-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss10-fonts/*

%files -n iosevka-fixed-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss10-fonts/*

# Iosevka SS11 — Monospace, X Windows Fixed Style
%files -n iosevka-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss11-fonts/*

%files -n iosevka-term-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss11-fonts/*

%files -n iosevka-fixed-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss11-fonts/*

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%files -n iosevka-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss12-fonts/*

%files -n iosevka-term-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss12-fonts/*

%files -n iosevka-fixed-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss12-fonts/*

# Iosevka SS13 — Monospace, Lucida Style
%files -n iosevka-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss13-fonts/*

%files -n iosevka-term-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss13-fonts/*

%files -n iosevka-fixed-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss13-fonts/*

# Iosevka SS14 — Monospace, JetBrains Mono Style
%files -n iosevka-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss14-fonts/*

%files -n iosevka-term-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss14-fonts/*

%files -n iosevka-fixed-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss14-fonts/*

# Iosevka Aile — Quasi-proportional, Sans-serif
%files -n iosevka-aile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-aile-fonts/*

# Iosevka Etoile — Quasi-proportional, Slab-serif
%files -n iosevka-etoile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-etoile-fonts/*

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%files -n iosevka-sparkle-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-sparkle-fonts/*

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
