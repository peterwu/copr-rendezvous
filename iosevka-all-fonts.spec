%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka
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
%package -n %{name}-fonts
Summary:        Monospace, Default
%description -n %{name}-fonts
Iosevka Monospace, Default

%package -n %{name}-term-fonts
Summary:        Monospace, Default
%description -n %{name}-term-fonts
Iosevka Monospace, Default

%package -n %{name}-fixed-fonts
Summary:        Monospace, Default
%description -n %{name}-fixed-fonts
Iosevka Monospace, Default

# Iosevka Slab — Monospace, Slab-serif
%package -n %{name}-slab-fonts
Summary:        Monospace, Slab-serif
%description -n %{name}-slab-fonts
Iosevka Monospace, Slab-serif

%package -n %{name}-term-slab-fonts
Summary:        Monospace, Slab-serif
%description -n %{name}-term-slab-fonts
Iosevka Monospace, Slab-serif

%package -n %{name}-fixed-slab-fonts
Summary:        Monospace, Slab-serif
%description -n %{name}-fixed-slab-fonts
Iosevka Monospace, Slab-serif

# Iosevka Curly — Monospace, Curly Style
%package -n %{name}-curly-fonts
Summary:        Monospace, Curly Style
%description -n %{name}-curly-fonts
Iosevka Monospace, Curly Style

%package -n %{name}-term-curly-fonts
Summary:        Monospace, Slab-serif
%description -n %{name}-term-curly-fonts
Iosevka Monospace, Curly Style

%package -n %{name}-fixed-curly-fonts
Summary:        Monospace, Slab-serif
%description -n %{name}-fixed-curly-fonts
Iosevka Monospace, Curly Style

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%package -n %{name}-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n %{name}-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n %{name}-term-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n %{name}-term-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n %{name}-fixed-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n %{name}-fixed-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

# Iosevka SS01 — Monospace, Andale Mono Style
%package -n %{name}-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n %{name}-ss01-fonts
Iosevka Monospace, Andale Mono Style

%package -n %{name}-term-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n %{name}-term-ss01-fonts
Iosevka Monospace, Andale Mono Style

%package -n %{name}-fixed-ss01-fonts
Summary:        Monospace, Andale Mono Style
%description -n %{name}-fixed-ss01-fonts
Iosevka Monospace, Andale Mono Style

# Iosevka SS02 — Monospace, Anonymous Pro Style
%package -n %{name}-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n %{name}-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

%package -n %{name}-term-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n %{name}-term-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

%package -n %{name}-fixed-ss02-fonts
Summary:        Monospace, Anonymous Pro Style
%description -n %{name}-fixed-ss02-fonts
Iosevka Monospace, Anonymous Pro Style

# Iosevka SS03 — Monospace, Consolas Style
%package -n %{name}-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n %{name}-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n %{name}-term-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n %{name}-term-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n %{name}-fixed-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n %{name}-fixed-ss03-fonts
Iosevka Monospace, Consolas Style

# Iosevka SS04 — Monospace, Menlo Style
%package -n %{name}-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n %{name}-ss04-fonts
Iosevka Monospace, Menlo Style

%package -n %{name}-term-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n %{name}-term-ss04-fonts
Iosevka Monospace, Menlo Style

%package -n %{name}-fixed-ss04-fonts
Summary:        Monospace, Menlo Style
%description -n %{name}-fixed-ss04-fonts
Iosevka Monospace, Menlo Style

# Iosevka SS05 — Monospace, Fira Mono Style
%package -n %{name}-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n %{name}-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n %{name}-term-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n %{name}-term-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n %{name}-fixed-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n %{name}-fixed-ss05-fonts
Iosevka Monospace, Fira Mono Style

# Iosevka SS06 — Monospace, Liberation Mono Style
%package -n %{name}-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n %{name}-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n %{name}-term-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n %{name}-term-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n %{name}-fixed-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n %{name}-fixed-ss06-fonts
Iosevka Monospace, Liberation Mono Style

# Iosevka SS07 — Monospace, Monaco Style
%package -n %{name}-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n %{name}-ss07-fonts
Iosevka Monospace, Monaco Style

%package -n %{name}-term-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n %{name}-term-ss07-fonts
Iosevka Monospace, Monaco Style

