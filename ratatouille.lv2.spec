%global		debug_package	%{nil}
%define		oname	Ratatouille.lv2

Summary:		A Neural Model loader and mixer
Name:		ratatouille.lv2
Version:		0.9.10
Release:		1
License:		BSD
Group:		Sound
Url:		https://github.com/ratatouille.lv2/ratatouille.lv2
Source0:	https://github.com/ratatouille.lv2/ratatouille.lv2/archive/%{version}/%{oname}-v%{version}-src.tar.xz
Patch0:		ratatouille-0.9.10-fix-installation-path.patch
BuildRequires:		cmake
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(cairo)
BuildRequires:		pkgconfig(jack)
BuildRequires:		pkgconfig(lv2)
BuildRequires:		pkgconfig(portaudio-2.0)
BuildRequires:		pkgconfig(sndfile)
BuildRequires:		pkgconfig(x11)

%description
Ratatouille is a Neural Model loader and mixer for Linux/Windows. It can load
two models, which can be *.nam files with the Neural Amp Modeler module, or
*.json or .aidax files with the RTNeural module.
The "Delay" control could add a small delay to overcome phasing issues, or to
add some color/reverb to the sound.
Optionally, Ratatouille could detect the phase offset and compensate it
internal. To round up your sound you can load two Impulse Response Files and
mix them to your needs. IR-files could be normalised on load, so that they
didn't influence the loudness.
It supports resampling when needed to match the expected sample rate of the
loaded models.

%files
%license LICENSE
%doc README.md
%{_bindir}/Ratatouille
%{_libdir}/lv2/%{oname}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-v%{version}


%build
%make_build


%install
%make_install
