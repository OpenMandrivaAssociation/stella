Name:			stella
Version:		3.5
Release:		%mkrel 1

%define enable_gl	1
%define enable_sound	1
%define enable_debugger	1
%define enable_snapshot	1
%define enable_joystick	1
%define enable_cheats	1
%define enable_static	0

Summary:	An Atari 2600 Video Computer System emulator
License:	GPLv2+
Group:		Emulators
URL:		http://stella.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz

BuildRequires:	SDL-devel
BuildRequires:	MesaGLU-devel
BuildRequires:	zlib-devel
%if %enable_snapshot
BuildRequires:	png-devel
%endif
BuildRequires:	desktop-file-utils
#ctags
BuildRequires:	xemacs-extras
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was the most
popular home video game system of the early 1980's.  This emulator will run
most Atari ROM images, so that you can play your favorite old Atari 2600 games
on your PC.

%prep
%setup -q
perl -pi -e "s|.png||" src/unix/stella.desktop

%build
touch configure.in
%configure \
%if %enable_gl
  --enable-gl \
%else
  --disable-gl \
%endif
%if %enable_sound
  --enable-sound \
%else
  --disable-sound \
%endif
%if %enable_debugger
  --enable-debugger \
%else
  --disable-debugger \
%endif
%if %enable_snapshot
  --enable-snapshot \
%else
  --disable-snapshot \
%endif
%if %enable_joystick
  --enable-joystick \
%else
  --disable-joystick \
%endif
%if %enable_cheats
  --enable-cheats \
%else
  --disable-cheats \
%endif
%if %enable_static
  --enable-static \
%else
  --enable-shared \
%endif
  --docdir=%{_docdir}/stella \
  --x-libraries=%{_prefix}/X11R6/%{_lib}

%make

%install
rm -rf %{buildroot}

make install-strip DESTDIR=%{buildroot}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/stella/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/icons/mini/%{name}.png
%{_datadir}/icons/large/%{name}.png

