%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Display Management software
Name:		kscreen5
Version:	5.6.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/kscreen-%{version}.tar.xz
BuildRequires:	cmake(KF5Screen)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	pkgconfig(kscreen2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(ECM)
Conflicts: kscreen

%description
KCM and KDED modules for managing displays in KDE.

%files -f all.lang
%{_bindir}/kscreen-console
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_datadir}/icons/*/*/*
%{_datadir}/kcm_kscreen
%{_datadir}/kservices5/*.desktop

#------------------------------------------------------------------------------

%prep
%setup -qn kscreen-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm_displayconfiguration
%find_lang kscreen
%find_lang plasma_applet_org.kde.plasma.kscreen
cat *.lang >all.lang
