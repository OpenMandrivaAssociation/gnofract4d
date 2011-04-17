Name:           gnofract4d
Version:        3.13
Release:        %mkrel 2
Group:          Graphics
License:        BSD
Summary:        Gnofract 4D: Superior Fractal Software
Source:         %{name}-%{version}.tar.gz
Patch0:		gnofract4d-3.13-fix_desktop_file.patch
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
