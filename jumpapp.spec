# jumpapp.spec: specification for building the .rpm file

# Created with: rpmdev-newspec jumpapp

Name:           jumpapp
Version:        VERSION
Release:        1%{?dist}
Summary:        jump to another application, unconditionally

License:        MIT
URL:            https://github.com/mkropat/jumpapp
Source0:        %{name}_%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:	pandoc
Requires:       wmctrl

%description
Jumpapp focuses the window of the application you're interested in — assuming
it's already running — otherwise jumpapp launches the application for you.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} PREFIX=/usr install
mkdir -p %{buildroot}%{_unitdir}

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Mar 18 2022 Michael Kropat <mail@michael.kropat.name> - 1.2-1
- Add fallback for non-stacking window managers

* Wed Jun 20 2019 Michael Kropat <mail@michael.kropat.name> - 1.1-1
- Add -m option to toggle window visibility
- Change window-type filter logic to work better with Slack

* Mon Jul 2 2018 Michael Kropat <mail@michael.kropat.name> - 1.0-1
- Add -C option to center mouse
- Fix stacking order bug with >10 windows

* Sat Mar 4 2017 Michael Kropat <mail@michael.kropat.name> - 0.9-1
- Make `-t` support regex matching

* Tue Apr 12 2016 Michael Kropat <mail@michael.kropat.name> - 0.8-1
- Jump to last-focused window when switching applications
- Add `-t` title-matching option
- Add `-w` workspace-matching option

* Fri Mar 28 2014 Michael Kropat <mail@michael.kropat.name> - 0.2-1
- Window Cycling feature

* Thu Mar 27 2014 Michael Kropat <mail@michael.kropat.name> - 0.1-1
- Initial version