%package -n %{name}-fixed-ss07-fonts
Summary:        Monospace, Monaco Style
%description -n %{name}-fixed-ss07-fonts
Iosevka Monospace, Monaco Style

# Iosevka SS08 — Monospace, Pragmata Pro Style
%package -n %{name}-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n %{name}-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n %{name}-term-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n %{name}-term-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n %{name}-fixed-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n %{name}-fixed-ss08-fonts
Iosevka Monospace, Monaco Style

# Iosevka SS09 — Monospace, Source Code Pro Style
%package -n %{name}-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n %{name}-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n %{name}-term-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n %{name}-term-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n %{name}-fixed-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n %{name}-fixed-ss09-fonts
Iosevka Monospace, Source Code Pro Style

# Iosevka SS10 — Monospace, Envy Code R Style
%package -n %{name}-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n %{name}-ss10-fonts
Iosevka Monospace, Envy Code R Style

%package -n %{name}-term-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n %{name}-term-ss10-fonts
Iosevka Monospace, Envy Code R Style

%package -n %{name}-fixed-ss10-fonts
Summary:        Monospace, Envy Code R Style
%description -n %{name}-fixed-ss10-fonts
Iosevka Monospace, Envy Code R Style

# Iosevka SS11 — Monospace, X Windows Fixed Style
%package -n %{name}-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n %{name}-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

%package -n %{name}-term-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n %{name}-term-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

%package -n %{name}-fixed-ss11-fonts
Summary:        Monospace, X Windows Fixed Style
%description -n %{name}-fixed-ss11-fonts
Iosevka Monospace, X Windows Fixed Style

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%package -n %{name}-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n %{name}-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n %{name}-term-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n %{name}-term-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n %{name}-fixed-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n %{name}-fixed-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

# Iosevka SS13 — Monospace, Lucida Style
%package -n %{name}-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n %{name}-ss13-fonts
Iosevka Monospace, Lucida Style

%package -n %{name}-term-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n %{name}-term-ss13-fonts
Iosevka Monospace, Lucida Style

%package -n %{name}-fixed-ss13-fonts
Summary:        Monospace, Lucida Style
%description -n %{name}-fixed-ss13-fonts
Iosevka Monospace, Lucida Style

# Iosevka SS14 — Monospace, JetBrains Mono Style
%package -n %{name}-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n %{name}-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n %{name}-term-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n %{name}-term-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n %{name}-fixed-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n %{name}-fixed-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

# Iosevka Aile — Quasi-proportional, Sans-serif
%package -n %{name}-aile-fonts
Summary:        Quasi-proportional, Sans-serif
%description -n %{name}-aile-fonts
Iosevka Quasi-proportional, Sans-serif

