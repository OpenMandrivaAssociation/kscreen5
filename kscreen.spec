%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Display Management software
Name:		kscreen5
Version:	5.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/kscreen-%{version}.tar.xz
BuildRequires:	extra-cmake-modules5
BuildRequires:	cmake(KF5Screen)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	ninja
BuildRequires:	cmake

%description
KCM and KDED modules for managing displays in KDE.

%files -f all.lang
%{_bindir}/kscreen-console
%{_libdir}/qt5/plugins/*.so
%{_datadir}/icons/*/*/*
%{_datadir}/kcm_kscreen
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/*.desktop

#------------------------------------------------------------------------------

%prep
%setup -qn kscreen-%{version}

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja install -C build
%find_lang kcm_displayconfiguration
%find_lang kscreen
%find_lang plasma_applet_org.kde.plasma.kscreen
cat *.lang >all.lang
