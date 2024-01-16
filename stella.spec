%define enable_gl	1
%define enable_sound	1
%define enable_debugger	1
%define enable_joystick	1
%define enable_cheats	1
%define enable_static	0

Summary:	An Atari 2600 Video Computer System emulator
Name:		stella
Version:	6.7.1
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		https://stella-emu.github.io/
Source0:	https://github.com/stella-emu/stella/releases/download/%{version}/%{name}-%{version}-src.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	desktop-file-utils

BuildRequires:	glibc-static-devel

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was the most
popular home video game system of the early 1980's.  This emulator will run
most Atari ROM images, so that you can play your favorite old Atari 2600 games
on your PC.

%prep
%setup -q
perl -pi -e "s|.png||" src/unix/stella.desktop
perl -pi -e "s|$(INSTALL) -c -s|$(INSTALL) -c|" Makefile

%build
%setup_compile_flags
touch configure.in
./configure \
%if %{enable_gl}
	--enable-gl \
%else
	--disable-gl \
%endif
%if %{enable_sound}
	--enable-sound \
%else
	--disable-sound \
%endif
%if %{enable_debugger}
	--enable-debugger \
%else
	--disable-debugger \
%endif
%if %{enable_joystick}
	--enable-joystick \
%else
	--disable-joystick \
%endif
%if %{enable_cheats}
	--enable-cheats \
%else
	--disable-cheats \
%endif
%if %{enable_static}
	--enable-static \
%else
	--enable-shared \
%endif
	--docdir=%{_docdir}/stella \
	--prefix=%{_prefix} \
	--x-libraries=%{_prefix}/X11R6/%{_lib}

%make_build

%install
%make_install

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%files
%{_docdir}/stella/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

