%global        _hardened_build 1

%global        build_timestamp %(date +"%Y%m%d")

%global        git_revision eff6f0c7f123a79d376f5b06c3a946efb797bb03
%global        git_revision_short %(echo %{git_revision} | head -c 7)

Summary:       GNU Emacs text editor
Name:          emacs
Version:       28.0.50
Release:       %{build_timestamp}~%{git_revision_short}%{?dist}
License:       GPLv3+ and CC0-1.0
URL:           http://www.gnu.org/software/emacs/
Source0:       https://github.com/emacs-mirror/emacs/archive/%{git_revision}.tar.gz

BuildRequires: gcc
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: dbus-devel
BuildRequires: giflib-devel
BuildRequires: glibc-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libjpeg-turbo
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXpm-devel
BuildRequires: ncurses-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: librsvg2-devel
BuildRequires: m17n-lib-devel
BuildRequires: libotf-devel
BuildRequires: libselinux-devel
BuildRequires: alsa-lib-devel
BuildRequires: gpm-devel
BuildRequires: liblockfile-devel
BuildRequires: libxml2-devel
BuildRequires: autoconf
BuildRequires: bzip2
BuildRequires: cairo
BuildRequires: texinfo
BuildRequires: gzip
BuildRequires: desktop-file-utils
BuildRequires: libacl-devel
BuildRequires: harfbuzz-devel
BuildRequires: jansson-devel
BuildRequires: systemd-devel

BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

BuildRequires: gnupg2

# For docs
BuildRequires: texinfo-tex
BuildRequires: texlive-eurosym

# Emacs doesn't run without dejavu-sans-mono-fonts, rhbz#732422
Requires:      desktop-file-utils
Requires:      dejavu-sans-mono-fonts
Requires(preun): %{_sbindir}/alternatives
Requires(posttrans): %{_sbindir}/alternatives

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with support for X windows.

%prep
%setup -q -n emacs-%{git_revision}
./autogen.sh

%build
export CFLAGS="-DMAIL_USE_LOCKF %{build_cflags}"
%set_build_flags

LDFLAGS=-Wl,-z,relro;  export LDFLAGS;

%configure --with-dbus --with-gif --with-jpeg --with-png --with-rsvg \
           --with-tiff --with-xft --with-xpm --with-x-toolkit=gtk3 --with-gpm=no \
           --with-xwidgets --with-modules --with-harfbuzz --with-cairo --with-json
#make bootstrap -j $(nproc --all)
%{__make} -j $(nproc --all)

# Since we are building from the git repo we must also build the info files.
%{__make} docs

%install
%{make_install} -j $(nproc --all)

# Remove the emacsclient desktop file
%{__rm} %{buildroot}%{_datadir}/applications/emacsclient.desktop

# Remove emacs.pdmp
%{__rm} %{buildroot}%{_libexecdir}/%{name}/%{version}/%{_host}/emacs.pdmp

# Remove devel header file
%{__rm} -f %{buildroot}%{_includedir}/emacs-module.h

%{__mv} %{buildroot}%{_bindir}/{etags,etags.emacs}
%{__mv} %{buildroot}%{_mandir}/man1/{ctags.1.gz,gctags.1.gz}
%{__mv} %{buildroot}%{_mandir}/man1/{etags.1.gz,etags.emacs.1.gz}
%{__mv} %{buildroot}%{_bindir}/{ctags,gctags}

%{__mv} %{buildroot}%{_infodir}/{info.info.gz,info.gz}

# Emacs 26.1 installs the upstream unit file to /usr/lib64 on 64bit archs, we don't want that
%{__mkdir} -p %{buildroot}%{_userunitdir}
%{__mv} %{buildroot}%{_libdir}/systemd/user/emacs.service %{buildroot}%{_userunitdir}/emacs.service

%preun
%{_sbindir}/alternatives --remove emacs %{_bindir}/emacs-%{version}

%posttrans
%{_sbindir}/alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version} 80

%files
%license etc/COPYING
%doc etc/NEWS BUGS README
%{_bindir}/*
%{_userunitdir}/emacs.service
%{_libexecdir}/%{name}/%{version}/%{_host}/hexl
%{_libexecdir}/%{name}/%{version}/%{_host}/movemail
%{_libexecdir}/%{name}/%{version}/%{_host}/rcs2log
%{_datadir}/*

%changelog
* Wed Dec  2 11:41:51 EST 2020 Peter Wu <peterwu@hotmail.com>
- git commit eff6f0c7f123a79d376f5b06c3a946efb797bb03
