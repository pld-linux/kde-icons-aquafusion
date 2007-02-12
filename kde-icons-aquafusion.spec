%define		_name		AquaFusion
Summary:	KDE Icons Theme - AquaFusion
Summary(pl.UTF-8):   Motyw ikon dla KDE - AquaFusion
Name:		kde-icons-aquafusion
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	ftp://distfiles.pld-linux.org/src/%{_name}-20030130.tar.gz
# Source0-md5:	e83a8aee62aad62725e4150fb1fc0c4e
URL:		http://kde-look.org/content/show.php?content=4815
BuildRequires:	rpmbuild(macros) >= 1.123
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Icons Theme - AquaFusion.

%description -l pl.UTF-8
Motyw ikon dla KDE - AquaFusion.

%prep
%setup -q -n %{_name}-Devel

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}

cp -r 16x16 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
cp -r 22x22 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
cp -r 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
cp -r 48x48 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
cp -r 64x64 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
cp -r 128x128 $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
install index.desktop $RPM_BUILD_ROOT%{_iconsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_iconsdir}/%{_name}