# Iosevka Etoile — Quasi-proportional, Slab-serif
%package -n %{name}-etoile-fonts
Summary:        Quasi-proportional, Slab-serif
%description -n %{name}-etoile-fonts
Iosevka Quasi-proportional, Slab-serif

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%package -n %{name}-sparkle-fonts
Summary:        Quasi-proportional, Hybrid, like iA Writer’s Duo
%description -n %{name}-sparkle-fonts
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

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}/ttf/*.ttf                  -t %{buildroot}%{_datadir}/fonts/%{name}-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term/ttf/*.ttf             -t %{buildroot}%{_datadir}/fonts/%{name}-term-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed/ttf/*.ttf            -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-slab/ttf/*.ttf             -t %{buildroot}%{_datadir}/fonts/%{name}-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-slab/ttf/*.ttf        -t %{buildroot}%{_datadir}/fonts/%{name}-term-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-curly/ttf/*.ttf            -t %{buildroot}%{_datadir}/fonts/%{name}-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-curly/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/%{name}-term-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-curly/ttf/*.ttf      -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-curly-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/%{name}-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-curly-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/%{name}-term-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-curly-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-curly-slab-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-term-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-term-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss01/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss01-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss02/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss02-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss03/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss07/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss07-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss10/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss10-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss11/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss11-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-fixed-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-fixed-ss14-fonts

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-aile/ttf/*.ttf    -t %{buildroot}%{_datadir}/fonts/%{name}-aile-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-etoile/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/%{name}-etoile-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/%{name}-sparkle/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/%{name}-sparkle-fonts


# Iosevka — Monospace, Default
%files -n %{name}-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fonts/*

%files -n %{name}-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-fonts/*

%files -n %{name}-fixed-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-fonts/*

# Iosevka Slab — Monospace, Slab-serif
%files -n %{name}-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-slab-fonts/*

%files -n %{name}-term-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-slabfonts/*

%files -n %{name}-fixed-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-slab-fonts/*

# Iosevka Curly — Monospace, Curly Style
%files -n %{name}-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-curly-fonts/*

%files -n %{name}-term-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-curly-fonts/*

%files -n %{name}-fixed-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-curly-fonts/*

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%files -n %{name}-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-curly-slab-fonts/*

%files -n %{name}-term-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-curly-slab-fonts/*

%files -n %{name}-fixed-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-curly-slab-fonts/*


# Iosevka SS01 — Monospace, Andale Mono Style
%files -n %{name}-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss01-fonts/*

%files -n %{name}-term-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss01-fonts/*

%files -n %{name}-fixed-ss01-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss01-fonts/*

# Iosevka SS02 — Monospace, Anonymous Pro Style
%files -n %{name}-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss02-fonts/*

%files -n %{name}-term-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss02-fonts/*

%files -n %{name}-fixed-ss02-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss02-fonts/*

# Iosevka SS03 — Monospace, Consolas Style
%files -n %{name}-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss03-fonts/*

%files -n %{name}-term-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss03-fonts/*

%files -n %{name}-fixed-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss03-fonts/*

# Iosevka SS04 — Monospace, Menlo Style
%files -n %{name}-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss04-fonts/*

%files -n %{name}-term-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss04-fonts/*

%files -n %{name}-fixed-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss04-fonts/*

# Iosevka SS05 — Monospace, Fira Mono Style
%files -n %{name}-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss05-fonts/*

%files -n %{name}-term-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss05-fonts/*

%files -n %{name}-fixed-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss05-fonts/*

# Iosevka SS06 — Monospace, Liberation Mono Style
%files -n %{name}-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss06-fonts/*

%files -n %{name}-term-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss06-fonts/*

%files -n %{name}-fixed-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss06-fonts/*

# Iosevka SS07 — Monospace, Monaco Style
%files -n %{name}-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss07-fonts/*

%files -n %{name}-term-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss07-fonts/*

%files -n %{name}-fixed-ss07-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss07-fonts/*

# Iosevka SS08 — Monospace, Pragmata Pro Style
%files -n %{name}-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss08-fonts/*

%files -n %{name}-term-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss08-fonts/*

%files -n %{name}-fixed-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss08-fonts/*

# Iosevka SS09 — Monospace, Source Code Pro Style
%files -n %{name}-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss09-fonts/*

%files -n %{name}-term-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss09-fonts/*

%files -n %{name}-fixed-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss09-fonts/*

# Iosevka SS10 — Monospace, Envy Code R Style
%files -n %{name}-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss10-fonts/*

%files -n %{name}-term-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss10-fonts/*

%files -n %{name}-fixed-ss10-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss10-fonts/*

# Iosevka SS11 — Monospace, X Windows Fixed Style
%files -n %{name}-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss11-fonts/*

%files -n %{name}-term-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss11-fonts/*

%files -n %{name}-fixed-ss11-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss11-fonts/*

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%files -n %{name}-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss12-fonts/*

%files -n %{name}-term-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss12-fonts/*

%files -n %{name}-fixed-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss12-fonts/*

# Iosevka SS13 — Monospace, Lucida Style
%files -n %{name}-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss13-fonts/*

%files -n %{name}-term-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss13-fonts/*

%files -n %{name}-fixed-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss13-fonts/*

# Iosevka SS14 — Monospace, JetBrains Mono Style
%files -n %{name}-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-ss14-fonts/*

%files -n %{name}-term-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-term-ss14-fonts/*

%files -n %{name}-fixed-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fixed-ss14-fonts/*

# Iosevka Aile — Quasi-proportional, Sans-serif
%files -n %{name}-aile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-aile-fonts/*

# Iosevka Etoile — Quasi-proportional, Slab-serif
%files -n %{name}-etoile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-etoile-fonts/*

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%files -n %{name}-sparkle-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-sparkle-fonts/*

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
