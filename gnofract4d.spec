Name:           gnofract4d
Version:        3.14
Release:        %mkrel 1
Group:          Graphics
License:        BSD
Summary:        Gnofract 4D: Superior Fractal Software
Source:         %{name}-%{version}.tar.gz
Patch0:		gnofract4d-3.13-fix_desktop_file.patch
Patch1:		gnofract4d-3.13-fix_libdl.patch
URL:            http://%{name}.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel
BuildRequires:  glibc-devel

%description
Gnofract 4D is a free, open source program which allows anyone to
create beautiful images called fractals. The images are automatically
created by the computer based on mathematical principles.
These include the Mandelbrot and Julia sets and many more.
You don't need to do any math: you can explore a universe of images
just using a mouse.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
python setup.py build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

#duplicate docs
rm -rf %{buildroot}%{_docdir}/%{name}

#fix rights
chmod 644 %{buildroot}%{_datadir}/%{name}/maps/royal.map

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}-logo.png
%{_datadir}/mime/packages/%{name}-mime.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{python_sitearch}/fract4d
%{python_sitearch}/fract4dgui
%{python_sitearch}/fractutils
%{python_sitearch}/%{name}-%{version}-py%{py_ver}.egg-info


%changelog
* Sun Oct 30 2011 Andrey Bondrov <abondrov@mandriva.org> 3.14-1mdv2011.0
+ Revision: 707897
- New version 3.14

* Mon Apr 18 2011 Olivier Faurax <ofaurax@mandriva.org> 3.13-3
+ Revision: 654809
- Patch to add libdl

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 3.13-2mdv2011.0
+ Revision: 594849
- rebuild for python 2.7
- fix install
- fix filelist (don't own /usr/share or /usr/lib{64,})
- fix file rights
- fix desktop file

* Sun Sep 19 2010 Olivier Faurax <ofaurax@mandriva.org> 3.13-1mdv2011.0
+ Revision: 579872
- New version 3.13 (oups)
- New version 3.13

* Mon Dec 28 2009 Olivier Faurax <ofaurax@mandriva.org> 3.12-1mdv2010.1
+ Revision: 483143
- import gnofract4d


