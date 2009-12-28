Name:           gnofract4d
Version:        3.12
Release:        %mkrel 1
Group:          Graphics
License:        BSD
Summary:        Gnofract 4D: Superior Fractal Software
Source:         %{name}-%{version}.tar.gz
URL:            http://%{name}.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel

%description
Gnofract 4D is a free, open source program which allows anyone to
create beautiful images called fractals. The images are automatically
created by the computer based on mathematical principles.
These include the Mandelbrot and Julia sets and many more.
You don't need to do any math: you can explore a universe of images
just using a mouse.

%prep
%setup -q

%build
python setup.py build

%install
%__rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}%_prefix --install-lib=%{buildroot}%{_libdir}/python2.6/site-packages

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/%name
%{_prefix}/share
%{_libdir}



